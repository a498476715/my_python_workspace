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
    #����Ĭ��Ϊ����
    date = date.today()
    #date =
    #date = date - timedelta(1)
    
    
    #for key in head.keys():
    #    data = pd.read_sql(sql_stock_trans, conn)
    product_name = ['����02','����01','�Գ�','��ѡ','��Ӫ']
    writer = pd.ExcelWriter('���׻���/���׻���'+str(date)+'.xlsx')
    workbook = writer.book
    for name in product_name:
        portsname = '\'%'+name+'%\''
        sql_fund_trans = ("select * from (select EntrustBS as 'ί�з���', SecurityName as '��������', convert(decimal(18,1), sum(TradeAmount)/10000)"
                 "as \"�ܶ�(��Ԫ)\" from jydb_all.dbo.dpTransDetails a where a.portsname like %s and securitytype = '3' and date = \'%s\'"
                 "group by SecurityName, EntrustBS) as a where a.[�ܶ�(��Ԫ)] > 0" % (portsname, date))
        sql_fund_pos = ("select * from (select SecurityName as \"��������\", convert(decimal(18,1),CurrentMarketValue/10000) as \"��ֵ(��Ԫ)\" "
                    "from dpPortDetails a where a.portsname like %s and securitytype = '3' and date = \'%s\') as a where a.[��ֵ(��Ԫ)] > 0" % (portsname, date))
        sql_stock_mkv = ("select convert(decimal(18,1),SUM(a.CurrentMarketValue)/10000) as \"��Ʊ��ֵ(��Ԫ)\" from dpPortDetails a "
                     "where a.portsname like %s and securitytype = '0' and date = \'%s\' " % (portsname, date))
        sql_stock_trans = ("select EntrustBS as 'ί�з���', convert(decimal(18,1),SUM(TradeAmount)/10000) as \"�ܶ�(��Ԫ)\" from jydb_all.dbo.dpTransDetails a "
                       "where a.portsname like %s and securitytype = '0' and date = \'%s\' group by EntrustBS"%(portsname, date))
        head = [['��Ʊ����',sql_stock_trans], ['��Ʊ�ֲ�',sql_stock_mkv], ['������',sql_fund_trans], ['����ֲ�',sql_fund_pos]]
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
        print(name + "\t\t���")
    writer.save()
    print('________________________________________________')
    print("ȫ�����")
            #print(pd_data)
#     print('��Ʊ����')
#     print(pd.read_sql(sql_stock_trans, conn))
#     print('_________________________________')
#     print('��Ʊ�ֲ�')
#     print(pd.read_sql(sql_stock_mkv, conn))
#     print('_________________________________')
#     print('������')
#     data = pd.read_sql(sql_fund_trans, conn)
#     generate_excel(data, '������')
#     print(data)
#     print('_________________________________')
#     print('����ֲ�')
#     data = pd.read_sql(sql_fund_pos, conn)
#     generate_excel(data, '����ֲ�')
#     print(data)
    
    #result = pd.read_sql(sql_fund_trans, conn)
    #a=result['balance'].values.to_string()+'��'
    #a = [str(item)+'��' for item in result['balance'].values]
    #print(a)
    #generate_excel(result)
    #print(result.to_html())
    
    
    
    
    
    
    