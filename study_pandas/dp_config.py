# coding=gbk

#############################################################################
# 用于 道朴产品名称
product_std_names = ['招商主动1号','中信主动2号','中信自营','对冲1号','精选1号']
product_sql_names = ['主动01','主动02', '对冲', '精选', '自营']

#############################################################################
# 用于数据库, 均以db开头
db_types = {'SQLServer': 'SQL Server'}

db_driver = {}
db_ip = {}
db_port = {}
db_name = {} # 要使用的数据库的名字，每个server会设置默认数据库
db_usr = {}
db_pwd = {}


# 252 服务器
# 252的所有数据库：datayes, JYDB, jydb_all, paperportfolio, ReportServer$DPPROD, ReportServer$DPPRODTempDB, wddb
#'SQL Server', '192.168.1.252', '1433', 'jydb_all', 'dpadmin', 'Dao2016pu'
server_name = '252'

db_driver[server_name] = db_types['SQLServer']
db_ip[server_name] = '192.168.1.252'
db_port[server_name] = '1433'
db_name[server_name] = 'jydb_all'
db_usr[server_name] = 'dpadmin'
db_pwd[server_name] = 'Dao2016pu'

# 253 数据库
server_name = '253'

db_driver[server_name] = db_types['SQLServer']
db_ip[server_name] = '192.168.1.253'
db_port[server_name] = '1433'
db_name[server_name] = 'jydb_all'
db_usr[server_name] = 'dpadmin'
db_pwd[server_name] = 'dpadmin'

# 62 server
# 62的数据库包括：forecast, JYDB, jydb_all, paperportfoilo, ReportServer, ReportServerTempDB, wddb
# 'SQL Server', '112.74.196.62', '1433', 'jydb_all', 'dpadmin', 'dpadmin'
server_name = '62'

db_driver[server_name] = db_types['SQLServer']
db_ip[server_name] = '112.74.196.62'
db_port[server_name] = '1433'
db_name[server_name] = 'jydb_all'
db_usr[server_name] = 'dpadmin'
db_pwd[server_name] = 'dpadmin'

###############################################################################
#sql 语句模板

#