"""
Sorted Permutation Rank With Repeats
====================================

Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Characters can be repeated. If the characters are repeated, we need to look at the rank in unique permutations.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba

Input : 'aba'
Output : 2

The order permutations with letters 'a', 'a', and 'b' :
aab
aba
baa

The answer might not fit in an integer, so return your answer % 1000003
"""

from __future__ import print_function


def letter_ind(c):
    # Latin letter index (zero-based):
    # a-0, b-1, ... z-25
    return ord(c) - ord('a')


def mod_pow(a, n, m):
    # Calculates fast exponent a**n mod m in O(log(n))
    res = 1
    exp = a
    while n:
        if n & 1:
            res = res*exp % m
        exp = exp*exp % m
        n >>= 1
    return res


def mult_inverse(a, m):
    # Finds multiplicative inverse b of a in modular arithmetic.
    # a*b mod m = 1
    # b = a**(phi(m)-1) = a**(m-2) for prime m, where phi(m) - Euler's totient function
    # Time complexity O(log(m))
    return mod_pow(a, m-2, m)


def permutation_rank(s, m=1000003):
    # Assuming we are dealing with latin alphabet.
    count = [0] * 26

    for l in s:
        count[letter_ind(l)] += 1

    # how many letters in str are less that current letter
    def letter_order(l):
        i = letter_ind(l)
        return sum(count[:i])

    def remove_letter(l):
        count[letter_ind(l)] -= 1

    # Array of multiplicative inverse mod m for numbers from 0 to max(count)
    inv = [mult_inverse(i, m) for i in range(max(count)+1)]

    # Calculates array of (n! mod m) without overflow.
    fact = [1, 1]
    for i in range(2, len(s)):
        fact.append(fact[i-1] * i % m)

    rank = 0
    n = len(s)
    for l in s[:-1]:
        o = letter_order(l)
        rc = count[letter_ind(l)] # letter's repeat count
        rank = (rank + o*fact[n-1]) * inv[rc] % m
        remove_letter(l)
        n -= 1

    return rank+1


print(permutation_rank('cabacc'))
