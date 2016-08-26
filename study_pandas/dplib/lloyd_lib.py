import pandas as pd
import pypyodbc
from datetime import date
from datetime import timedelta
import xlsxwriter

def connect_to_database(driver, ip, port, db_name, user_ID, password):
    connect_str = ('DRIVER={%s};'
                     'SERVER=%s,%s;'
                     'UID=%s;'
                     'PWD=%s;'
                     %(driver, ip, port, user_ID, password))
    #print(connect_str)
    try:
        conn = pypyodbc.connect(connect_str)
        return conn
    except Exception as e:
        print(e)

