"""
Capture Regions on Board
========================

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input Format:

    First and only argument is a N x M character matrix A
Output Format:

    make changes to the the input only as matrix is passed by reference.
Constraints:

    1 <= N,M <= 1000
For Example:

Input 1:
    A = [ [X, X, X, X],
          [X, O, O, X],
          [X, X, O, X],
          [X, O, X, X] ]
Output 1:
    After running your function, the board should be:
    A = [ [X, X, X, X],
          [X, X, X, X],
          [X, X, X, X],
          [X, O, X, X] ]
Explanation:
    O in (4,2) is not surrounded by X from below.
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


def capture(field):
    def dfs(row, col, symb):
        field[row, col] = symb
        for r, c in field.neighbours(row, col):
            if field[r, c] == '0':
                dfs(r, c, symb)

    # fill border regions
    for row in range(field.height):
        for col in (0, field.width-1):
            if field[row, col] == '0':
                dfs(row, col, 'B')

    for col in range(1, field.width-1):
        for row in (0, field.height-1):
            if field[row, col] == '0':
                dfs(row, col, 'B')

    # capture inner regions
    for row in range(field.height):
        for col in range(field.width):
            if field[row, col] == '0':
                dfs(row, col, 'X')


field = Field(cells=(
    list("X00XXXX"),
    list("00X00X0"),
    list("0X0XXX0")
))
print(field)
print()
capture(field)
print(field)
