# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
    '''
    left rotation on array [1,2,3,4,5]
    :param a: size of d
    :param d: numbers of steps
    :return:
    '''
    d = d % len(a)
    a.extend(a[:d])
    a = a[d:]
    # for i in range(d):
    #     a.append(a[0])
    #     a = a[1:]
    return a

if __name__ == '__main__':
    a = [1,2,3,4,5]
    d = 7
    res = rotLeft(a,d)
    print(res)




