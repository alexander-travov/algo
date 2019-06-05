"""
Merge Overlapping Intervals
===========================

Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""

from __future__ import print_function


def merge_overlapping_intervals(intervals):
    # First make sure intervals are sorted according to their start time.
    # This makes solution O(NlogN)
    intervals.sort(key=lambda x: x[0])

    merged_start, merged_stop = intervals[0]

    for start, stop in intervals[1:]:
        if start <= merged_stop:
            merged_stop = max(merged_stop, stop)
        else:
            yield [merged_start, merged_stop]
            merged_start = start
            merged_stop = stop

    yield [merged_start, merged_stop]


for intervals in (
        [[1,3], [6,9], [2,5]],
        [[1,2], [3,5], [6,7], [8,10], [12,16], [4,9]],
        [[1,3], [2,6], [8,10], [15,18]],
        [[1, 2]],
    ):
    print(intervals, '~', list(merge_overlapping_intervals(intervals)))
