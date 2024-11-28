import time
from cell import Cell
from graphics import Point


class Maze:
    def __init__(self, window, x, y, num_rows, num_cols, cell_width, cell_height):
        self._window = window
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for row in range(self._num_rows):
            self._cells.append([])

            for col in range(self._num_cols):
                cell = self._make_cell(row, col)
                self._cells[row].append(cell)
                cell.draw(self._window)
                self._animate()

    def _make_cell(self, row, col):
        p1 = Point(self._x + (col * self._cell_width), self._y + (row * self._cell_height))
        p2 = Point(p1.x + self._cell_width, p1.y + self._cell_height)
        return Cell(True, True, True, True, p1, p2)

    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)
        