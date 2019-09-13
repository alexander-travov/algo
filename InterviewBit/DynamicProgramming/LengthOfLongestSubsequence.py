"""
Length of Longest Subsequence
=============================

Given an array of integers, A of length N, find the length of longest subsequence which is first increasing then decreasing.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the answer as described in the problem statement.
Constraints:

1 <= N <= 3000
1 <= A[i] <= 1e7
Example:

Input 1:
    A = [1, 2, 1]

Output 1:
    3

Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]

Output 2:
    6

Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
"""

from __future__ import print_function


def find_inc_subseq_lens(arr):
    lens = [(1, el) for el in arr]

    for i in range(1, len(arr)):
        el = arr[i]
        cur_len, cur_last = lens[i]
        for j in range(i):
            prev_len, prev_last = lens[j]
            if prev_last <= el and cur_len <= prev_len:
                cur_len = prev_len + 1
                cur_last = el
            elif prev_last > el and cur_len < prev_len:
                cur_len = prev_len
                cur_last = prev_last
        lens[i] = (cur_len, cur_last)

    return lens


def find_subseq_len(arr):
    inc_lens = find_inc_subseq_lens(arr)
    dec_lens = find_inc_subseq_lens(list(reversed(arr)))
    dec_lens.reverse()
    print(inc_lens)
    print(dec_lens)

    max_len = -1
    for i in range(len(arr)):
        inc_len, inc_last = inc_lens[i]
        dec_len, dec_last = dec_lens[i]
        cur_len = inc_len + dec_len
        if inc_last == arr[i] and dec_last == arr[i]:
            cur_len -= 1
        print(i, cur_len)
        max_len = max(max_len, cur_len)

    return max_len


print(find_subseq_len([1, 11, 2, 10, 4, 5, 2, 1]))
