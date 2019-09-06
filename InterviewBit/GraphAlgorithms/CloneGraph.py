"""
Clone Graph
===========

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""

from __future__ import print_function


class Node:
    def __init__(self, label, neighbours=None):
        self.label = label
        if neighbours is None:
            neighbours = []
        self.neighbours = neighbours

    def __repr__(self):
        return '{%r}->%r' % (self.label, [n.label for n in self.neighbours])


n1 = Node('1')
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')
n5 = Node('5')

n1.neighbours = [n2, n3]
n2.neighbours = [n1, n4]
n3.neighbours = [n1, n4, n5]
n4.neighbours = [n2, n3]
n5.neighbours = [n3]

graph = [n1, n2, n3, n4, n5]


def clone(graph):
    id_index = {id(n): i for i, n in enumerate(graph)}
    graph_copy = [Node(n.label) for n in graph]
    for i, n in enumerate(graph):
        for v in n.neighbours:
            vi = id_index[id(v)]
            v_copy = graph_copy[vi]
            graph_copy[i].neighbours.append(v_copy)
    return graph_copy


graph_copy = clone(graph)
for n in graph_copy:
    print(n)
