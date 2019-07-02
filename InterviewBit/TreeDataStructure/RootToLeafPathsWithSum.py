# -*- coding: utf8 -*-
"""
Root to Leaf Paths With Sum
===========================

Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def path_sum(node, target):
    if node.left is None and node.right is None:
        if target == node.data:
            return [[node.data]]
        else:
            return []
    paths = []
    if node.left:
        paths += path_sum(node.left, target-node.data)
    if node.right:
        paths += path_sum(node.right, target-node.data)
    return [[node.data]+p for p in paths]


tree = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, Node(5), Node(1))))
print(path_sum(tree, 22))
