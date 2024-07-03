import turtle
import random
from collections import deque
# try:
#     import world.turtle.world as worldturtle
# except ModuleNotFoundError as error:
#     pass



GRID_SIZE = 20
CELL_SIZE = 20


maze = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(CELL_SIZE / 20)
my_turtle.penup()
my_turtle.speed(0)  

def draw_square(x, y):
    """Draw a square at the given coordinates."""
    turtle.tracer(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.penup()

def create_maze():
    """Create a maze with random walls."""
    for i in range(-GRID_SIZE // 2, GRID_SIZE // 2):
        for j in range(-GRID_SIZE // 2, GRID_SIZE // 2):
            if random.random() < 0.3: 
                draw_square(i * CELL_SIZE, j * CELL_SIZE)
                maze[i + GRID_SIZE // 2][j + GRID_SIZE // 2] = 1  

def bfs(start, end):
    """Breadth-First Search to find the shortest path."""
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path + [current]

        if current not in visited:
            visited.add(current)

            x, y = current
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for neighbor in neighbors:
                if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE and maze[neighbor[0]][neighbor[1]] == 0:
                    queue.append((neighbor, path + [current]))

    return None

def main():
    create_maze()
    start_point = (-GRID_SIZE // 2, -GRID_SIZE // 2)
    end_point = (GRID_SIZE // 2, GRID_SIZE // 2)
    path = bfs(start_point, end_point)

    if path:

        turtle.pencolor("red")
        for point in path:
            draw_square(point[0] * CELL_SIZE, point[1] * CELL_SIZE)

    turtle.hideturtle()
    turtle.mainloop()

main()