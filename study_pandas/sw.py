# encoding=gbk

import datetime
import sys
import pandas as pd
from pandas import DataFrame as df

# from WindPy import w     
from WindPy import w

import dplib.lloyd_lib
import dp_config as cfg

name_dict = {}
name_dict['S_INFO_WINDCODE'] = 'Wind����'
name_dict['trade_dt'] = '����'
name_dict['con_num'] = '�ɷֹ�����'
name_dict['pe_lyr'] = '��ӯ��(PE,LYR)'
name_dict['pe_ttm'] = '��ӯ��(PE,TTM)'
name_dict['pb_lf'] = '�о���(PB,LF)'
name_dict['pcf_lyr'] = '������(PCF,LYR)'
name_dict['pcf_ttm'] = '������(PCF,TTM)'
name_dict['ps_lyr'] = '������(PS,LYR)'
name_dict['ps_ttm'] = '������(PS,TTM)'
name_dict['MV_TOTAL'] = '��������ֵ�ϼƣ�Ԫ��'
name_dict['MV_FLOAT'] = '������ͨ��ֵ�ϼƣ�Ԫ��'
name_dict['dividend_yield'] = '��Ϣ��'
name_dict['TOT_SHR_FLOAT'] = '��ͨ�ɱ��ϼƣ��ɣ�'
name_dict['TOT_SHR_FREE'] = '������ͨ�ɱ��ϼƣ��ɣ�'
name_dict['turnover'] = '������'
name_dict['turnover_free'] = '������(������ͨ)'
# name_dict[''] = ''

def get_his_data(sec_windcode):
    sql = 

if __name__ == "__main__":
    w.start(showmenu=False)
    # ����һ��28����ҵ���룬����
    sw_sec = df(w.wset("SectorConstituent", "date=20160805;sectorId=a39901011g000000").Data[1:3], index=['����', '�������'])
    sw_sec = sw_sec.T
    sw_sec.index += 1
    sw_sec.index.name = '���'
#     for key in sw
    print(sw_sec)
#     print(w.wset("SectorConstituent","date=20160805;sectorId=a39901011g000000").Data[1])
    
    
