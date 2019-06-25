"""
Colorful Number
===============

For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.

Solution
--------

1. First of all, 0 and 1 are colorful numbers
2. If N>=2, and has 0 or 1 digit it is not colorful.
3. If N has duplicate digits it is not colorful.
4. There exist several combinations of distinct digits, whose multiplication give equal product:
(6)~(2,3), (8)~(2,4), (2,6)~(3,4), (2,9)~(3,6), (3,8)~(4,6), (2,3,6)~(4,9), (3,4,6)~(8,9).
5. If all digits, consecutive duplets and triplets in N's digits have different products, then N is colorful.

Time complexity O(1), space complexity O(1) since conditions 2.-3. guarantee
that colorful N has at max 8 digits, and limit the number of iterations in the algorithm.
"""

from __future__ import print_function


def is_colorful(n):
    if n in (0, 1):
        return True

    digits = []
    products = set()

    # check digits
    while n:
        n, d = divmod(n, 10)
        if d in (0, 1) or d in products:
            return False
        digits.append(d)
        products.add(d)

    # check all duplets and triplets
    for part_len in (2, 3):
        i = 0
        for i in range(len(digits)-part_len+1):
            product = 1
            for j in range(part_len):
                product *= digits[i+j]
            if product in products:
                return False
            products.add(product)

    return True


print(is_colorful(5643987))
