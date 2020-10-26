# -*- coding: utf-8 -*-
# Author: Weichen Liao

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    def swap(array, i1, i2):
        temp = array[i1]
        arr[i1] = array[i2]
        arr[i2] = temp
        return array

    i = 0
    move = 0
    while i <= len(arr)-1:
        if arr[i] != i+1:
            arr = swap(arr, i, arr[i]-1)
            move += 1
        else:
            i += 1
    return move


if __name__ == '__main__':
    # arr = [7,1,3,2,4,5,6]
    arr = [2,3,4,1,5]
    res = minimumSwaps(arr)
    print(res)


