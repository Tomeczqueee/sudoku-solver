from game.cell import Cell
from game.board import Board
import array as arr


class SudokuSolver(Board):
    def __repr__(self):
        return f'Sudoku solver object ' \
               f'with {self.cell_set_size} sized cells'

    # Defines cell_set position basing on x,y coords, e.g. for (4,5) it is 5, fifth box
    def define_position(self, x, y):
        positions = [tuple(coord for coord in range(scale, scale + self.cell_set_size))
                     for scale in range(0, len(self.board), self.cell_set_size)]
        sets = sorted([tuple([x, y]) for y in positions for x in positions])

        for p in sets:
            if x in p[1] and y in p[0]:
                return sets.index(p)

    @property
    def cell_sets(self):
        return [self.get_cell_set(pos) for pos in range(1, len(self.board) + 1)]

    @property
    def unsolved_cells(self):
        unsolved = []

        for y, line in enumerate(self.board):
            for x in range(0, self.cell_set_size ** 2):
                if line[x] == 0:
                    cell_set_index = self.define_position(x, y)
                    cell_set = self.cell_sets[cell_set_index]
                    unsolved.append(Cell(x, y, current_cell_set=cell_set, current_board=self.board))
        return unsolved

    def solve(self):
        while self.unsolved_cells:
            for unsolved in self.unsolved_cells:
                cell_poss = unsolved.cell_possibilities
                x, y = unsolved.x, unsolved.y

                if len(cell_poss) == 1:
                    self.board[y][x] = list(cell_poss)[0]

        return self.board

    def check_correctness(self, solution):
        computed_solution = self.solve()
        passed_solution = [arr.array('H', row) for row in solution]
        return passed_solution == computed_solution
