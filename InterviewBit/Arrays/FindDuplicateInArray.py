"""
Find Duplicate in Array
=======================
Given a read only array of n + 1 integers between 1 and n,
find one number that repeats in linear time using less than O(n) space
and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1

Solution
--------

0. Since we have n+1 integers between 1 and n there always exist a duplicate.

1. If we could change array values, we could use the following trick.
Since elements are from 1 to n, we can use that value as an index in the same array.
We can use sign bit of element of corresponding index to signal, if we already looked at that position.

for el in arr:
    ind = abs(el)
    if arr[ind] < 0:
        return el
    arr[ind] = -abs(arr[ind])

But that solution does not meet the constraint that array is read only.

2. We can interpret that array as a linked list, where the next element for el is defined as:
next = arr[el] so the element is used as an index to the next element.

In such interpretation every duplicate creates a loop. F.e. for array [3, 4, 1, 4, 1] we get the sequence:
3 -> 4 -> 1 -> 4 -> 1 ...

We can use Floyd's Tortoise and Hare algorithm for finding the entry point of the loop, which is the duplicate.
"""

from __future__ import print_function


def get_duplicate1(arr):
    for el in arr:
        ind = abs(el)
        if arr[ind] < 0:
            return ind
        arr[ind] = -abs(arr[ind])


def get_duplicate2(arr):
    slow = arr[0]
    fast = arr[slow]

    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    slow = 0

    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


arr = [5, 1, 4, 3, 1, 2]
print(get_duplicate2(arr))
