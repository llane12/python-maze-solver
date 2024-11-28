import unittest
from maze import Maze


class MazeTests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 3
        num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Entrance always top of top-left cell
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertTrue(maze._cells[0][0].has_left_wall)
        self.assertTrue(maze._cells[0][0].has_right_wall)
        self.assertTrue(maze._cells[0][0].has_bottom_wall)

        # Exit always bottom of bottom-right cell
        self.assertFalse(maze._cells[2][2].has_bottom_wall)
        self.assertTrue(maze._cells[2][2].has_left_wall)
        self.assertTrue(maze._cells[2][2].has_right_wall)
        self.assertTrue(maze._cells[2][2].has_top_wall)

if __name__ == "__main__":
    unittest.main()