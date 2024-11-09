# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------


import turtle
import random
import world.text.world as worldtext
import maze.obstacles as mazeobstacles
import robot as main_robot

turtle1= turtle.Turtle()
turtle1.shape('square')

def draw_barrier(x,y):
    turtle.penup()
    turtle.speed(100)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(500) 
        turtle.left(90)
    turtle.hideturtle()


def move_turtle():
    """
    Moves the turtle to the current position of the robot.
    """
    turtle1.speed(0)
    turtle1.penup()
    turtle1.goto(worldtext.position_x, worldtext.position_y)
    turtle1.pendown()


def draw_random_square():
    """
#     Draws a random square for each obstacle on the screen.
#     """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for obstacle in mazeobstacles.obstacles:
        t.color(random.random(), random.random(), random.random())
        t.begin_fill()
        t.penup()
        t.goto(obstacle[0], obstacle[1])
        t.pendown()
        square_size = 20 
        for _ in range(4):
            t.forward(square_size)
            t.right(90)

