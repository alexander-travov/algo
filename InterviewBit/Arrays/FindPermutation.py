"""
Find Permutation
================

Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :

Input 1:

n = 3

s = ID

Return: [1, 3, 2]


Solution
--------

First thing to notice: there exist n! permutations of n numbers and only 2^(n-1) strings that consist of 'D's and 'I's on length n-1.
So for n>2 the amount of permutations is greater and for certain strings several permutations would satisfy:

n=3
123 II
132 ID
213 DI
231 ID
312 DI
321 DD
"""

from __future__ import print_function


def find_permutation(s):
    n = len(s) + 1
    big = n
    small = 1
    permutation = []

    for i in range(n):
        # Get the last element twice
        i = min(i, len(s)-1)
        c = s[i]
        if c == 'D':
            permutation.append(big)
            big -= 1
        else:
            permutation.append(small)
            small += 1

    return permutation


s = 'IDIDIDID'
print(s, find_permutation(s))
