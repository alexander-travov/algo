"""
Binary Tree From Inorder And Postorder
======================================

Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree. 

Example:

Input: 
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return: 
            1
           / \
          2   3

Solution
--------

inorder: (left)root(right)
postorder: (left)(right)root

Last element in postorder traversal gives us the root key.
Then we can scan inorder traversal and all elements before the root key go to the left subtree and vice versa.
F.e. from inorder we get that keys k1, k2, ... kn go in the left subtree.
First n elements in postorder arr would give use postorder arr for left subtree.
For left and right subtree we call same procedure recursively.
"""


from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bst_from_inorder_and_postorder(inorder, postorder):
    if not inorder:
        return None

    root_key = postorder[-1]
    root_key_ind = inorder.index(root_key)

    return Node(
        data=root_key,
        left=bst_from_inorder_and_postorder(
            inorder[:root_key_ind],
            postorder[:root_key_ind]
        ),
        right=bst_from_inorder_and_postorder(
            inorder[root_key_ind+1:],
            postorder[root_key_ind:-1]
        )
    )


def bst_from_inorder_and_preorder(inorder, preorder):
    if not inorder:
        return None

    root_key = preorder[0]
    root_key_ind = inorder.index(root_key)

    return Node(
        data=root_key,
        left=bst_from_inorder_and_preorder(
            inorder[:root_key_ind],
            preorder[1:root_key_ind+1]
        ),
        right=bst_from_inorder_and_preorder(
            inorder[root_key_ind+1:],
            preorder[root_key_ind+1:]
        )
    )


tree = bst_from_inorder_and_postorder([2, 1, 3], [2, 3, 1])
tree2 = bst_from_inorder_and_preorder([2, 1, 3], [2, 3, 1])
