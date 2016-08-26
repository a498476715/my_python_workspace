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
    证券class，是所有证券类型的parent类
    子类包括：Stock
    '''
    
class Stock(Security):
    '''
    股票class，继承了Security类
    '''

class Derivatives(WindProduct):
    '''
    衍生品class，继承了WindProduct
    子类包括：Furture, 
    '''

class Future(Security):
    '''
    期货类，继承了Security类
    子类包括：
    '''

class IndexFuture(Future):
    '''
    股指期货，继承了Future类
    '''

class Index(WindProduct):
    '''
    指数类，继承了WindProduct
    子类包括：Sector（板块类），Industry（行业类）
    '''

class Sector(Index):
    '''
    板块类，继承了Index类。板块由行业组成
    '''
    
class Industry(Index):
    'Class for Industry. Child class of Index class.'
#      def query_weight(self, date):
#          'return weight of constituent '


w.start(waitTime=120, showmenu=False)