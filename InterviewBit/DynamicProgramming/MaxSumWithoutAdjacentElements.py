"""
Max Sum Without Adjacent Elements
=================================

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.

Input Format:

The first and the only argument of input contains a 2d matrix, A.
Output Format:

Return an integer, representing the maximum possible sum.
Constraints:

1 <= N <= 20000
1 <= A[i] <= 2000
Example:

Input 1:
    A = [   [1]
            [2]    ]

Output 1:
    2

Explanation 1:
    We will choose 2.

Input 2:
    A = [   [1, 2, 3, 4]
            [2, 3, 4, 5]    ]

Output 2:
    We will choose 3 and 5.
"""

from __future__ import print_function


def find_max_sum(arr):
    N = len(arr[0])
    max_arr = [max(arr[0][i], arr[1][i]) for i in range(N)]

    elems_used_sum = [max_arr[0]]
    elems_not_used_sum = [0]

    for i in range(1, N):
        elems_not_used_sum.append(max(elems_used_sum[i-1], elems_not_used_sum[i-1]))
        elems_used_sum.append(max_arr[i] + elems_not_used_sum[i-1])

    return max(elems_used_sum[-1], elems_not_used_sum[-1])


print(find_max_sum([
    [1, 2, 3, 4],
    [2, 3, 4, 5],
]))
