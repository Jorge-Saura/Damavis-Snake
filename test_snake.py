import unittest

import snake as spf

class TestSnake(unittest.TestCase):

    def test_1(self):
        
        board = [4, 3]
        snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
        depth = 3
        snakePathFinder = spf.SnakePathFinder(board,snake)
        self.assertEqual(snakePathFinder.get_all_paths(depth), 7)

    def test_2(self):
        
        board = [2, 3]
        snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
        depth = 10
        snakePathFinder = spf.SnakePathFinder(board,snake)
        self.assertEqual(snakePathFinder.get_all_paths(depth), 1)

    def test_3(self):
        
        board = [10, 10]
        snake =  [[5,5], [5,4], [4,4], [4,5]]
        depth = 4
        snakePathFinder = spf.SnakePathFinder(board,snake)
        self.assertEqual(snakePathFinder.get_all_paths(depth), 81)



if __name__ == "__main__":
    unittest.main()
