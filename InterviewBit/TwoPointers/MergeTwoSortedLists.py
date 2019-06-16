"""
Merge Two Sorted Lists II
=========================

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You have to modify the array A to contain the merge of A and B.
Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result. 
If the number of elements initialized in A and B are m and n respectively,
the resulting size of array A after your code is executed should be m + n

Example :

Input : 
A : [1 5 8]
B : [6 9]

Modified A : [1 5 6 8 9]
"""

from __future__ import print_function


def merge(a, b):
    m = len(a)
    n = len(b)

    res = []
    i = j = 0
    while i<m and j<n:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:m])
    res.extend(b[j:n])
    return res


print(merge([1, 5, 8], [6, 9]))
