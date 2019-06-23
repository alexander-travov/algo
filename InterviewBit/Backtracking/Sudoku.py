"""
Sudoku
======

Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.' 
You may assume that there will be only one unique solution.
"""

from __future__ import print_function


class Sudoku:
    def __init__(self, puzzle):
        self.cells = [
            [0 if c=='x' else int(c) for c in line]
            for line in puzzle
        ]

        self.num_set_cells = sum(self.cells[r][c] != 0 for r in range(9) for c in range(9))

        self.choices = [
            [self._init_choices(r, c) for c in range(9)]
            for r in range(9)
        ]

    def _init_choices(self, row, col):
        ch = [True] * 10
        ch[0] = False

        for c in range(9):
            n = self.cells[row][c]
            ch[n] = False

        for r in range(9):
            n = self.cells[r][col]
            ch[n] = False

        r, c = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                n = self.cells[r+i][c+j]
                ch[n] = False

        return ch

    def __str__(self):
        return '\n'.join(
            ''.join(str(v) if v else 'x' for v in self.cells[r])
            for r in range(9)
        )

    def __repr__(self):
        return 'Sudoku(\n' + str(self) + '\n)'

    def set_cell(self, row, col, val):
        self.cells[row][col] = val
        self.num_set_cells += 1

        for c in range(9):
            self.choices[row][c][val] = False

        for r in range(9):
            self.choices[r][col][val] = False

        r, c = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                self.choices[r+i][c+j][val] = False

    def free_cell(self, row, col):
        val = self.cells[row][col]
        self.cells[row][col] = 0
        self.num_set_cells -= 1

        for c in range(9):
            self.choices[row][c] = self._init_choices(row, c)

        for r in range(9):
            self.choices[r][col] = self._init_choices(r, col)

        r, c = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                self.choices[r+i][c+j] = self._init_choices(r+i, c+j)

    def num_choices(self, row, col):
        return sum(self.choices[row][col])


def solve(sudoku):
    print(sudoku.num_set_cells)
    if sudoku.num_set_cells == 81:
        return sudoku

    min_num_choices = 10
    min_r, min_c = -1, -1

    for r in range(9):
        for c in range(9):
            if sudoku.cells[r][c]:
                continue
            num_choices = sudoku.num_choices(r, c)
            if num_choices < min_num_choices:
                min_num_choices = num_choices
                min_r = r
                min_c = c

    if min_num_choices == 0:
        return None

    for val in range(1, 10):
        if not sudoku.choices[min_r][min_c][val]:
            continue
        print(sudoku)
        print('In pos: ({}, {}) setting {} from {} choices.'.format(
            min_r, min_c, val, sudoku.choices[min_r][min_c]))
        sudoku.set_cell(min_r, min_c, val)
        solution = solve(sudoku)
        if solution:
            return solution
        print('Deadend: Free cell: ({}, {})'.format(min_r, min_c))
        sudoku.free_cell(min_r, min_c)


s = Sudoku([
    '53xx7xxxx',
    '6xx195xxx',
    'x98xxxx6x',
    '8xxx6xxx3',
    '4xx8x3xx1',
    '7xxx2xxx6',
    'x6xxxx28x',
    'xxx419xx5',
    'xxxx8xx79'
])

s = Sudoku([
    '6xx3xxxxx',
    'x13x6xxxx',
    'xxxx9xx8x',
    '4xxxx5xxx',
    'x6xxx4x9x',
    'x3xxxx7xx',
    '8xxxxx25x',
    'xxx8x1xx9',
    'x4x9xxxx1',
])
solve(s)
