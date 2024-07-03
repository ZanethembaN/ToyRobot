# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------this is robot.py module responsible for running the whole program


def robot_start():
    """
    Replace me!
    """
import maze.obstacles as mazeobstacles

import sys

if "maze" in sys.argv:
    import maze.maze_runner as mazerunner
if "turtle" in sys.argv:
    import world.turtle.world as worldturtle
else:
    import world.text.world as worldtext


# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint','mazerun']
move_commands = valid_commands[3:]

# commands history
history = []

argv = sys.argv

if len(argv) >2 and 'turtle' in argv:
    from world.turtle.world import *
    import world.turtle.world as worldturtle
else:
    import world.text.world as worldtext

def get_robot_name():
    """
    Asks the user for the robot's name.
    :return: The name given to the robot.
    """
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name



def get_command(robot_name):
    """
    Asks the user for a command and validates it.
    :param robot_name: The name of the robot.
    :return: The validated command.
    """
    prompt = '' + robot_name + ': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '" + command + "'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, getting the command and its argument(s).
    :param command: The input command.
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int.
    :param value: The string value to test.
    :return: True if it is an int, False otherwise.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Checks if the robot can understand the command.
    :param command: The input command.
    :return: True if the command is valid, False otherwise.
    """
    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(
                arg1.lower().replace('silent', '').replace('reversed', '').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed', '')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or arg1.lower() == 'top' or arg1.lower() == 'bottom' or arg1.lower() == 'left' or arg1.lower() == 'right' or is_int(arg1))


def output(name, message):
    """
    Prints the output message.
    :param name: The name of the robot.
    :param message: The message to print.
    """
    print('' + name + ": " + message)


def do_help():
    """
    Provides help information to the user.
    :return: (True, help text) to indicate the robot can continue after this command was handled.
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""


def do_sprint(robot_name, steps):
    """
    Sprints the robot.
    :param robot_name: The name of the robot.
    :param steps: The number of steps to sprint.
    :return: (True, forward output)
    """

    if steps == 1:
        return worldtext.do_forward(robot_name, 1)
    else:
        (do_next, command_output) = worldtext.do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieves the commands from history list, breaking them up into (command_name, arguments) tuples.
    :param reverse: If True, then reverse the list.
    :param relativeStart: The start index relative to the end position of the command.
    :param relativeEnd: The end index relative to the end position of the command.
    :return: List of (command_name, arguments) tuples.
    """

    commands_to_replay = [(name, args) for (name, args) in
                          list(map(lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (
            relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if (
            relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(
        commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments):
    """
    Replays historic commands.
    :param robot_name: The name of the robot.
    :param arguments: A string containing arguments
    for the replay command.
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(command_name, command_arg, robot_name)
        if not silent:
            print(command_output)
            worldtext.show_position(robot_name)

    return True, ' > ' + robot_name + ' replayed ' + str(len(commands_to_replay)) + ' commands' + (
        ' in reverse' if reverse else '') + (' silently.' if silent else '.')


def mazerun(robot_name, edge = 'top'):
    print(f'starting maze run..')
    return  f'I am at the {edge} edge'



def mazerun_top(robot_name, edge='top'):
    """
    Executes the maze run to the specified edge.
    :param robot_name: The name of the robot.
    :param edge: The specified edge ('top').
    """
    print(f'starting maze run..')
    return  f'I am at the {edge} edge'


def mazerun_bottom(robot_name, edge='bottom'):
    """
    Executes the maze run to the specified edge.
    :param robot_name: The name of the robot.
    :param edge: The specified edge ('bottom').
    """
    print(f'starting maze run..')
    return  f'I am at the {edge} edge'

def mazerun_left(robot_name, edge='left'):
    """
    Executes the maze run to the specified edge.
    :param robot_name: The name of the robot.
    :param edge: The specified edge ('left').
    """
    print(f'starting maze run..')
    return f'I am at the {edge} edge'


def mazerun_right(robot_name, edge='right'):
    """
    Executes the maze run to the specified edge.
    :param robot_name: The name of the robot.
    :param edge: The specified edge ('right').
    """
    print(f'starting maze run..')
    return f'I am at the {edge} edge'


def call_command(command_name, command_arg, robot_name):
    """
    Calls the appropriate command based on the command name.
    :param command_name: The name of the command.
    :param command_arg: The arguments for the command.
    :param robot_name: The name of the robot.
    :return: (True, output string)
    """

    if command_name == 'help':
        return do_help()
    elif command_name == 'forward':
        return worldtext.do_forward(robot_name, int(command_arg))
    elif command_name == 'back':
        return worldtext.do_back(robot_name, int(command_arg))
    elif command_name == 'right':
        return worldtext.do_right_turn(robot_name)
    elif command_name == 'left':
        return worldtext.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return do_sprint(robot_name, int(command_arg))
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg)
    
    
    elif command_name.startswith('maze'):
    
        if command_name == 'mazerun' and (command_arg =='top'):
            return True,mazerun_top(robot_name)
        
        elif command_name == 'mazerun' and (command_arg =='bottom'):
            return  True,mazerun_bottom(robot_name)
        
        elif command_name == 'mazerun' and (command_arg =='left'):
            return  True,mazerun_left(robot_name)                             

        elif command_name == 'mazerun' and (command_arg =='right'):
            return  True,mazerun_right(robot_name)
        
        elif command_name == 'mazerun':
            return True, mazerun(robot_name)
        

    return False, None


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: The name given to the robot.
    :param command: The command entered by the user.
    :return: `True` if the robot must continue after the command, or else `False` if the robot must shutdown.
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name)

    print(command_output)
    worldtext.show_position(robot_name)
    add_to_history(command)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands.
    :param command: The command to add to the history.
    """
    history.append(command)



def robot_start():
    """This is the entry point for starting my robot"""

    global history

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")



    if mazeobstacles.generate_obstacles():
        try:
            worldturtle.draw_barrier(-180,-250)
            
            worldturtle.draw_random_square()
        except:
            pass

        mazeobstacles.print_obstacles(robot_name)

    worldtext.position_x = 0
    worldtext.position_y = 0
    worldtext.current_direction_index = 0
    history = []

    mazeobstacles.generate_obstacles()

    # mazerun(robot_name)#remove


    command = get_command(robot_name)
    while handle_command(robot_name, command):
        try:
            worldturtle.move_turtle()
        except:
            pass

        command = get_command(robot_name)
        mazeobstacles.run(robot_name)
       

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
