# -*- coding: utf8 -*-
"""
Level Order
===========

Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""

from __future__ import print_function
from collections import deque


class Node:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r

    def __repr__(self):
        return '{%r}' % self.data


def level_order(tree):
    levels = []

    current_level = [tree]
    next_level = []

    while current_level:
        for n in current_level:
            if n.left:
               next_level.append(n.left)
            if n.right:
               next_level.append(n.right)
        levels.append(current_level)
        current_level = next_level
        next_level = []

    return levels


tree = Node(4, Node(2, Node(1), Node(3)), Node(6, r=Node(7)))
print(level_order(tree))
