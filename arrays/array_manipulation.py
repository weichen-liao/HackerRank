# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://sites.northwestern.edu/acids/2018/11/12/solution-hackerrank-array-manipulation/

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    '''
    :param n: is the length of array zeros
    :param queries:
    :return:
    '''
    dictionary = {}
    # {'1-2':100}
    # {'1':100, '2':200, '3-5':100, }
    for q in queries:
        start, end, num = q.split(' ')
        for k in dictionary.keys():
            if not k:
                continue
            # see if there are intersection
            if '-' in k:
                k_start, k_end = k.split('-')
                # no intersection
                if int(end) < int(k_start) or int(start) > int(k_end):
                    new_key = '-'.join([start, end]) if start!=end else start
                    dictionary[new_key] = int(num)
                # has intersection
                else:
                    # completely cover
                    if int(start) >= int(k_start) and int(end) <= int(k_end):


                    if int(end) >= int(start) and int(start)<=int(start):


