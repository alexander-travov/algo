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
            [0 if c=='.' else int(c) for c in line]
            for line in puzzle
        ]

        self.num_set_cells = sum(
            self.cells[r][c] != 0
            for r in range(9)
            for c in range(9)
        )

        self.choices = [
            [self.reset_choices(r, c) for c in range(9)]
            for r in range(9)
        ]

    def reset_choices(self, row, col):
        ch = [True] * 10
        ch[0] = False # Ficticious zero cell

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
            ''.join(str(v) if v else '.' for v in self.cells[r])
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
        self.cells[row][col] = 0
        self.num_set_cells -= 1

        for c in range(9):
            self.choices[row][c] = self.reset_choices(row, c)

        for r in range(9):
            self.choices[r][col] = self.reset_choices(r, col)

        r, c = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                self.choices[r+i][c+j] = self.reset_choices(r+i, c+j)

    def num_choices(self, row, col):
        return sum(self.choices[row][col])


def solve(sudoku):
    # All cells are set. Solution is found.
    if sudoku.num_set_cells == 81:
        return sudoku

    # Find empty cell with minimum number of available choices.
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

    # Not a solution. One of the previous guesses was wrong.
    if min_num_choices == 0:
        return None

    for val in range(1, 10):
        # Try to solve sudoku for every available choice
        if not sudoku.choices[min_r][min_c][val]:
            continue
        sudoku.set_cell(min_r, min_c, val)
        solution = solve(sudoku)
        if solution:
            return solution
        # If solution is not found - reset cell and try next choice.
        sudoku.free_cell(min_r, min_c)


s = Sudoku([
    '6..3.....',
    '.13.6....',
    '....9..8.',
    '4....5...',
    '.6...4.9.',
    '.3....7..',
    '8.....25.',
    '...8.1..9',
    '.4.9....1',
])
print(solve(s))
