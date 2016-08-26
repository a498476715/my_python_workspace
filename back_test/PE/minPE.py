import datetime
from pandas import Series
from pandas import DataFrame
import pandas as pd

from WindPy import w

index_code = "399006.SZ"
benchmark_code = index_code

w.start(showmenu=False)

wsd_data = w.wsd(index_code, "close, pct_chg", "2011-01-01", "2016-08-23", "")
dates = wsd_data.Times
index_df = DataFrame(wsd_data.Data,index=wsd_data.Fields,columns=wsd_data.Times).T
index_df['nav'] = (index_df['PCT_CHG']/100 + 1).cumprod()

pe_df = DataFrame()
for date in dates:
    date = datetime.datetime.strftime(date, '%Y-%m-%d')
    cons_code = w.wset("sectorconstituent", "date=%s;windcode=%s"%(date,index_code)).Data[1]
    code_str = ','.join(cons_code)
    wsd_data = w.wsd(code_str, 'pe_ttm', date, date, "")
    print(wsd_data)
    pe_df[date] = (DataFrame(wsd_data.Data, index=[date],columns=wsd_data.Codes).T).loc[:, date]
print(pe_df)
