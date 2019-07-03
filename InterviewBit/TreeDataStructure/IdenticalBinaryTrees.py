"""
Identical Binary Trees
======================

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 or True
"""

from __future__ import print_function


class Node:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r


def identical(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None and t2 is not None:
        return False
    elif t1 is not None and t2 is None:
        return False
    return (t1.data == t2.data and
            identical(t1.left, t2.left) and
            identical(t1.right, t2.right))


tree1 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
tree2 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(identical(tree1, tree2))
