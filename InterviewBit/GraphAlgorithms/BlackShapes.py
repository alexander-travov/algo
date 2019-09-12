"""
Black Shapes
============

Given N x M character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

Input Format:

    The First and only argument is a N x M character matrix.
Output Format:

    Return a single integer denoting number of black shapes.
Constraints:

    1 <= N,M <= 1000
    A[i][j] = 'X' or 'O'
Example:

Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
Note: we are looking for connected shapes here.

XXX
XXX
XXX
is just one single connected black shape.
"""

from __future__ import print_function


class Field:
    def __init__(self, cells):
        lens = {len(s) for s in cells}
        assert len(lens) == 1, 'Not all strings have same length.'
        self.cells = cells

    @property
    def height(self):
        return len(self.cells)

    @property
    def width(self):
        return len(self.cells[0])

    def __getitem__(self, item):
        r, c = item
        return self.cells[r][c]

    def __setitem__(self, key, value):
        r, c = key
        self.cells[r][c] = value

    def __str__(self):
        return '\n'.join(''.join(s) for s in self.cells)

    def neighbours(self, row, col):
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r, c = row+dr, col+dc
            if 0 <= r < self.height and 0 <= c < self.width:
                yield r, c


def num_shapes(field):
    def dfs(row, col, num):
        field[row, col] = str(num)
        for r, c in field.neighbours(row, col):
            if field[r, c] == 'X':
                dfs(r, c, num)

    num = 1
    for row in range(field.height):
        for col in range(field.width):
            if field[row, col] == 'X':
                dfs(row, col, num)
                num += 1

    return num-1


field = Field(cells=(
    list("X00X00X"),
    list("00XX0X0"),
    list("0X000X0")
))
print(field)
print(num_shapes(field))
print(field)
