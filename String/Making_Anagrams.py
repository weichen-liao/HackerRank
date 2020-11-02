# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

'''
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.

Function Description

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):

a: a string
b: a string
Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc
Sample Output

4
Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line.


'''

def makeAnagram(a, b):
    dict_a = {}
    dict_b = {}
    res = 0
    for c in a:
        try:
            dict_a[c] += 1
        except:
            dict_a[c] = 1
    for c in b:
        try:
            dict_b[c] += 1
        except:
            dict_b[c] = 1
    keys_a = dict_a.keys()
    keys_b = dict_b.keys()
    print(dict_a)
    print(dict_b)
    for item in keys_a:
        if item not in keys_b:
            res += dict_a[item]
        elif dict_a[item] != dict_b[item]:
            res += abs(dict_a[item]-dict_b[item])
            dict_a[item] = min(dict_a[item], dict_b[item])
    for item in keys_b:
        if item not in keys_a:
            res += dict_b[item]
        # elif dict_a[item] != dict_b[item]:
        #     res += abs(dict_a[item]-dict_b[item])
        #     dict_a[item] = min(dict_a[item], dict_b[item])
    print(res)
    return res


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    makeAnagram(a, b)