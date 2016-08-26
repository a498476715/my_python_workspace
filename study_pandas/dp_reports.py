# coding=gbk

import pandas as pd
import pypyodbc
from datetime import date
from datetime import timedelta
import xlsxwriter

from dplib import lloyd_lib
import dp_config as cfg

def sql_ret_to_readable(ret, report_type):
    readable_str=''
    if report_type == "fund_trans":
        
        return readable_str

def generate_excel(data, name):
    #workbook = xlsxwriter.Workbook('demo1.xlsx')
    data.to_excel(name+'.xlsx', sheet_name='Sheet1')
    #workbook.close()

if __name__ == "__main__":
    #result = connect_to_database('SQL Server', '112.74.196.62', '1433', 'jydb_all', 'dpadmin', 'dpadmin')
    conn = lloyd_lib.connect_to_database('SQL Server', '112.74.196.62', '1433', 'jydb_all', 'dpadmin', 'dpadmin')
    #日期默认为当日
    date = date.today()
    #date =
    #date = date - timedelta(1)
    
    
    #for key in head.keys():
    #    data = pd.read_sql(sql_stock_trans, conn)
    product_name = ['主动02','主动01','对冲','精选','自营']
    writer = pd.ExcelWriter('交易汇总/交易汇总'+str(date)+'.xlsx')
    workbook = writer.book
    for name in product_name:
        portsname = '\'%'+name+'%\''
        sql_fund_trans = ("select * from (select EntrustBS as '委托方向', SecurityName as '基金名称', convert(decimal(18,1), sum(TradeAmount)/10000)"
                 "as \"总额(万元)\" from jydb_all.dbo.dpTransDetails a where a.portsname like %s and securitytype = '3' and date = \'%s\'"
                 "group by SecurityName, EntrustBS) as a where a.[总额(万元)] > 0" % (portsname, date))
        sql_fund_pos = ("select * from (select SecurityName as \"基金名称\", convert(decimal(18,1),CurrentMarketValue/10000) as \"市值(万元)\" "
                    "from dpPortDetails a where a.portsname like %s and securitytype = '3' and date = \'%s\') as a where a.[市值(万元)] > 0" % (portsname, date))
        sql_stock_mkv = ("select convert(decimal(18,1),SUM(a.CurrentMarketValue)/10000) as \"股票市值(万元)\" from dpPortDetails a "
                     "where a.portsname like %s and securitytype = '0' and date = \'%s\' " % (portsname, date))
        sql_stock_trans = ("select EntrustBS as '委托方向', convert(decimal(18,1),SUM(TradeAmount)/10000) as \"总额(万元)\" from jydb_all.dbo.dpTransDetails a "
                       "where a.portsname like %s and securitytype = '0' and date = \'%s\' group by EntrustBS"%(portsname, date))
        head = [['股票交易',sql_stock_trans], ['股票持仓',sql_stock_mkv], ['基金交易',sql_fund_trans], ['基金持仓',sql_fund_pos]]
        pd_table_list = []
        row = 0
        for item in head:
            table_name = item[0]
            sql = item[1]
            pd_data = pd.read_sql(sql, conn)
            #pd_data.index = pd_data[pd_data.columns[0]]
            #print(pd_data)
            #pd_data = pd_data.iloc[:, 1:len(pd_data.columns)]
            pd_table_list.append(pd_data)
            
            #print(pd_data.to_json())
        #writer = pd.ExcelWriter(name+' '+str(date)+'.xlsx')
        row = 0
        #worksheet = workbook.add_worksheet(name)
        for dataframe in pd_table_list:
            dataframe.to_excel(writer, startrow = row, startcol = 1, sheet_name = name, index = False)
            worksheet = writer.sheets[name]
            row = row + len(dataframe.index) + 2
        print(name + "\t\t完成")
    writer.save()
    print('________________________________________________')
    print("全部完成")
            #print(pd_data)
#     print('股票交易')
#     print(pd.read_sql(sql_stock_trans, conn))
#     print('_________________________________')
#     print('股票持仓')
#     print(pd.read_sql(sql_stock_mkv, conn))
#     print('_________________________________')
#     print('基金交易')
#     data = pd.read_sql(sql_fund_trans, conn)
#     generate_excel(data, '基金交易')
#     print(data)
#     print('_________________________________')
#     print('基金持仓')
#     data = pd.read_sql(sql_fund_pos, conn)
#     generate_excel(data, '基金持仓')
#     print(data)
    
    #result = pd.read_sql(sql_fund_trans, conn)
    #a=result['balance'].values.to_string()+'万'
    #a = [str(item)+'万' for item in result['balance'].values]
    #print(a)
    #generate_excel(result)
    #print(result.to_html())
    
    
    
    
    
    
    