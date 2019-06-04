"""
Repeat and Missing Number Array
===============================

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Solution
--------

Assuming following formulas are known:

sum_n = sum(1 + 2 + ... + n) = n*(n+1)/2 
sum_nsq = sum(1^2 + 2^2 + ... + n^2) = n*(n+1)*(2n+1)/6

If A appears twice and B is missing,
then the difference between sum(arr) and sum_n should be B-A

Repeating the same thought for array of squared elems, we get the difference between
sum(arr_sq) and sum_nsq that is equal to B*B-A*A = (B-A)*(B+A)

So we get a linear system of equations for A, B.
"""

from __future__ import print_function


def sum_n(n):
    return n*(n+1)/2


def sum_nsq(n):
    return n*(n+1)*(2*n+1)/6


def find_a_b(arr):
    n = len(arr)
    b_minus_a = sum_n(n) - sum(arr)
    b_plus_a = (sum_nsq(n) - sum(x*x for x in arr)) / b_minus_a

    b = (b_minus_a + b_plus_a)/2
    a = b_plus_a - b
    return a, b


for arr in [
        [3, 1, 2, 5, 3]
    ]:
    print(arr, find_a_b(arr))
