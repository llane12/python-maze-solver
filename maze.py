from graphics import *

class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, p1, p2):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._p1 = p1
        self._p2 = p2

    def draw(self, window, line_color):
        if self.has_left_wall:
            window.draw_line(Line(Point(self._p1.x, self._p1.y), Point(self._p1.x, self._p2.y)), line_color)
        if self.has_right_wall:
            window.draw_line(Line(Point(self._p2.x, self._p1.y), Point(self._p2.x, self._p2.y)), line_color)
        if self.has_top_wall:
            window.draw_line(Line(Point(self._p1.x, self._p1.y), Point(self._p2.x, self._p1.y)), line_color)
        if self.has_bottom_wall:
            window.draw_line(Line(Point(self._p1.x, self._p2.y), Point(self._p2.x, self._p2.y)), line_color)
