"""
2-Sum Binary Tree
=================

Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes

Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :

Input 1: 

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2: 

T:        10
         / \
        9   20

K = 40

Return: 0
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


def find_sum(tree, target):
    for_it = iter(tree)
    rev_it = reversed(tree)

    a = next(for_it)
    b = next(rev_it)

    while a < b:
        if a+b == target:
            break
        elif a+b < target:
            a = next(for_it)
        else:
            b = next(rev_it)
    else:
        return False

    return True


tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
for s in (2, 3, 10, 13, 14):
    print(s, find_sum(tree, s))
