# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the minimumBribes function below.
def minimumBribes(q):
    move = 0
    for i, item in enumerate(q):
        if q[i] == i+1:
            continue
        elif q[i] - (i+1) > 2:
            print('Too chaotic')
            return
        else:
            q[q[i]-1] = q[i]
            move += 1
    print(move)
    return


if __name__ == '__main__':
    # q = [2,1,5,3,4]
    q = [1,2,5,3,7,8,6,4]
    minimumBribes(q)



