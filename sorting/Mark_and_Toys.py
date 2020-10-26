# -*- coding: utf-8 -*-
# Author: Weichen Liao

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    sum = 0
    i = 0
    while i <= len(prices)-1:
        sum += prices[i]
        if sum <= k:
            i += 1
            continue
        else:
            break
    return i

if __name__ == '__main__':
    prices=[1,2,3,4]
    k = 7
    res = maximumToys(prices, k)
    print(res)
