from graphics import *
from cell import *

def main():
    win = Window(800, 600)

    cells = [
        Cell(True, False, True, True, Point(50, 50), Point(100, 100)),
        Cell(False, True, True, False, Point(100, 50), Point(150, 100)),
        Cell(True, True, False, True, Point(100, 100), Point(150, 150))
    ]
    for cell in cells:
        cell.draw(win)
    draw_move(win, cells[0], cells[1])
    draw_move(win, cells[1], cells[2], undo=True)

    win.wait_for_close()

if __name__ == "__main__":
    main()
