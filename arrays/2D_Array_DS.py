# -*- coding: utf-8 -*-
# Author: Weichen Liao

def hourglassSum(arr):
    '''
    :param arr:The array will always be 6x6.
    :return: maximun of the hourglass sum in this matrix
    '''
    hourglass_sum = []
    for i in range(4):
        for j in range(4):
            hourglass_sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    return max(hourglass_sum)







