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
    window = Window(screen_width, screen_height)

    maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height)
    maze.draw_cells(window)
    
    window.wait_for_close()

if __name__ == "__main__":
    main()
