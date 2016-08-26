# coding=gbk

import pandas as pd
from pandas import Series
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

import helper
import dp_config
from django.dispatch.dispatcher import Signal

index_list = {}
index_list['hs300'] = '000300.SH'
index_list['zz500'] = '000905.SH'
index_list['sz50'] = '000016.SH'
index_list['cybz'] = '399006.SZ'
index_list['cybzh'] = '399102.SZ'

data_set = {}
start_date = '\'20010101\''
short = True

def get_index_from_db(wind_code, conn):
    '''
    ϣ�������Լ��������ݿ⣬���û�ȡ��ͬ����(��ʲô�۸�������)
    '''
    
    sql_string = ("select TRADE_DT, S_INFO_WINDCODE, S_DQ_CLOSE, S_DQ_PCTCHANGE " 
                  "from AINDEXEODPRICES " 
                  "where S_INFO_WINDCODE = \'%s\' and TRADE_DT > %s"
                  "order by TRADE_DT" % (wind_code, start_date))
    data = pd.read_sql(sql_string, conn, index_col='trade_dt', parse_dates=['trade_dt'])
#     data.columns = ['code', 'close', 'return']
    return data

def strategy_cross(data, short_term, long_term, short = True, short_ua = '000300.SH', freq = 'day', benchmark='self'):
    '''
    ���㽻����ԵĻر�������������ma�ߣ�һ���ź��ߣ�һ���������ߣ��Լ�һ������������
    short_term�Ƕ��ڵ��ߵĳ��ȣ�Ϊint����
    freq�ǲ��������ݻ��Ƿ������ݣ�ֵ�����ǣ�day�� min
    '''
    data = helper.delete_na(data)
    
    short_term_str = str(short_term)
    long_term_str = str(long_term)
    short_ma_str = 'ma_' + short_term_str
    long_ma_str = 'ma_' + long_term_str
    signal_line_str = 'sig_' + short_term_str + '_' + long_term_str
    ret_daily_str = 'ret_daily_' + short_term_str + '_' + long_term_str
    ret_cumprod = 'ret_sum_ma_' + short_term_str + '_' + long_term_str
    ua_pctchange_daily = 's_dq_pctchange'
    benchmark_code = data.iat[0,0]
    ret_cumprod_benchmark = 'ret_sum_' + benchmark_code
    #�����ݻ��߷�������
    if freq == 'day':
        close_str = 's_dq_close'
    elif freq == 'min':
        #������δʵ��
        print('This func does not support min data. ^_^')
        print('The system will be closed. Bye!')
        exit(1)
#     print(data[close_str])
    #����MA
    if short_ma_str not in data.columns:
        data[short_ma_str] = helper.ma_simple(data[close_str], short_term)
    if long_ma_str not in data.columns:
        data[long_ma_str] = helper.ma_simple(data[close_str], long_term)
    #�����ź�
    if signal_line_str not in data.columns:
        data[signal_line_str] = cal_signal(data.loc[:, [short_ma_str, long_ma_str]], strategy='cross')
    #����ÿ������%
    if ret_daily_str not in data.columns:
        data[ret_daily_str] = return_cross_daily(data.loc[:, [ua_pctchange_daily, short_ma_str, long_ma_str]], short, short_ua)
    #�����ۼ�����%����
    if ret_cumprod not in data.columns:
        data[ret_cumprod] = return_compound(data[ret_daily_str])
    #��ͼ
    if benchmark == 'self':
#         print('haha')
        if ret_cumprod_benchmark not in data.columns:
            data[ret_cumprod_benchmark] = return_compound(data[ua_pctchange_daily]/100)
#             print('hehhe')
    data = helper.delete_na(data)
    data_fig = data.loc[:,[ret_cumprod_benchmark, ret_cumprod]]
    data_fig.plot()
    plt.show()
    return data

# def return_benchmark(data, ):

def return_cross_daily(data, short = True, short_ua = '000300.SH'):
    '''
    ���ؽ��淽����ÿ��������
    ��Ҫ3�У��ֱ�Ϊ 0��������棬 1������ma��2������ma
    '''
    data['signal_line'] = cal_signal(data.iloc[:,1:3], strategy = 'cross')
    data = helper.delete_na(data)
    return_string = data.columns[0]
    signal_string = data.columns[3]
    if short:
        ret = (data.apply(lambda x: x[return_string] if x[signal_string] else -x[return_string], axis=1))/100
    else:
        ret = (data.apply(lambda x: x[return_string] if x[signal_string] else 0, axis=1))/100
    
    return ret

def return_compound(data):
    '''
    ��������, ����Ϊһ��������(���ǵ���)
    '''
    data = data + 1
    data = data.cumprod()
#     print(data)
    return data
    

def cal_signal(data, strategy = 'cross'):
    '''
    �����ź��У�TrueΪӦ�ö�ͷ��FalseΪӦ�ÿ�ͷ/�ղ�.
    Ĭ�ϵ��㷨Ϊ���淨,data��ԭdata����Ƭ��ֻ�ǽ�ȡ��Ҫ�����������
  1. ���淽��: ��Ҫ���У������ߺͳ����ߵ�MA�ߡ�short_term����ǰ��long_term���ں�
    �����ź���
    '''
    #��ֹ�õ�δ�����ݣ�Ҫshift 1λ
    if strategy == 'cross':
#         short_term = data.iloc[:,0]
#         long_term = data.iloc[:,1]
        signal_line = data.iloc[:,0] > data.iloc[:,1]
#         print(signal_line)
        signal_line = signal_line.shift(1)
#         print(signal_line)
        
    return signal_line     

def main():
    server = '253'
    db_name = 'wddb'
    conn = helper.connect_to_database(dp_config.db_driver[server], dp_config.db_ip[server], dp_config.db_port[server],
                                      'wddb', dp_config.db_usr[server], dp_config.db_pwd[server])
    
    # ���ñ����
    ua_string = index_list['zz500']
    ua = ua_string
    
    data = get_index_from_db(ua_string, conn)
    data = strategy_cross(data, 5, 20)
    print(data)
    data = strategy_cross(data, 5, 10)
    print(data)
 
if __name__ == '__main__':
    main()
    