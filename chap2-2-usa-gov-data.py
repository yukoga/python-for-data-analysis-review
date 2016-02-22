# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 01:56:40 2016

@author: yutaka
"""

from pandas import DataFrame as df, Series as se
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

path = './usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, encoding='utf-8')]
frame = df(records)

#tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'

tz_counts = clean_tz.value_counts()

user_agents = se([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]

count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)

def show_chart(data, num=10):
    y_pos = np.arange(len(data[:num]))
    x_pos = data[:num].values
    index = data[:num].keys()
    plt.barh(y_pos, x_pos, align='center')
    plt.yticks(y_pos, index)
    plt.show()
    


    