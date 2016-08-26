# coding=gbk
from _ast import Num
from pandas.io.tests.parser.na_values import NAvaluesTests

class DPFund(object):
    'Fund Class of Daopu Capital'
    
    
    def __init__(self, fund_name, conn):
        self.__name = fund_name
        self.__conn = conn
        
    def set_name(self, name):
        self.__name = name
    
    def set_conn(self, conn):
        self.__conn = conn
    
    def set_estb_date(self, date):
        '''
        设置基金成立日期
        '''
        self.setup_date = date
    
    def set_beginning_nav(self, nav):
        '''
        设置年初净值
        '''
        self.beginning_nav = nav
    
    def get_YTD(self):
        '''
        返回YTD收益
        '''
        return (self.nav - self.beginning_nav)/self.beginning_nav
    
    def get_yesterday_nav(self):
        '''
        获取前日净值
        '''
    
    def cal_nav(self):
        '''
        计算当日净值
        '''
        
    