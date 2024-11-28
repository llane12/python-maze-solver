from graphics import *
from maze import *

def main():
    win = Window(800, 600)

    cell_width = 50
    line_colors = [ "black", "red", "green", "blue" ]
    i = 0
    for y in range(50, 500, cell_width):
        for x in range(50, 500, cell_width):
            cell = Cell(x % 50 == 0, y % 100 == 0, x % 100 == 0, y % 50 == 0, Point(x, y), Point(x + cell_width, y + cell_width))
            cell.draw(win, line_colors[i])
            i = (i + 1) % len(line_colors)

    win.wait_for_close()

if __name__ == "__main__":
    main()
