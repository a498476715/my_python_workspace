# coding=gbk

import datetime
import pandas as pd
from pandas import Series
from pandas import DataFrame

import lloyd_lib
import classes

conn = lloyd_lib.connect_to_database('SQL Server', '192.168.1.252', '1433', 'jydb_all', 'dpadmin', 'Dao2016pu')
# myProduct = product.Stock('000300.SH')
# print(myProduct.get_wind_code())
# myStock = product.Stock('000300.SH')
# print(myStock.get_wind_code())
#ret = w.wset("IndexConstituent","date=20160804;windcode=000300.SH").Data
string1 = "SectorConstituent"
string2 = "date=20160805;sectorid=a001010100000000"
ret = classes.w.wset(string1, string2)
#data = DataFrame(ret.Data, )
print(ret)
#print(w.wset(string1, string2))
#print(ret)
# data = DataFrame(ret).T
# print(data[0])
# #print(data)
#print(w.wset("SectorConstituent","date=20160805;sectorId=a001010100000000"))
#w.WindData
