# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints

 where
Output Format

Return the total number of matching pairs of socks that Alex can sell.

'''


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    res = 0
    dict_socks = {}
    for i,item in enumerate(ar):
        try:
            dict_socks[item] += 1
        except:
            dict_socks[item] = 1
        if dict_socks[item] == 2:
            res += 1
            dict_socks[item] = 0
    return res



if __name__ == '__main__':
    # n = 7
    n=9
    # ar = [1, 2, 1, 2, 1, 3, 2]
    ar = [1, 2, 2, 1, 1, 3, 5, 1, 2]
    res = sockMerchant(n, ar)
    print(res)

