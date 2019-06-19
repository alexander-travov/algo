# -*- coding: utf-8 -*-
"""
Largest Rectangle in Histogram
==============================

Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.

Solution
--------

Problem can be solved with two stacks in O(N).
"""

from __future__ import print_function


def largest_rect(hist):
    heights = []
    positions = []
    max_area = 0

    hist.append(0) # Fake zero bar

    for i, h in enumerate(hist):
        if not heights or h > heights[-1]:
            heights.append(h)
            positions.append(i)
        else:
            while heights and h <= heights[-1]:
                area = heights[-1] * (i - positions[-1])
                max_area = max(max_area, area)
                heights.pop()
                p = positions.pop()
            heights.append(h)
            positions.append(p)

    return max_area


print(largest_rect([1, 3, 2, 1, 2]))
