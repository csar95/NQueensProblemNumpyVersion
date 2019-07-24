import copy
from queen import *


class Game:

    # Class variable
    numberOfSolutions = 0

    # Instance variable
    currentEmptyCol = 0

    def __init__(self, board):
        self.board = board

    def find_solutions(self):

        if self.board.is_full():
            Game.numberOfSolutions += 1
            self.board.print_solution()
            return

        # Find first empty column
        self.currentEmptyCol = np.argmin(self.board.solution)

        # Play with the user input
        for rowIndex in range(1, self.board.nCols + 1):
            self.board.solution[self.currentEmptyCol] = rowIndex
            q = Queen(self.currentEmptyCol, rowIndex)
            self.board.place_queen(q)
            if not q.is_threatened(self.board):
                gameCopy = Game(copy.deepcopy(self.board))
                gameCopy.find_solutions()
            self.board.remove_queen(q)

    def is_solution_correct(self):
        for col in range(self.board.nCols):
            if Queen(col, self.board.solution[col]).is_threatened(self.board):
                return False
        return True
