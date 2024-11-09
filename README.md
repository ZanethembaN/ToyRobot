Toy Robot Simulator
This project simulates the movement of a toy robot in a 2D grid environment. The robot can respond to user commands such as forward, backward, turn left, turn right, and status, while handling obstacles and checking if it can move to the requested position. If the robot encounters an obstacle, it will stop and print a message indicating the obstacle's position.

Features
Move the robot forward and backward in four directions: NORTH, EAST, SOUTH, and WEST.
Turn the robot left or right by 90 degrees.
Place obstacles on the grid that the robot cannot move through.
The robot will stop and print a message if it encounters an obstacle or tries to move out of bounds.
Supports additional robot commands like status to get the robot's current position and facing direction.
Requirements
Python 3.x
Installation
Clone the repository to your local machine:

bash
Copy code
git clone [https://github.com/yourusername/toy-robot-simulator.git](https://github.com/ZanethembaN/ToyRobot.git)
Navigate to the project directory:

bash
Copy code
cd toy-robot-simulator
Run the toy_robot.py script using Python:

bash
Copy code
python toy_robot.py
Usage
Example:
python
Copy code
# Create a ToyRobot object in a 5x5 grid, starting at (0, 0)
robot = ToyRobot(grid_size=(5, 5), start_position=(0, 0))

# Place obstacles at specific positions
robot.place_obstacle(2, 0)  # Obstacle at (2, 0)
robot.place_obstacle(3, 1)  # Obstacle at (3, 1)

# Move the robot and observe behavior
robot.status()  # Print the current state of the robot
robot.move_forward(3)  # Try moving forward 3 steps (will stop at obstacle at (2, 0))
robot.turn_right()  # Turn the robot right (now facing EAST)
robot.move_backward(2)  # Try moving backward 2 steps (will stop at obstacle at (3, 1))
robot.move_forward(2)  # Move freely without hitting an obstacle
robot.status()  # Final robot position
Available Commands:
Move Forward: move_forward(steps) – Move the robot forward by a specified number of steps. If there is an obstacle, the robot will stop and print an error message.

Move Backward: move_backward(steps) – Move the robot backward by a specified number of steps. Similar to moving forward, it will stop if an obstacle is encountered.

Turn Left: turn_left() – Turn the robot 90 degrees counterclockwise (e.g., from NORTH to WEST).

Turn Right: turn_right() – Turn the robot 90 degrees clockwise (e.g., from NORTH to EAST).

Status: status() – Print the current position and direction of the robot (e.g., Robot is at (2, 1), facing EAST.).

Place Obstacle: place_obstacle(x, y) – Place an obstacle at the specified (x, y) position on the grid.

Move: move(direction, steps) – A generic command that allows you to move in a given direction (either 'forward' or 'backward') for a specified number of steps. This can be used in place of the move_forward() and move_backward() methods.

