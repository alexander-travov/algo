# -*- coding: utf8 -*-
"""
NQueens
=======

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

from __future__ import print_function
import sys


class Chessboard:
    def __init__(self, n):
        self.n = n
        self.hits = [[0]*n for _ in range(n)]
        self.board = [['.']*n for _ in range(n)]

    def __str__(self):
        return '\n'.join(
            ''.join(self.board[i]) for i in range(self.n)
        )

    def __repr__(self):
        return 'Chessboard(\n' + str(self) + '\n)'

    def in_board(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n

    def queen(self, row, col, remove=False):
        self.board[row][col] = '.' if remove else 'Q'
        a = -1 if remove else 1

        for r in range(self.n):
            self.hits[r][col] += a
        for c in range(self.n):
            self.hits[row][c] += a

        k = 1
        while self.in_board(row-k, col-k):
            self.hits[row-k][col-k] += a
            k += 1

        k = 1
        while self.in_board(row-k, col+k):
            self.hits[row-k][col+k] += a
            k += 1

        k = 1
        while self.in_board(row+k, col-k):
            self.hits[row+k][col-k] += a
            k += 1

        k = 1
        while self.in_board(row+k, col+k):
            self.hits[row+k][col+k] += a
            k += 1


def find_queens(board, row=0):
    if board.n == row:
        yield str(board)
    else:
        for c in range(board.n):
            if board.hits[row][c]:
                continue
            board.queen(row, c)
            for pos in find_queens(board, row+1):
                yield pos
            board.queen(row, c, remove=True)


if __name__ == '__main__':
    b = Chessboard(int(sys.argv[1]))
    for i, pos in enumerate(find_queens(b)):
        print(i+1)
        print(pos)
        print()
