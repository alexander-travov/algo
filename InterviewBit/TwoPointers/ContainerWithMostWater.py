"""
Container With Most Water
=========================

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

 Note: You may not slant the container. 
Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6


Solution
--------

Problem can be solved in linear time with two pointers: left l and right r bar of container.

For l and r amount of water in container is:
V(l, r) = H*L = min(a[l], a[r]) * (r-l)

If a[l] >= a[r] then we can deduce that:
    V(l+1, r) < V(l, r),
    V(l+2, r) < V(l, r),
    ...
    V(r-2, r) < V(l, r),
    V(r-1, r) < V(l, r)
as for each of those containers height is less or equal and length is less that for (l, r).
So the only way to increase amount of water is to move right bar to the left.

Symmetrically, if a[l] < a[r], then
    V(l, r-1) < V(l, r),
    V(l, r-2) < V(l, r),
    ...
    V(l, l+2) < V(l, r),
    V(l, l+1) < V(l, r)
So the only way to increase amount of water is to move left bar to the right.

Time complexity O(N), space complexity O(1).
"""

from __future__ import print_function


def most_water(a):
    l = 0
    r = len(a)-1
    max_water = 0

    while l < r:
        water = min(a[l], a[r]) * (r-l)
        max_water = max(water, max_water)

        if a[l] <= a[r]:
            l += 1
        else:
            r -= 1

    return max_water


print(most_water([2, 1, 10, 11, 3]))
