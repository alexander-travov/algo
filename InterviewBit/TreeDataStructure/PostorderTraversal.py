# -*- coding: utf8 -*-
"""
Postorder Traversal
=================

Given a binary tree, return the postorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [3, 2, 1].

Using recursion is not allowed.

Solution
--------

We can use two stacks for getting postorder traversal.
One for nodes to process and one for processed data.
Time complexity O(N), space complexity O(N).
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def postorder(root):
    s1 = []
    s2 = []

    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node.data)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        yield s2.pop()


def recursive_postorder(root):
    if root is None:
        return
    for d in recursive_postorder(root.left):
        yield d
    for d in recursive_postorder(root.right):
        yield d
    yield root.data


tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(list(postorder(tree)))
print(list(recursive_postorder(tree)))
