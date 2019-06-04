"""
Add One To Number
=================

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
"""

from __future__ import print_function


def add_one(v):
    carry = True
    for i in range(len(v)-1, -1, -1):
        if not carry:
            break
        carry = v[i] == 9
        v[i] = (v[i] + 1) % 10
    if i == 0 and carry:
        v.insert(0, 1)
    return v


for v in [
        [1, 2, 3],
        [9, 9, 9, 9, 9, 9]
    ]:
    print(v)
    print(add_one(v))
