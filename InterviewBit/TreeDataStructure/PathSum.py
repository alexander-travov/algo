"""
Path Sum
========

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def path_sum(node, target):
    if node is None:
        return target == 0
    return (path_sum(node.left, target-node.data) or
            path_sum(node.right, target-node.data))


tree = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, right=Node(1))))
print(path_sum(tree, 22))
