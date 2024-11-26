from graphics import *

def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(10, 10), Point(10, 100)), "red")
    win.draw_line(Line(Point(10, 10), Point(100, 10)), "green")
    win.draw_line(Line(Point(10, 100), Point(100, 100)), "blue")
    win.draw_line(Line(Point(100, 10), Point(100, 100)), "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()
