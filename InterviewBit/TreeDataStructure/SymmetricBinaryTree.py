"""
Symmetric Binary Tree
======================

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric. 
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

from __future__ import print_function


class Node:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r


def symmetrical(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None and t2 is not None:
        return False
    elif t1 is not None and t2 is None:
        return False
    return (t1.data == t2.data and
            symmetrical(t1.left, t2.right) and
            symmetrical(t1.right, t2.left))


tree = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
print(symmetrical(tree.left, tree.right))
