"""
Inorder Traversal of Cartesian Tree
===================================

Given an inorder traversal of a cartesian tree, construct the tree.

 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 
 Note: You may assume that duplicates do not exist in the tree. 
Example :

Input : [1 2 3]

Return :   
          3
         /
        2
       /
      1

Solution
--------

Heap is constructed with the following recursive procedure:
1. Find max in an array. It goes to the root.
2. All keys in inorder traversal before the maximum form the left subtree, after the maximum - right subtree.
3. Use same procedure for left and right subtree.
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def heap_from_arr(arr):
    if not arr:
        return None

    max_key = max(arr)
    max_key_ind = arr.index(max_key)

    left_subtree = heap_from_arr(arr[:max_key_ind])
    right_subtree = heap_from_arr(arr[max_key_ind+1:])

    return Node(max_key, left_subtree, right_subtree)


heap = heap_from_arr([1, 2, 4, 3])
