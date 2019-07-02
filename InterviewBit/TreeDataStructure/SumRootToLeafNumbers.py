"""
Sum Root to Leaf Numbers
========================

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def number_sum(node):
    # Leaf node
    if node.left is None and node.right is None:
        return [(node.data, 0)]
    nums = []
    if node.left:
        nums += number_sum(node.left)
    if node.right:
        nums += number_sum(node.right)
    return [
        (node.data * 10**(d+1) + n, d+1)
        for n, d in nums
    ]


tree = Node(5, Node(4), Node(3, Node(2)))
print(number_sum(tree))
