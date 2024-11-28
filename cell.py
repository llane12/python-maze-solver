from graphics import *
from constants import *

class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, p1, p2):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.p1 = p1
        self.p2 = p2

    def draw(self, window, line_color="black"):
        window.draw_line(Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y)), line_color if self.has_left_wall else background_color)
        window.draw_line(Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y)), line_color if self.has_right_wall else background_color)
        window.draw_line(Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y)), line_color if self.has_top_wall else background_color)
        window.draw_line(Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y)), line_color if self.has_bottom_wall else background_color)

def draw_move(window : Window, from_cell, to_cell, undo=False):
    from_centre = get_cell_centre(from_cell)
    to_centre = get_cell_centre(to_cell)
    window.draw_line(Line(from_centre, to_centre), "gray" if undo else "red")

def get_cell_centre(cell):
    x = (cell.p1.x + cell.p2.x) / 2
    y = (cell.p1.y + cell.p2.y) / 2
    return Point(x, y)
