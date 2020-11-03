# -*- coding: utf-8 -*-
# Author: Weichen Liao

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

For example, if , it is a valid string because frequencies are . So is  because we can remove one  and have  of each character in the remaining string. If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of .

Function Description

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

s: a string
Input Format

A single string .

Constraints

Each character
Output Format

Print YES if string  is valid, otherwise, print NO.

Sample Input 0

aabbcd
Sample Output 0

NO
Explanation 0

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

Sample Input 1

aabbccddeefghi
Sample Output 1

NO
Explanation 1

Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove  characters with a frequency of : .
Remove  characters of frequency : .
Neither of these is an option.

Sample Input 2

abcdefghhgfedecba
Sample Output 2

YES
Explanation 2

All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.

'''



# def isValid(s):
#     invalid_count = 0
#     current_num = 1
#     dict_freq = {}
#     for char in s:
#         print(dict_freq)
#         if invalid_count == 2:
#             return 'NO'
#         try:
#             dict_freq[char] += 1
#         except:
#             dict_freq[char] = 1
#         if dict_freq[char] == current_num+1:
#             invalid_count += 1
#         elif dict_freq[char] == 3:
#             return 'No'
#     return 'YES'

# i must finish the scan first
# 2 freq:2, 1 freq:3
def isValid(s):
    dict_char = {}
    for char in s:
        try:
            dict_char[char] += 1
        except:
            dict_char[char] = 1
    print(dict_char)
    dict_freq = {}
    for freq in list(dict_char.values()):
        try:
            dict_freq[freq] += 1
        except:
            dict_freq[freq] = 1
    print(dict_freq)
    values = list(dict_freq.values())
    keys = list(dict_freq.keys())
    print(values)
    if len(values) <= 1:
        return 'YES'
    elif len(values) == 2:
        if 1 in values:
            if 1 in keys and dict_freq[1] == 1:
                return 'YES'
            elif abs(keys[0]-keys[1])==1:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
    else:
        return 'NO'


    

if __name__ == '__main__':
    s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    res = isValid(s)
    print(res)
    print(isValid('aaaabc'))


