"""
Matrix Median
=============

Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.

For example,

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
Note: No extra memory is allowed.

Solution
--------

1. Find the minimum and maximum value of matrix in O(N).
min = min(a[i][0])  i=0..N-1
max = max(a[i][-1]) i=0..N-1

2. For any value x and for every row we can find the number of elements that are less than x in O(log(M)) with binary search.
For all matrix that number is a sum for each row, and can be found in O(N*log(M)).

3. To find matrix median we do binary search between min and max value until the number of elements in matrix below x is N*M/2.
As max-min fits in 32 bits there would be not more that 32 iterations.
So overall time complexity O(32*N*log(M)) = O(N*log(M)), extra space O(1).

Note: Median of Array problem is analogous to this.
"""

from __future__ import print_function


def lt_count(a, x):
    """
    Returns number of elements in array that are less than x.
    """
    n = len(a)

    if a[0] >= x:
        return 0
    if a[-1] < x:
        return n

    l, r = 1, n-1
    while l <= r:
        m = l + (r-l)//2 # watch for oveflow
        if a[m] >= x:
            # Guaranteed to happen at least once, since x is within array [min; max]
            res = m
            r = m - 1
        else:
            l = m + 1
    return res


def le_count(a, x):
    """
    Returns number of elements in array that are less than or equal to x.
    """
    n = len(a)

    if a[0] > x:
        return 0
    if a[-1] <= x:
        return n

    l, r = 0, n-2
    while l <= r:
        m = l + (r-l)//2
        if a[m] <= x:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res + 1


def gt_count(a, x):
    """
    Returns number of elements in array that are greater than x.
    """
    return len(a) - le_count(a, x)


def ge_count(a, x):
    """
    Returns number of elements in array that are greater than or equal to x.
    """
    return len(a) - lt_count(a, x)


def matrix_median(m):
    low = min(a[0] for a in m)
    high = max(a[-1] for a in m)

    median_count = len(m) * len(m[0]) // 2

    while low <= high:
        mid = low + (high-low)//2
        count = sum(lt_count(a, mid) for a in m)
        print(low, high, mid, count)
        if count == median_count:
            return mid
        elif count < median_count:
            low = mid + 1
        else:
            high = mid - 1

    # Corner cases for duplicate elements
    if sum(lt_count(a, low) for a in m) <= median_count <= sum(le_count(a, low) for a in m):
        return low
    if sum(lt_count(a, high) for a in m) <= median_count <= sum(le_count(a, high) for a in m):
        return high
    raise Exception("Can't find median")


mat = [[1, 3, 5],
       [5, 6, 9],
       [5, 6, 9]]


print(matrix_median(mat))
