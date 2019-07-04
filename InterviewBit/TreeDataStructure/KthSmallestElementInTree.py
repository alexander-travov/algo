"""
Kth Smallest Element In Tree
============================

Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
NOTE : You may assume 1 <= k <= Total number of nodes in BST
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __iter__(self):
        return Node.NodeIterator(self)

    def __reversed__(self):
        return Node.NodeReverseIterator(self)

    def __getitem__(self, k):
        it = self if k >= 0 else reversed(self)
        if k < 0:
            k = -k-1
        for i, el in enumerate(it):
            if i == k:
                return el

    class NodeIterator:
        def __init__(self, root):
            self.root = root
            self.current = None
    
        def next(self):
            # Find minimum on the first run
            if not self.current:
                node = self.root
                while node.left:
                    node = node.left
                self.current = node
                return node.data

            # If there is right child, go down
            successor = self.current.right
            if successor:
                while successor.left:
                    successor = successor.left
            # Otherwise, go up
            else:
                node = self.root
                data = self.current.data
                while node.data != data:
                    if node.data > data:
                        successor = node
                        node = node.left
                    else:
                        node = node.right
    
            # On max element in BST - stop
            if not successor:
                raise StopIteration
    
            self.current = successor
            return successor.data
       
        __next__ = next

    class NodeReverseIterator:
        def __init__(self, root):
            self.root = root
            self.current = None

        def __iter__(self):
            return self
    
        def next(self):
            # Find maximum on the first run
            if not self.current:
                node = self.root
                while node.right:
                    node = node.right
                self.current = node
                return node.data

            # If there is left child, go down
            predessor = self.current.left
            if predessor:
                while predessor.right:
                    predessor = predessor.right
            # Otherwise, go up
            else:
                node = self.root
                data = self.current.data
                while node.data != data:
                    if node.data > data:
                        node = node.left
                    else:
                        predessor = node
                        node = node.right
    
            # On min element in BST - stop
            if not predessor:
                raise StopIteration
    
            self.current = predessor
            return predessor.data

        __next__ = next


tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print('Fourth:', tree[3])
print('Min:', tree[0])
print('Max:', tree[-1])
