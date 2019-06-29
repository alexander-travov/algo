"""
N max pair combinations
=======================

Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+6),
9    (4+5),
8    (2+6)

Solution
--------

1. Sort both arrays
2. Init Max Heap with (k,v) = (A[N-1]+B[N-1], (N-1, N-1))
3. Store N indices:

4. Extract Max. Its indexes are (i,j). Add to Max Heap sums of
   (i-1,j), (i,j-1) if they are not there already. You can use set for that.

5. Repeat 4. any number or times.

Time complexity O(Nlog(N)), space complexity O(N)
"""

from __future__ import print_function
from heap import MinHeap


def get_max_pairs(A, B, M=None):
    N = len(A)
    if not M:
        M = N
    A.sort()
    B.sort()

    h = MinHeap()
    used_pairs = set()

    val = (N-1, N-1)
    key = -A[val[0]]-B[val[1]]
    h.insert(key, val)
    used_pairs.add(val)

    for _ in range(M):
        key, (i, j) = h.extract_min()
        yield -key
        for pair in ((i-1, j), (i, j-1)):
            if pair[0]<0 or pair[1]<0 or pair in used_pairs:
                continue
            key = -A[pair[0]]-B[pair[1]]
            h.insert(key, pair)
            used_pairs.add(pair)


A = [1, 4, 2, 7, 3]
B = [2, 5, 1, 4, 6]
for s in get_max_pairs(A, B, 25):
    print(s)
