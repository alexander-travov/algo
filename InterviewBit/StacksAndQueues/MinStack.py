# -*- coding: utf8 -*-
"""
Min Stack
=========

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1


Solution
--------

We can build a stack on the top of two arrays: one for the elements and one for the minimums.
"""

from __future__ import print_function


class MinStack:
    def __init__(self):
        self.elems = []
        self.mins = []

    def push(self, x):
        self.elems.append(x)
        if self.mins:
            self.mins.append(min(self.mins[-1], x))
        else:
            self.mins.append(x)

    def pop(self):
        if self.elems:
            self.mins.pop()
            return self.elems.pop()

    def top(self):
        if self.elems:
            return self.elems[-1]
        return -1

    def getMin(self):
        if self.mins:
            return self.mins[-1]
        return -1


ms = MinStack()
ms.push(2)
ms.push(3)
ms.push(1)
print('min', ms.getMin())
print('pop', ms.pop())
print('min', ms.getMin())
