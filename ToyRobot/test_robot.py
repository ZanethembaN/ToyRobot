import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import maze.obstacles as obstacles
import robot


class MyTestCase(unittest.TestCase):
    def test_step3_default_maze(self):

        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
There are some obstacles:
- At position 1,1 (to 5,5)""", output[:130])


        with captured_io(StringIO('HAL\nmazerun\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)

    def test_step5_mazerun_top(self):

        with captured_io(StringIO('HAL\nmazerun top\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)


    def test_step5_mazerun_left(self):

        with captured_io(StringIO('HAL\nmazerun left\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the left edge') > -1)

    def test_step5_mazerun_right(self):

        with captured_io(StringIO('HAL\nmazerun right\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the right edge') > -1)



    def test_replay_basic(self):
        with captured_io(StringIO('MERO\nforward 10\nforward 5\nreplay\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,10).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,15).
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,25).
 > MERO moved forward by 5 steps.
 > MERO now at position (0,30).
 > MERO replayed 2 commands.
 > MERO now at position (0,30).
MERO: What must I do next? MERO: Shutting down..""", output)


    def test_replay_twice(self):
        with captured_io(StringIO('MERO\nforward 10\nforward 5\nreplay\nreplay\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.maxDiff = None
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,10).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,15).
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,25).
 > MERO moved forward by 5 steps.
 > MERO now at position (0,30).
 > MERO replayed 2 commands.
 > MERO now at position (0,30).
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,40).
 > MERO moved forward by 5 steps.
 > MERO now at position (0,45).
 > MERO replayed 2 commands.
 > MERO now at position (0,45).
MERO: What must I do next? MERO: Shutting down..""", output)

    def test_replay_silent(self):
        with captured_io(StringIO('MERO\nforward 10\nforward 5\nreplay silent\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,10).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,15).
MERO: What must I do next?  > MERO replayed 2 commands silently.
 > MERO now at position (0,30).
MERO: What must I do next? MERO: Shutting down..""", output)

  

    def test_replay_reversed(self):
        with captured_io(StringIO('MERO\nforward 10\nforward 5\nreplay reversed\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,10).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,15).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,20).
 > MERO moved forward by 10 steps.
 > MERO now at position (0,30).
 > MERO replayed 2 commands in reverse.
 > MERO now at position (0,30).
MERO: What must I do next? MERO: Shutting down..""", output)

  

    def test_replay_silent_reversed(self):
        with captured_io(StringIO('MERO\nforward 10\nforward 5\nreplay reversed silent\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,10).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,15).
MERO: What must I do next?  > MERO replayed 2 commands in reverse silently.
 > MERO now at position (0,30).
MERO: What must I do next? MERO: Shutting down..""", output)



    def test_replay_silent_reversed_invalid(self):
        with captured_io(StringIO('MERO\nforward 10\nforward 5\nreplay REVERSED,SILENT\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 10 steps.
 > MERO now at position (0,10).
MERO: What must I do next?  > MERO moved forward by 5 steps.
 > MERO now at position (0,15).
MERO: What must I do next? MERO: Sorry, I did not understand 'replay REVERSED,SILENT'.
MERO: What must I do next? MERO: Shutting down..""", output)

   

    def test_replay_range_basic_reversed(self):
        with captured_io(StringIO('MERO\nforward 3\nforward 2\nforward 1\nreplay 2 reversed\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? MERO: Hello kiddo!
MERO: What must I do next?  > MERO moved forward by 3 steps.
 > MERO now at position (0,3).
MERO: What must I do next?  > MERO moved forward by 2 steps.
 > MERO now at position (0,5).
MERO: What must I do next?  > MERO moved forward by 1 steps.
 > MERO now at position (0,6).
MERO: What must I do next?  > MERO moved forward by 2 steps.
 > MERO now at position (0,8).
 > MERO moved forward by 3 steps.
 > MERO now at position (0,11).
 > MERO replayed 2 commands in reverse.
 > MERO now at position (0,11).
MERO: What must I do next? MERO: Shutting down..""", output)

  
if __name__ == '__main__':
    unittest.main()
