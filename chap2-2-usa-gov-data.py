# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 01:56:40 2016

@author: yutaka
"""

from pandas import DataFrame as df, Series
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

path = '../pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, encoding='utf-8')]
frame = df(records)

#tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'

tz_counts = clean_tz.value_counts()


def show_chart(data, num=10):
    y_pos = np.arange(len(data[:num]))
    x_pos = data[:num].values
    index = data[:num].keys()
    plt.barh(y_pos, x_pos, align='center')
    plt.yticks(y_pos, index)
    plt.show()
    


    