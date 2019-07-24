from queen import *


class Board:

    def __init__(self, solution):
        self.nCols = len(solution)
        self.solution = solution
        self.rows = []
        self.fill_board()

    def fill_board(self):
        for i in range(self.nCols):
            # row = []
            # for j in range(self.nCols):
            #    if j == self.solution[i]-1:
            #       row.append(1)
            #    else:
            #       row.append(0)

            row = [1 if j == self.solution[i] - 1 else 0 for j in range(self.nCols)]
            self.rows.append(row)

    def place_queen(self, queen):
        if isinstance(queen, Queen):
            self.rows[queen.row][queen.col] = 1

    def remove_queen(self, queen):
        if isinstance(queen, Queen):
            self.rows[queen.row][queen.col] = 0

    def is_full(self):
        for col in range(self.nCols):
            if self.solution[col] == 0:
                return False
        return True

    def print_board(self):
        for i in range(self.nCols):
            print(self.rows[i])

    def print_solution(self):
        result = ""
        for col in range(len(self.solution)):
            result += (str(self.solution[col]) + ' ')
        print(result)
