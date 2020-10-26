# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

'''


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    curPos = 0
    while curPos < len(c)-1:
        nextPos = curPos + 1
        nextNextPos = nextPos + 1
        if nextPos >= len(c)-1 or nextNextPos >= len(c)-1:
            jump += 1
            break

        if c[nextPos] == 1:
            jump += 1
            curPos += 2
        else:
            if c[nextNextPos] == 1:
                jump += 1
                curPos += 1
            else:
                jump += 1
                curPos += 2
    return jump


if __name__ == '__main__':
    c = [0,1,0,0,0,1,0]
    c = [0,0,1,0,0,1,0]
    c = [0,0,0,0,1,0]
    ans = jumpingOnClouds(c)
    print(ans)


