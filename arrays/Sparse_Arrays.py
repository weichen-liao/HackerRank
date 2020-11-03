# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://www.hackerrank.com/challenges/sparse-arrays/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def matchingStrings(strings, queries):
    dict_freq = {}
    res = []
    for s in strings:
        try:
            dict_freq[s] += 1
        except:
            dict_freq[s] = 1
    for q in queries:
        try:
            res.append(dict_freq[q])
        except:
            res.append(0)
    return res



