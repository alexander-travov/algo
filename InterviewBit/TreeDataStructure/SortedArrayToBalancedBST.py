"""
Sorted Array To Balanced BST
============================

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Balanced tree: a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 

Example:
Given A: [1, 2, 3]
A height balanced BST: 

      2
    /   \
   1     3
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def balanced_tree_from_arr(arr):
    if not arr:
        return None

    root_key_ind = len(arr) // 2
    return Node(
        data=arr[root_key_ind],
        left=balanced_tree_from_arr(arr[:root_key_ind]),
        right=balanced_tree_from_arr(arr[root_key_ind+1:])
    )


def height_balanced(node):
    """
    Returns a height of a tree and a boolean indicating whether it is balanced.
    """
    if node is None:
        return -1, True

    if node.left is None and node.right is None:
        return 0, True

    left_height, left_balance = height_balanced(node.left)
    right_height, right_balance = height_balanced(node.right)

    height = max(left_height, right_height) + 1
    balanced = left_balance and right_balance and abs(left_height-right_height) <= 1
    return height, balanced


tree = balanced_tree_from_arr(list(range(100)))
print(height_balanced(tree))
