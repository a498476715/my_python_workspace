# coding=gbk
from datetime import date
from datetime import datetime
from datetime import timedelta

import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np


def load_csv_data(filename, columns=None, columns_new=None, index_column=None, index_new=None):
    """
    columns: 想要读取的columns,不设置会读取全部columns
    columns_new: 给columns改名
    """
    data = pd.read_csv(filename, usecols=columns, index_col=index_column)
    if columns_new is not None:
        data.columns = columns_new
    if index_new is not None:
        data.index.name = index_new
    return data


def load_two_legs(leg1, leg2):
    data_leg1 = load_csv_data('../data/%sMinQuote.csv' % leg1, columns=['TDATETIME', 'LASTPX', 'CHGPCTMIN'],
                              index_column='TDATETIME', columns_new=['最新成交价', '分钟收益%'], index_new='时间')
    data_leg2 = load_csv_data('../data/%sMinQuote.csv' % leg2, columns=['TDATETIME', 'LASTPX', 'CHGPCTMIN'],
                              index_column='TDATETIME', columns_new=['最新成交价', '分钟收益%'],
                              index_new='时间')
    data = data_leg1.merge(data_leg2, left_index=True, right_index=True, suffixes=[leg1, leg2])
    return data


def cal_sig(leg1_p, leg2_p, window, method="diff"):
    sig = Series()
    if method == "diff":
        sig = leg2_p - leg1_p
    elif method == "ratio":
        sig = leg2_p / leg1_p
    else:
        print("sig_method can only be 'diff' or 'ratio'")
        exit(1)
    return sig


def cal_mean(leg1_p, leg2_p, window, method="diff"):
    spread = Series()

    return cal_ma(spread, window)


def cal_ma(data, window):
    """
    :rtype: pandas.Series
    """
    return data.rolling(window=window).mean()


def cal_std(data, window) -> Series:
    """
    :rtype: pandas.Series
    """
    return data.rolling(window=window).std()


def delete_na(data):
    """
    删除NAN值
    """
    data = data.dropna(axis=0)
    return data


def high_freq_arbitrage(leg1, leg2, back_time, sig, sig_method, leg1_sig, leg2_sig, up_std, down_std):
    data = load_two_legs(leg1, leg2)
    data['sig'] = cal_sig(data[leg1_sig], data[leg2_sig], window=back_time, method=sig_method)
    data['mean'] = cal_ma(data['sig'], window=back_time)
    data['sig_sd'] = cal_std(data['sig'], back_time)
    data['up'] = data['mean'] + up_std * data['sig_sd']
    data['down'] = data['mean'] - down_std * data['sig_sd']
    # data['order'] =
    data = delete_na(data)
    return data


def order_sig(up, down, sig):
    up_pre = up.shift(1)
    down_pre = down.shift(1)
    if up <= sig < up_pre: #long leg1
        return 1
    elif mean <= sig < up:
        return


def generate_trans(up, mean, down, sig, vol1, vol2):
    shift = False
    transaction_1 = Series(0, index=up.index)
    pre_sig_1 = sig.shift(1)
    transaction_1 = np.where()


def main():
    # 配置数据
    leg1 = 'P'
    leg2 = 'OI'
    # 数据所在的路径： '../data/%sMinQuote.csv' % leg1
    back_time = 20
    # sig = '分钟收益%'
    sig = '最新成交价'
    sig_method = "diff"
    # sig_method = "ratio"
    leg1_sig = sig + leg1
    leg2_sig = sig + leg2
    up_std = 1
    down_std = 1

    ret = high_freq_arbitrage(leg1, leg2, back_time, sig, sig_method, leg1_sig, leg2_sig, up_std, down_std)

    print(ret.head(n=5))


if __name__ == '__main__':
    main()
