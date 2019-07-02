"""
Max Depth of Binary Tree
========================

Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
max depth = 2.
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def max_depth(node, depth=0):
    if node.left is None and node.right is None:
        return depth+1
    elif node.left and node.right:
        return max(
            max_depth(node.right, depth+1),
            max_depth(node.left, depth+1)
        )
    elif node.left:
        return max_depth(node.left, depth+1)
    else:
        return max_depth(node.right, depth+1)


tree = Node(1, Node(2, Node(5)), Node(3, Node(4), Node(6, Node(7))))
print(max_depth(tree))
