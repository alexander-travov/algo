"""
Merge Intervals
===============

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""

from __future__ import print_function


def merge_intervals(intervals, new_interval):
    new_start, new_stop = new_interval

    i = 0
    N = len(intervals)

    # preceding intervals
    while i < N:
        start, stop = interval = intervals[i]
        if stop < new_start:
            yield interval
        else:
            merged_start = min(start, new_start)
            merged_stop = max(stop, new_stop)
            break
        i += 1

    # merged interval
    while i < N:
        start, stop = intervals[i]
        if start > merged_stop:
            yield [merged_start, merged_stop]
            break
        merged_stop = max(merged_stop, stop)
        i += 1

    # following intervals
    for interval in intervals[i:]:
        yield interval


for intervals, new_int in (
            ([[1,3],[6,9]], [2,5]),
            ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]),
        ):
    print(intervals, '+', new_int, '=', list(merge_intervals(intervals, new_int)))
