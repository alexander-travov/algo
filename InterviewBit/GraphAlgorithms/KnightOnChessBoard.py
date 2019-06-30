"""
Knight On Chess Board
=====================

Given any source point and destination point on a chess board, we need to find whether Knight can move to the destination or not.

If yes, then what would be the minimum number of steps for the knight to move to the said point.
If knight can not move from the source point to the destination point, then return -1

Input:

    N, M, x1, y1, x2, y2
    where N and M are size of chess board
    x1, y1  coordinates of source point
    x2, y2  coordinates of destination point

Solution
--------

Use BFS.
"""

from __future__ import print_function
from collections import deque


def knight(n, m, start, stop):
    board = [[-1]*m for _ in range(n)]
    board[start[0]][start[1]] = 0

    q = deque()
    q.append(start)

    while q:
        row, col = q.popleft()
        num_moves = board[row][col]

        if (row, col) == stop:
            return num_moves

        for dr, dc in (
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ):
            r = row + dr
            c = col + dc
            if 0<=r<n and 0<=c<m and board[r][c] == -1:
                board[r][c] = num_moves+1
                q.append((r, c))

    return -1


print(knight(8, 8, (0,0), (7, 7)))
