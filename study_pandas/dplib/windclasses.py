# coding=gbk

from WindPy import w 

class WindProduct(object):
    'Base class of stock and industry'
    #__name_string = ''
    def __init__(self, wind_code):
        self.__wind_code = wind_code
    def set_wind_code(self, wind_code):
        self.__wind_code
    def get_wind_code(self):
        return self.__wind_code
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

class Security(WindProduct):
    '''
    ֤ȯclass��������֤ȯ���͵�parent��
    ���������Stock
    '''
    
class Stock(Security):
    '''
    ��Ʊclass���̳���Security��
    '''

class Derivatives(WindProduct):
    '''
    ����Ʒclass���̳���WindProduct
    ���������Furture, 
    '''

class Future(Security):
    '''
    �ڻ��࣬�̳���Security��
    ���������
    '''

class IndexFuture(Future):
    '''
    ��ָ�ڻ����̳���Future��
    '''

class Index(WindProduct):
    '''
    ָ���࣬�̳���WindProduct
    ���������Sector������ࣩ��Industry����ҵ�ࣩ
    '''

class Sector(Index):
    '''
    ����࣬�̳���Index�ࡣ�������ҵ���
    '''
    
class Industry(Index):
    'Class for Industry. Child class of Index class.'
#      def query_weight(self, date):
#          'return weight of constituent '


w.start(waitTime=120, showmenu=False)