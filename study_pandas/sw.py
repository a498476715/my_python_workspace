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
name_dict['S_INFO_WINDCODE'] = 'Wind代码'
name_dict['trade_dt'] = '日期'
name_dict['con_num'] = '成分股数量'
name_dict['pe_lyr'] = '市盈率(PE,LYR)'
name_dict['pe_ttm'] = '市盈率(PE,TTM)'
name_dict['pb_lf'] = '市净率(PB,LF)'
name_dict['pcf_lyr'] = '市现率(PCF,LYR)'
name_dict['pcf_ttm'] = '市现率(PCF,TTM)'
name_dict['ps_lyr'] = '市销率(PS,LYR)'
name_dict['ps_ttm'] = '市销率(PS,TTM)'
name_dict['MV_TOTAL'] = '当日总市值合计（元）'
name_dict['MV_FLOAT'] = '当日流通市值合计（元）'
name_dict['dividend_yield'] = '股息率'
name_dict['TOT_SHR_FLOAT'] = '流通股本合计（股）'
name_dict['TOT_SHR_FREE'] = '自由流通股本合计（股）'
name_dict['turnover'] = '换手率'
name_dict['turnover_free'] = '换手率(自由流通)'
# name_dict[''] = ''

def get_his_data(sec_windcode):
    sql = 

if __name__ == "__main__":
    w.start(showmenu=False)
    # 申万一级28个行业代码，名字
    sw_sec = df(w.wset("SectorConstituent", "date=20160805;sectorId=a39901011g000000").Data[1:3], index=['代码', '板块名称'])
    sw_sec = sw_sec.T
    sw_sec.index += 1
    sw_sec.index.name = '序号'
#     for key in sw
    print(sw_sec)
#     print(w.wset("SectorConstituent","date=20160805;sectorId=a39901011g000000").Data[1])
    
    
