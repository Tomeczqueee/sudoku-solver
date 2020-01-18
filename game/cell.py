import array as arr


class Cell:
    def __init__(self, x, y, current_cell_set, current_board):
        self.x = x
        self.y = y
        self.current_cell_set = current_cell_set
        self.current_board = current_board

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'

    @property
    def box_possibilities(self):
        box = []
        [box.extend(li) for li in self.current_cell_set]
        available_nums = arr.array('H', (num for num in range(1, 10) if num not in set(box)))

        return available_nums

    @property
    def cell_possibilities(self):
        positions_found = (set(self.current_board[self.y]) | set(row_arr[self.x] for row_arr in self.current_board))
        return set(self.box_possibilities) - positions_found
