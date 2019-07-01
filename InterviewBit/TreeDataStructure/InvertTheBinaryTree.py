"""
Invert the Binary Tree
======================

Given a binary tree, invert the binary tree and return it. 
Look at the example for more details.

Example : 
Given binary tree

     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return

     1
   /   \
  3     2
 / \   / \
7   6 5   4
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def invert(node):
    if node is None:
        return
    tmp = node.left
    node.left = node.right
    node.right = tmp
    invert(node.left)
    invert(node.right)
