"""
Given an unsorted integer array, find the first missing positive integer.

Example
-------

Given
[1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

Solution
--------

The idea is to put the positive elements from 1 to N, contained in array to corresponding positions:
1, if it is present in array, would go to the first position a[0]
2, if it is present in array, would go to the second position a[1].
k, if it is present in array, would go to a[k-1] and so on.

You start at the first position and swap elements to corresponding positions until you
either get 1 in the first position or get an element that is outside of [1..N] range.
Then you move to the second position.

Such swapping is done linear time, as each element in array is moved at most once
and is checked whether it needs to move at most twice.

After such reordering, search of the first missing positive is obvious and is done in O(N).
"""


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def need_swap(arr, i):
    el = arr[i]
    return 0 < el <= len(arr) and el != i+1


def reorder(arr):
    for i in range(len(arr)):
        while need_swap(arr, i):
            swap(arr, i, arr[i]-1)
    return arr


def find_missing(arr):
    for i, el in enumerate(arr):
        if el != i+1:
            return i+1
    return len(arr)+1


for arr in [
        [5, 4, 3, 2, 1],
        [1, 2, 0],
        [3, 4, -1, 1],
        [-8, -7, -6]
    ]:
    print(find_missing(reorder(arr)), arr)
