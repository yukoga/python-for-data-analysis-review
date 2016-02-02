# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
from collections import defaultdict
from collections import Counter

path = '../pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, encoding='utf-8')]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts
    
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    
def use_counter(sequence, n=10):
    return Counter(sequence).most_common(n)

