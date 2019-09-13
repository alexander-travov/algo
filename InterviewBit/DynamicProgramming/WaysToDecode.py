"""
Ways To Decode
==============

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

from __future__ import print_function


def ways_to_decode(n):
    prev = 1
    curr = 1
    digits = [int(d) for d in str(n)]
    i = 1
    while i < len(digits):
        curr_digit = digits[i]
        prev_digit = digits[i-1]

        # 10, 20
        if curr_digit == 0:
            if prev_digit not in (1, 2):
                return 0
            curr, prev = prev, prev
        # 11-19, 21-26
        elif prev_digit == 1 or (curr_digit <= 6 and prev_digit == 2):
            curr, prev = curr+prev, curr
        else:
            curr, prev = curr, curr
        i += 1
    return curr


print(ways_to_decode(121411029))
