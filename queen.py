class Queen:

    def __init__(self, realCol, realRow):
        self.row = int(realCol)
        self.col = int(realRow) - 1

    def is_threatened(self, board):

        # --------- Check that there is only a 1 in the row -------- #

        for j in range(len(board.rows[self.row])):
            if j != self.col and board.rows[self.row][j] == 1:
                return True

        # ------- Check that there is only a 1 in the column ------- #

        for i in range(board.nCols):
            if i != self.row and board.rows[i][self.col] == 1:
                return True

        # ----- Oheck that there is only a 1 in both diagonals ----- #

        for i in range(board.nCols):
            index = i - self.row
            if index != 0:
                if 0 <= (self.col + index) < board.nCols and board.rows[self.row + index][self.col + index] == 1:
                    return True
                elif 0 <= (self.col - index) < board.nCols and board.rows[self.row + index][self.col - index] == 1:
                    return True

        return False
