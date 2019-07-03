# -*- coding: utf8 -*-
"""
ZigZag Level Order Traversal BT
===============================

Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example: 
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
  [3],
  [20, 9],
  [15, 7]
]
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def zigzag(node):
    if node is None:
        return

    s1 = [node]
    s2 = []
    reverse = False

    while True:
        n = s1.pop()
        yield n.data
        children = [n.left, n.right]
        if reverse:
            children.reverse()
        for ch in children:
            if ch is not None:
                s2.append(ch)
        if not s1:
            if not s2:
                break
            s1 = s2
            s2 = []
            reverse = not reverse


# perfect binary search tree of height 3.
tree = Node(8, Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7))),
               Node(12, Node(10, Node(9), Node(11)), Node(14, Node(13), Node(15))))
print(list(zigzag(tree)))
