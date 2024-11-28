from graphics import Window
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_width = 800
    screen_height = 600
    cell_width = (screen_width - (2 * margin)) / num_cols
    cell_height = (screen_height - (2 * margin)) / num_rows
    win = Window(screen_width, screen_height)

    Maze(win, margin, margin, num_rows, num_cols, cell_width, cell_height)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
