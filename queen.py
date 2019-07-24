import numpy as np


class Queen:

    def __init__(self, realCol, realRow):
        self.row = int(realCol)
        self.col = int(realRow) - 1

    def is_threatened(self, board):

        # --------- Check that there is only a 1 in the row -------- #

        if np.sum(board.rows[self.row]) > 1:  # THE SAME AS: if board.rows[self.row].sum() > 1:
            return True

        # ------- Check that there is only a 1 in the column ------- #

        if np.sum(board.rows, axis=0)[self.col] > 1:
            return True

        # ----- Check that there is only a 1 in both diagonals ----- #

        for i in range(board.nCols):
            index = i - self.row
            if index != 0:
                if 0 <= (self.col + index) < board.nCols and board.rows[self.row + index][self.col + index] == 1:
                    return True
                elif 0 <= (self.col - index) < board.nCols and board.rows[self.row + index][self.col - index] == 1:
                    return True

        return False
