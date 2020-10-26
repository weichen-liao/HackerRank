# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .
'''


# Complete the repeatedString function below.
def repeatedString(s, n):
    '''
    # this one is bad because it's O(n)
    sIndex = 0
    nIndex = 0
    res = 0
    while nIndex < n:
        if s[sIndex] == 'a':
            res += 1
        if n < len(s):
            sIndex = sIndex + 1
        else:
            sIndex = (sIndex+1)%len(s)
        nIndex += 1
    return res
    '''
    # calculate how many cycles it will be and how many a within a cycle
    length = len(s)
    res = 0
    if n < length:
        for i in range(n):
            if s[i] == 'a':
                res += 1
    else:
        for i in range(length):
            if s[i] == 'a':
                res += 1
        res = res * int(n/length)
        for i in range(n%length):
            if s[i] == 'a':
                res += 1
    return res


if __name__ == '__main__':
    s = 'a'
    n = 1000000
    res = repeatedString(s, n)
    print(res)




