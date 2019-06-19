"""
Nearest Smaller Element
=======================

Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

Input : A : [4, 5, 2, 10, 8]
Return : [-1, 4, -1, 2, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]


Solution
--------

The problem can be solved with stack.
When we traverse next element, we peak to the stack and pop while there isn't a smaller element.
If the stack is not empty, we return its head, else return -1.
Then we push new element on the stack.

Time complexity O(N), space complexity O(N). In the worst case we end up with increasing sequence
for which all elements would be saved on the stack.
"""

from __future__ import print_function


def nearest_element(arr):
    st = []
    for el in arr:
        while st and st[-1] >= el:
            st.pop()
        yield st[-1] if st else -1
        st.append(el)


for arr in (
    [4, 5, 2, 10, 8],
    [3, 2, 1]
):
    print(arr, list(nearest_element(arr)))
