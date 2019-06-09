"""
Sum of pairwise Hamming Distance
================================

Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8

Solution
--------

First thing to notice: if both integers a, b are 32-bit unsigned integers, then
hamming_distance(a, b) = hamming distance for the first bits of a and b plus
                         hamming distance for the second bits of a and b plus
                         ...
                         hamming distance for the 32th bits of a and b.
So hamming distance for a, b can be represented as 32 addendums.

Now lets suppose that array contains only 1s and 0s.
hamming_distance(a[i], a[j]) = 0 if a[i] and a[j] are the same
                               1 if a[i] and a[j] differ.
So pairwise sum of Hamming distances = number of pairs i,j such that a[i]!=a[j]
If count if 1s in array = c and number of 0s = n-c
then sum of pairwise Hamming distances = 2*c*(n-c) because differing pairs can be composed
from either (1, 0) or (0, 1).

For array of non-negative integers we can get the sum of pairwise Hamming distances
by adding 32 sums of pairwise Hamming distances for every bit.

Complexity O(N) time, O(1) space.
"""

from __future__ import print_function


def hamming(arr):
    num_bits = 32
    count = [0] * num_bits

    for el in arr:
        for i in range(num_bits):
            if el & (1<<i):
                count[i] += 1

    result = 0
    n = len(arr)
    for c in count:
        result += 2*c*(n-c) % 1000000007

    return result


print(hamming([2, 4, 6]))
