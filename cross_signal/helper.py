# coding=gbk

from datetime import date
from datetime import timedelta
import pandas as pd
from pandas import Series
from pandas import DataFrame
import pypyodbc
import xlsxwriter
import matplotlib.pyplot as plt

from WindPy import w

def connect_to_database(driver, ip, port, db_name, user_ID, password):
    '''
    ���ӵ�ָ�����ݿ�
    '''
    if db_name:
        connect_str = ('DRIVER={%s};'
                     'SERVER=%s,%s;'
                     'DATABASE=%s;'
                     'UID=%s;'
                     'PWD=%s;'
                     %(driver, ip, port, db_name,user_ID, password))
    else:
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

def checkIfWindConnected():
    '''
    ���wind�ӿ��Ƿ����ӳɹ�
    '''
    return w.isconnected()

def connectWind():
    '''
    ����wind�ӿ�
    '''
    if not checkIfWindConnected():
        w.start(showmenu = False)
    
def closeWind():
    '''
    �ر�wind�ӿ�
    '''
    w.stop()
    
def ma_simple(data, window, column_name = 'MA'):
    '''
    �������ƶ�ƽ��
    '''
#     data[column_name] = data['close'].rolling(window = window).mean()
#     return data
    return data.rolling(window = window).mean()

def delete_na(data):
    '''
    ɾ��NANֵ
    '''
    data = data.dropna(axis=0)
    return data

def cross_point(data, short_term, long_term):
    '''
    �����������н�������, short_term ������
    ''' 
    previous_short = data[short_term].shift(1)
    previous_long = data[long_term].shift(1)
    crossing = (((data[short_term] <= data[long_term]) & (previous_short >= previous_long))
                | ((data[short_term] >= data[long_term]) & (previous_short <= previous_long)))
    
    crossing_dates = data.loc[crossing]
    return crossing_dates
