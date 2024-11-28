import time
from cell import Cell
from graphics import Point


class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_width, cell_height):
        self._x = x
        self._y = y
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._cells = []
        self._create_cells(num_rows, num_cols)
        self._break_entrance_and_exit()

    def _create_cells(self, num_rows, num_cols):
        self._cells = [ [None]*num_cols for _ in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                cell = self._make_cell(row, col)
                self._cells[row][col] = cell

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

    def draw_cells(self, window):
        for row in self._cells:
            for cell in row:
                cell.draw(window)
                self._animate(window)

    def _make_cell(self, row, col):
        p1 = Point(self._x + (col * self._cell_width), self._y + (row * self._cell_height))
        p2 = Point(p1.x + self._cell_width, p1.y + self._cell_height)
        return Cell(True, True, True, True, p1, p2)

    def _animate(self, window):
        window.redraw()
        time.sleep(0.05)
        