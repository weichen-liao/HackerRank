# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://sites.northwestern.edu/acids/2018/11/12/solution-hackerrank-array-manipulation/

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    '''
    :param n: is the length of array zeros
    :param queries: list of queries to come: [[1,2,4], [4,7,9]]
    :return:
    '''
    arr = [0] * n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval
        

'''
def insertIntoArray(arr, pos, num, dropdup=True):
    left = arr[:pos]
    right = arr[pos:]
    left.append(num)
    left.extend(right)
    if dropdup==True:
        return sorted(list(set(left)))
    else:
        return left


def divide(arr, values, q):
    q_s, q_e, q_num = list(map(int, q.split(' ')))
    # possible position for q_s is [0,1,2,...,len(arr)]
    pos_s = 0
    while pos_s <=len(arr)-1 and q_s > arr[pos_s]:
        pos_s += 1
    arr = insertIntoArray(arr, pos_s, q_s,dropdup=True)
    values = insertIntoArray(values, pos_s, values[pos_s],dropdup=False)
    print('arr:',arr)
    print('values:', values)
    pos_e = pos_s
    while pos_e <=len(arr)-1 and q_e > arr[pos_e]:
        pos_e += 1
    arr = insertIntoArray(arr, pos_e, q_e, dropdup=True)
    values = insertIntoArray(values, pos_e, values[pos_e], dropdup=False)
    print('arr:', arr)
    print('values:', values)
    # change the values
    for i in range(pos_s+1, pos_e+1):
        values[i] += q_num
    return pos_s, pos_e, values
'''

if __name__ == '__main__':
    # res = divide([1,2,8,10], [0,4,5,7,0], '4 6 9')
    # res = divide([1, 6, 8, 10], [0, 4, 5, 7, 0], '4 9 9')
    # res = divide([1, 2, 8, 10], [0, 4, 5, 7, 0], '4 6 9')
    # print(res)

    arrayManipulation(10, [[1,2,100],[2,5,100]])


