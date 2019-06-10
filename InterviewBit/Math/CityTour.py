"""
City Tour
=========

There are A cities numbered from 1 to A. You have already visited M cities, the indices of which are given in an array B of M integers.

If a city with index i is visited, you can visit either the city with index i-1 (i >= 2) or the city with index i+1 (i < A) if they are not already visited. 
Eg: if N = 5 and array M consists of [3, 4], then in the first level of moves, you can either visit 2 or 5.

You keep visiting cities in this fashion until all the cities are not visited. 
Find the number of ways in which you can visit all the cities modulo 10^9+7.

Input Format
------------

The 1st argument given is an integer A, i.e total number of cities.
The 2nd argument given is an integer array B, where B[i] denotes ith city you already visited.

Output Format
-------------

Return an Integer X % (1e9 + 7), number of ways in which you can visit all the cities.

Constraints
-----------

1 <= A <= 1000
1 <= M <= A
1 <= B[i] <= A

Example
-------

Input:
    A = 5
    B = [2, 5]
Output:
    6
   
Explanation
-----------

All possible ways to visit remaining cities are:
1. 1 -> 3 -> 4
2. 1 -> 4 -> 3
3. 3 -> 1 -> 4
4. 3 -> 4 -> 1
5. 4 -> 1 -> 3
6. 4 -> 3 -> 1
"""

from __future__ import print_function


M = int(1e9+7)


def mod_factorial(a, m):
    # Calculates a! mod m
    res = 1
    for i in range(2, a+1):
        res = res*i % m
    return res


def mod_pow(a, n, m):
    # Calculates fast a**n mod m in O(log(n))
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


def num_ways(n, visited, m=M):
    visited.sort()

    terminal = []
    inner = []

    # left end
    if visited[0] != 1:
        terminal.append(visited[0]-1)
    # right end
    if visited[-1] != n:
        terminal.append(n-visited[-1])


    for i in range(len(visited)-1):
        delta = visited[i+1]-visited[i]-1
        if delta:
            inner.append(delta)

    res = mod_factorial(sum(terminal) + sum(inner), m)

    for k in terminal + inner:
        res = res * mult_inverse(mod_factorial(k, m), m) % m

    for k in inner:
        res = res * mod_pow(2, k-1, m) % m

    return res


print(num_ways(5, [2, 5]))
