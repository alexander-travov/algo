#-*- coding: utf8 -*-
"""
Prime Sum
=========

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.
"""

from __future__ import print_function


def goldbach(n):
    # Create Eratosphene's sieve up to n.
    sieve = [True] * (n+1)
    for i in range(2, n+1):
        if not sieve[i]:
            continue
        k = 2
        while i*k <= n:
            sieve[i*k] = False
            k += 1

    # find primes for given sum
    for i in range(2, n+1):
        if sieve[i] and sieve[n-i]:
            return i, n-i


print(goldbach(100))
