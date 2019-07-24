import copy
from queen import *


class Game:

    # Class variable
    numberOfSolutions = 0

    def __init__(self, board):
        self.board = board

    def find_solutions(self):

        if self.board.is_full():
            Game.numberOfSolutions += 1
            self.board.print_solution()
            return

        # Find first empty column
        currentEmptyCol = 0
        for col in range(self.board.nCols):
            if self.board.solution[col] == 0:
                currentEmptyCol = col
                break

        # Play with the user input
        for rowIndex in range(1, self.board.nCols + 1):
            self.board.solution[currentEmptyCol] = rowIndex
            q = Queen(currentEmptyCol, rowIndex)
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
