import unittest
from unittest.mock import patch
import world.text.world as worldtext

class TestWorldTextWorld(unittest.TestCase):

    
    def test_is_position_allowed(self):
        self.assertTrue(worldtext.is_position_allowed(50, 100))
        self.assertFalse(worldtext.is_position_allowed(-150, 250))

    def test_update_position(self):
        worldtext.position_x, worldtext.position_y = 0, 0
        self.assertTrue(worldtext.update_position(10))
        self.assertEqual(worldtext.position_x, 0)
        self.assertEqual(worldtext.position_y, 10)

    @patch('world.text.world.is_position_allowed', return_value=True)
    def test_do_forward_allowed(self, mock_position_allowed):
        result, output = worldtext.do_forward('HAL', 5)
        self.assertTrue(result)
        self.assertEqual(output, ' > HAL moved forward by 5 steps.')

  

    @patch('world.text.world.update_position', return_value=True)
    def test_do_back_allowed(self, mock_update_position):
        result, output = worldtext.do_back('HAL', 5)
        self.assertTrue(result)
        self.assertEqual(output, ' > HAL moved back by 5 steps.')

    @patch('world.text.world.update_position', return_value=False)
    def test_do_back_obstacle(self, mock_update_position):
        result, output = worldtext.do_back('HAL', 5)
        self.assertTrue(result)
        self.assertEqual(output, 'HAL: Sorry, I cannot go outside my safe zone.')

    def test_do_right_turn(self):
        result, output = worldtext.do_right_turn('HAL')
        self.assertTrue(result)
        self.assertEqual(output, ' > HAL turned right.')

    def test_do_left_turn(self):
        result, output = worldtext.do_left_turn('HAL')
        self.assertTrue(result)
        self.assertEqual(output, ' > HAL turned left.')


if __name__ == '__main__':
    unittest.main()