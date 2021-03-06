# coding=gbk

import lloyd_lib as llib
from datetime import timedelta

if __name__ == "__main__":
    #result = connect_to_database('SQL Server', '112.74.196.62', '1433', 'jydb_all', 'dpadmin', 'dpadmin')
    conn = llib.connect_to_database('SQL Server', '192.168.1.252', '1433', 'jydb_all', 'dpadmin', 'Dao2016pu')
    
    portsname = '\'%主动01%\''
    date = llib.date.today()
    date = date - timedelta(1)
    sql_fund_trans = ("select SecurityName, EntrustBS, convert(decimal(18,1), sum(TradeAmount)/10000)"
                 "as balance from jydb_all.dbo.dpTransDetails a where a.portsname like %s and securitytype = '3' and date = \'%s\'"
                 "group by SecurityName, EntrustBS" % (portsname, date))
    sql_fund_pos = ("select SecurityName, SecurityID, convert(decimal(18,1),CurrentMarketValue/10000) as '基金市值' "
                    "from dpPortDetails a where a.portsname like %s and securitytype = '3' and date = \'%s\'" % (portsname, date))
    sql_stock_mkv = ("select convert(decimal(18,1),SUM(a.CurrentMarketValue)/10000) as '股票市值' from dpPortDetails a "
                     "where a.portsname like %s and securitytype = '0' and date = \'%s\' " % (portsname, date))
    sql_stock_trans = ("select EntrustBS, SUM( TradeAmount) as balance from jydb_all.dbo.dpTransDetails a "
                       "where a.portsname like %s and securitytype = '0' and date = \'%s\' group by EntrustBS"%(portsname, date))
    
    result = llib.pd.read_sql(sql_stock_trans, conn)
    print(result)

