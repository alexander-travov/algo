"""
BST Iterator
============

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity.
"""

from __future__ import print_function


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __iter__(self):
        return Node.NodeIterator(self)

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


tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(list(tree))
