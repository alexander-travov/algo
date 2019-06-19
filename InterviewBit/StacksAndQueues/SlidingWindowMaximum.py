"""
Sliding Window Maximum
======================

A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window. The following example will give you more clarity.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position	       Max

[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]


Solution
--------

We can build MaxQueue on top of two MaxStacks to keep current maximum in the queue.
That way enqueue and getMax operations would be O(1) and dequeue would be O(1) amortized.

Time complexity for generating sliding window max is O(N).
"""

from __future__ import print_function


class MaxStack:
    def __init__(self):
        self.elems = []
        self.maxs = []

    def empty(self):
        return len(self.elems) == 0

    def push(self, x):
        self.elems.append(x)
        if self.maxs:
            self.maxs.append(max(self.maxs[-1], x))
        else:
            self.maxs.append(x)

    def pop(self):
        if self.elems:
            return self.elems.pop()

    def top(self):
        if self.elems:
            return self.elems[-1]

    def getMax(self):
        if self.maxs:
            return self.maxs[-1]


class MaxQueue:
    def __init__(self):
        self.head = MaxStack()
        self.tail = MaxStack()

    def empty(self):
        return self.head.empty() and self.tail.empty()

    def enqueue(self, x):
        self.head.push(x)

    def dequeue(self):
        if self.tail.empty():
            while not self.head.empty():
                self.tail.push(self.head.pop())
        return self.tail.pop()

    def getMax(self):
        return max(self.head.getMax(), self.tail.getMax())


def window_max(arr, w):
    mq = MaxQueue()
    for x in arr[:w-1]:
        mq.enqueue(x)

    for x in arr[w-1:]:
        mq.enqueue(x)
        yield mq.getMax()
        mq.dequeue()


print(list(window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)))
