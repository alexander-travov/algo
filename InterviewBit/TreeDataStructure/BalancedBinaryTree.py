"""
Balanced Binary Tree
====================

Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
"""

from __future__ import print_function


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height_balanced(node):
    """
    Returns a height of a tree and a boolean indicating whether it is balanced.
    """
    if node is None:
        return 0, True

    if node.left is None and node.right is None:
        return 0, True

    left_height, left_balance = height_balanced(node.left)
    right_height, right_balance = height_balanced(node.right)

    height = max(left_height, right_height) + 1
    balanced = left_balance and right_balance and abs(left_height-right_height) <= 1
    return height, balanced


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n2.right = n3

print(height_balanced(n1))
