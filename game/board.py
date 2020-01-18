import array as arr
import math


class Board:
    def __init__(self, board):
        self.board = [arr.array('H', row) for row in board]
        self.cell_set_size = int(math.sqrt(len(self.board)))

    def get_cell_set(self, position):
        row = math.ceil(position / self.cell_set_size) - 1
        col = position - (row * self.cell_set_size) - 1

        # Returns numbers box for specefic position
        return [(row[col * self.cell_set_size:(col + 1) * self.cell_set_size])
                for row in self.board[row * self.cell_set_size:(row + 1) * self.cell_set_size]]
