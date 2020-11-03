# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://www.hackerrank.com/challenges/down-to-zero-ii/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen

'''
You are given  queries. Each query consists of a single number . You can perform any of the  operations on  in each move:

1: If we take 2 integers  and  where , , then we can change

2: Decrease the value of  by .

Determine the minimum number of moves required to reduce the value of  to .

Input Format

The first line contains the integer .
The next  lines each contain an integer, .

Constraints



Output Format

Output  lines. Each line containing the minimum number of moves required to reduce the value of  to .

Sample Input

2
3
4
Sample Output

3
3
Explanation

For test case 1, We only have one option that gives the minimum number of moves.
Follow  ->  ->  -> . Hence,  moves.

For the case 2, we can either go  ->  ->  ->  ->  or  ->  ->  -> . The 2nd option is more optimal. Hence,  moves.

'''


def downToZero(n):
    print('current n:', n)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    i = 2
    candicates = []
    while i <= n/2+1:
        print('  current i:', i)
        if n % i != 0:
            i += 1
        else:
            candicates.append(max(i, int(n/i)))
            i += 1
    if len(candicates) > 0:
        return downToZero(min(candicates)) + 1
    return downToZero(n-1) + 1


if __name__ == '__main__':
    print(downToZero(86))





