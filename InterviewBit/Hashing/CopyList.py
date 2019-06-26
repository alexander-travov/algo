"""
Copy List
=========

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example:

Given list

   1 -> 2 -> 3

with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1

You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them.
The pointers in the returned list should not link to any node in the original input list.
"""

from __future__ import print_function


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None

    def __str__(self):
        node = self
        s = []
        while node:
            s.append('{}: {}->{}'.format(
                id(node),
                node.val,
                node.rand and node.rand.val
            ))
            node = node.next
        return '\n'.join(s)

    def deep_copy(self):
        id_to_index = {}
        node = self
        n = 0
        while node:
            id_to_index[id(node)] = n
            node = node.next
            n += 1

        rand_indices = []
        node = self
        while node:
            if node.rand:
                ind = id_to_index[id(node.rand)]
            else:
                ind = -1
            rand_indices.append(ind)
            node = node.next

        list_copy = []
        node = self
        while node:
            list_copy.append(Node(node.val))
            node = node.next

        for i, n in enumerate(list_copy):
            if i < len(list_copy)-1:
                n.next = list_copy[i+1]
            ri = rand_indices[i]
            if ri != -1:
                n.rand = list_copy[ri]

        return list_copy[0]


l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l1.next = l2
l2.next = l3
l3.next = l4
l1.rand = l3
l2.rand = l1
l3.rand = l1
print('Original:')
print(str(l1))
lc = l1.deep_copy()
print('Copy:')
print(str(lc))
