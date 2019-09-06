# -*- coding: utf8 -*-
"""
Valid Path
==========

There is a rectangle with left bottom as (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.
"""

from __future__ import print_function
from collections import namedtuple


Circle = namedtuple('Circle', 'x y r')


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[True]*height for _ in range(width)]

    def block_circle(self, circle):
        min_x = max(0, circle.x - circle.r)
        max_x = min(self.width, circle.x + circle.r + 1)
        min_y = max(0, circle.y - circle.r)
        max_y = min(self.height, circle.y + circle.r + 1)
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if (x - circle.x)**2 + (y - circle.y)**2 <= circle.r**2:
                    self.cells[x][y] = False

    def contains(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def __str__(self):
        return '\n'.join(
            ''.join('0' if c else 'X' for c in line)
            for line in self.cells
        )


f = Field(15, 10)
circles = [Circle(5, 1, 2), Circle(10, 7, 3)]
for c in circles:
    f.block_circle(c)

print(f)


def bfs(field):
    from collections import deque
    q = deque()
    if field.cells[0][0]:
        q.append((0, 0))
        f.cells[0][0] = False

    while q:
        x, y = q.popleft()
        if x == field.width-1 and y == field.height-1:
            print("Path found")
            return

        for i in range(-1, 2):
            for j in range(-1, 2):
                if field.contains(x+i, y+j) and field.cells[x+i][y+j]:
                    field.cells[x+i][y+j] = False
                    q.append((x+i, y+j))


def dfs(field, x=0, y=0):
    if x == field.width-1 and y == field.height-1:
        print("Path found")

    if field.cells[x][y]:
        field.cells[x][y] = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if field.contains(x+i, y+j) and field.cells[x+i][y+j]:
                    dfs(field, x+i, y+j)


# print('BFS')
# bfs(f)
print('DFS')
dfs(f)
