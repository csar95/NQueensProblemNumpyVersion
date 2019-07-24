from queen import *
import numpy as np


class Board:

    def __init__(self, solution):
        self.nCols = solution.size
        self.solution = solution
        self.rows = np.zeros((self.nCols, self.nCols), dtype=int)
        self.fill_board()

    def fill_board(self):
        for col, rowIndex in zip(range(self.nCols), np.nditer(self.solution)):
            if rowIndex == 0:
                break
            self.rows[col][rowIndex-1] = 1

    def place_queen(self, queen):
        if isinstance(queen, Queen):
            self.rows[queen.row][queen.col] = 1

    def remove_queen(self, queen):
        if isinstance(queen, Queen):
            self.rows[queen.row][queen.col] = 0

    def is_full(self):
        if np.min(self.solution) == 0:
            return False
        return True

    def print_board(self):
        for i in range(self.nCols):
            print(self.rows[i])

    def print_solution(self):
        result = ""
        for col in range(self.nCols):
            result += (str(self.solution[col]) + ' ')
        print(result)
