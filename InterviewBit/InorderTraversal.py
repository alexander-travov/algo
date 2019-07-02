# -*- coding: utf8 -*-
"""
Inorder Traversal
=================

Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.

Solution
--------

Morris traversal uses O(1) extra space, works in O(N) time, generates inorder
tree traversal and leaves tree without change after work.
But during work it can change pointers to right child in some nodes.
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    while root:
        # 1. If root does not have left subtree, yield its value and go to the right
        if root.left is None:
            yield root.data
            root = root.right
            continue

        # 2. Otherwise, try to find root's predecessor node.
        node = root.left
        while True:
            # Save uplink to the root in its predecessor creating a cycle
            # and go to the left subtree
            if node.right is None:
                node.right = root
                root = root.left
                break

            # If on our way of finding predecessor we bump into out node
            # Then we have a cycle.
            # Break cycle, restoring predecessor's right link,
            # yield data and go to the right subtree
            if node.right is root:
                node.right = None
                yield root.data
                root = root.right
                break

            node = node.right


tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(list(inorder(tree)))
