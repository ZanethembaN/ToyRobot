import unittest
from unittest.mock import patch
import maze.obstacles as mazeobstacles


class TestObstacleFunctions(unittest.TestCase):

    @patch('random.randint', return_value=5) 
    def test_generate_obstacles(self, randint_mock):
        obstacles = mazeobstacles.generate_obstacles()
        self.assertEqual(len(obstacles), 5) 

    def test_is_position_blocked(self):
        mazeobstacles.obstacles = [(1, 1), (3, 3)] 
        self.assertTrue(mazeobstacles.is_position_blocked(2, 2))
        self.assertFalse(mazeobstacles.is_position_blocked(5, 5))


if __name__ == '__main__':
    unittest.main()