# encoding = gbk

import pandas as pd
from pandas import DataFrame


def read_data():
    data = pd.read_csv('../data/CommodityArbPerformance.csv', index_col=0)
    data.columns = ['年收益', '胜率', '每笔收益率', '胜收益率', '胜钱', '负收益率', '负钱',
                    '交易数', '天数', '最大回撤', 'SD', 'ED', 'MPnL', '强平', 'up',
                    'up_close', 'down', 'down_close', '持有时间', '品种', '相关性', 'Beta']
    assert isinstance(data, DataFrame)
    return data
