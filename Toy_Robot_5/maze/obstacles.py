# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------this is the obstacles module

import random

obstacles = []

def generate_obstacles():
    """
    Generates a random number of obstacles at random positions within specified ranges.
    :return: List of obstacle positions as tuples.
    """
    global obstacles
    obstacles = []
    random_obstacles_num = random.randint(1, 10)

    for _ in range(random_obstacles_num):
        obstacles.append((random.randint(-100, 100), random.randint(-200, 200)))
    return obstacles


def is_position_blocked(x, y):
    """
    Checks if the given position (x, y) is blocked by any obstacles.
    :param x: X-coordinate of the position.
    :param y: Y-coordinate of the position.
    :return: True if the position is blocked, False otherwise.
    """
    for obstacle in obstacles:
        obstacle_x, obstacle_y = obstacle
        if x <= obstacle_x <= x + 4 and y <= obstacle_y <= y + 4:
            return True

    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Checks if the path from (x1, y1) to (x2, y2) is blocked by any obstacles.
    :param x1: X-coordinate of the starting point.
    :param y1: Y-coordinate of the starting point.
    :param x2: X-coordinate of the ending point.
    :param y2: Y-coordinate of the ending point.
    :return: True if the path is blocked, False otherwise.
    """
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if is_position_blocked(x, y1):
                return False
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if is_position_blocked(x1, y):
                return True
            
    return False


def run(robot_name):
    if is_path_blocked == True:
        print(f'{robot_name}: Sorry, there is an obstacle in the way.')
    else:
        pass


def get_obstacles():
    """
    Retrieves the list of obstacles.
    :return: List of obstacle positions as tuples.
    """
    return obstacles


def print_obstacles(robot_name):
    """
    Prints information about obstacles if there are any.
    """
    if obstacles != []:
        print(f'{robot_name}: Loaded obstacles.')
        print("There are some obstacles:")
        for obstacle in obstacles:
            new_obstacle = ''
            print(f"- At position {','.join(map(str, obstacle))} (to {obstacle[0] + 4},{obstacle[1] + 4})")

