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


class MinHeap(list):
    def _swap(self, i, j):
        tmp = self[i]
        self[i] = self[j]
        self[j] = tmp

    def _sift_up(self, ind):
        if ind == 0:
            return
        parent = (ind-1) // 2
        if self[ind][0] < self[parent][0]:
            self._swap(ind, parent)
            self._sift_up(parent)

    def _sift_down(self, ind):
        left_ch = 2*ind + 1
        right_ch = 2*ind + 2
        if left_ch >= len(self):
            return
        min_ch = left_ch
        if right_ch < len(self) and self[right_ch][0] < self[left_ch][0]:
            min_ch = right_ch
        if self[ind] > self[min_ch]:
            self._swap(ind, min_ch)
            self._sift_down(min_ch)

    def insert(self, key, value):
        self.append((key, value))
        self._sift_up(len(self)-1)

    def get_min(self):
        if not self:
            return
        return self[0]

    def extract_min(self):
        if not self:
            return
        min_kv = self[0]
        last_kv = self.pop()
        if self:
            self[0] = last_kv
            self._sift_down(0)
        return min_kv


def get_max_pairs(A, B):
    N = len(A)
    A.sort()
    B.sort()

    h = MinHeap()
    used_pairs = set()

    h.insert(-A[N-1]-B[N-1], (N-1, N-1))
    for _ in range(N):
        k, (i, j) = h.extract_min()
        used_pairs.add((i, j))
        yield -k
        for pair in ((i-1, j), (i, j-1)):
            if pair in used_pairs:
                continue
            h.insert(-A[pair[0]]-B[pair[1]], pair)


A = [1, 4, 2, 7, 3]
B = [2, 5, 1, 4, 6]
for s in get_max_pairs(A, B):
    print(s)
