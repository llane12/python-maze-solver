from random import Random
import time
from cell import Cell
from graphics import Point


class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_width, cell_height, seed=None):
        self._x = x
        self._y = y
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._cells = []
        self._create_cells(num_rows, num_cols)
        self._break_entrance_and_exit()
        self._random = Random()
        if seed is not None:
            self._random.seed(seed)

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
                self._animate(window, 0)

    def _make_cell(self, row, col):
        p1 = Point(self._x + (col * self._cell_width), self._y + (row * self._cell_height))
        p2 = Point(p1.x + self._cell_width, p1.y + self._cell_height)
        return Cell(True, True, True, True, p1, p2)

    def _animate(self, window, sleep=0.05):
        window.redraw()
        time.sleep(sleep)

    def break_walls(self, window=None):
        self._break_walls_r(0, 0, window)
        self._reset_cells_visited()

    def _break_walls_r(self, row, col, window):
        cur = self._cells[row][col]
        cur.visited = True

        while True:
            neighbors = []
            if col - 1 >= 0:
                neighbors.append((0, row, col - 1))
            if row - 1 >= 0:
                neighbors.append((1, row - 1, col))
            if col + 1 < len(self._cells[row]):
                neighbors.append((2, row, col + 1))
            if row + 1 < len(self._cells):
                neighbors.append((3, row + 1, col))
            
            # If all neighbors have been visited, return
            if all(self._cells[t[1]][t[2]].visited for t in neighbors):
                return
            
            self._random.shuffle(neighbors)
            for dir, row2, col2 in neighbors:
                neighbor = self._cells[row2][col2]
                if neighbor.visited:
                    continue

                if dir == 0: # left
                    cur.has_left_wall = False
                    neighbor.has_right_wall = False
                elif dir == 1: # up
                    cur.has_top_wall = False
                    neighbor.has_bottom_wall = False
                elif dir == 2: # right
                    cur.has_right_wall = False
                    neighbor.has_left_wall = False
                else: # down
                    cur.has_bottom_wall = False
                    neighbor.has_top_wall = False
                
                if window:
                    cur.draw(window)
                    neighbor.draw(window)
                    self._animate(window)

                self._break_walls_r(row2, col2, window)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
