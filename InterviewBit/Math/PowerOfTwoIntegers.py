"""
Power Of Two Integers
=====================

Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4.
"""

from __future__ import print_function


def is_power(n, k):
    # Returns True if n = k ** p
    # False otherwise
    # Time complexity: log_k(n)
    while True:
        n, rem = divmod(n, k)
        if rem:
            return False
        if n==1:
            return True


def check(n):
    # Checks for every possible dividor if n is a power of it.
    # Time complexity: sum of log_k(n) for k in 2..sqrt(n)
    for k in range(2, int(n ** .5) + 1):
        if is_power(n, k):
            return True
    return False


print(check(72))
