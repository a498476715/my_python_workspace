# coding=gbk

#############################################################################
# ���� ���Ӳ�Ʒ����
product_std_names = ['��������1��','��������2��','������Ӫ','�Գ�1��','��ѡ1��']
product_sql_names = ['����01','����02', '�Գ�', '��ѡ', '��Ӫ']

#############################################################################
# �������ݿ�, ����db��ͷ
db_types = {'SQLServer': 'SQL Server'}

db_driver = {}
db_ip = {}
db_port = {}
db_name = {} # Ҫʹ�õ����ݿ�����֣�ÿ��server������Ĭ�����ݿ�
db_usr = {}
db_pwd = {}


# 252 ������
# 252���������ݿ⣺datayes, JYDB, jydb_all, paperportfolio, ReportServer$DPPROD, ReportServer$DPPRODTempDB, wddb
#'SQL Server', '192.168.1.252', '1433', 'jydb_all', 'dpadmin', 'Dao2016pu'
server_name = '252'

db_driver[server_name] = db_types['SQLServer']
db_ip[server_name] = '192.168.1.252'
db_port[server_name] = '1433'
db_name[server_name] = 'jydb_all'
db_usr[server_name] = 'dpadmin'
db_pwd[server_name] = 'Dao2016pu'

# 253 ���ݿ�
server_name = '253'

db_driver[server_name] = db_types['SQLServer']
db_ip[server_name] = '192.168.1.253'
db_port[server_name] = '1433'
db_name[server_name] = 'jydb_all'
db_usr[server_name] = 'dpadmin'
db_pwd[server_name] = 'dpadmin'

# 62 server
# 62�����ݿ������forecast, JYDB, jydb_all, paperportfoilo, ReportServer, ReportServerTempDB, wddb
# 'SQL Server', '112.74.196.62', '1433', 'jydb_all', 'dpadmin', 'dpadmin'
server_name = '62'

db_driver[server_name] = db_types['SQLServer']
db_ip[server_name] = '112.74.196.62'
db_port[server_name] = '1433'
db_name[server_name] = 'jydb_all'
db_usr[server_name] = 'dpadmin'
db_pwd[server_name] = 'dpadmin'

###############################################################################
#sql ���ģ��

#