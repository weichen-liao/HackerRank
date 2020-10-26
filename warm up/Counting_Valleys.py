# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example



The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path
Returns

int: the number of valleys traversed
Input Format

The first line contains an integer , the number of steps in the hike.
The second line contains a single string , of  characters that describe the path.

'''
def countingValleys(steps, path):
    '''
    :param steps:
    :param path:
    :return:
    '''
    # Write your code here
    altitude = 0
    valleyCount = 0
    for i,item in enumerate(path):
        if altitude == 0 and item == 'D':
            valleyCount += 1
        if item == 'D':
            altitude -= 1
        else:
            altitude += 1
    return valleyCount

if __name__ == '__main__':
    D = 'D'
    U = 'U'
    path = [D,D,U,U,U,U,D,D]
    ans = countingValleys(len(path) ,path)
    print(ans)


