# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """


    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType
        Initialize a Rat with its name and position.
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def get_location(self):
        """
        Get the present location of this rat
        :return: row, col
        """

        return self.row, self.col


    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType
        :param row:
        :param col:
        :return:
        """
        self.row = row
        self.col = col


    def eat_sprout(self):
        """ (Rat) -> NoneType
        Add one to the rat's intance variable.
        :return: NoneType
        """
        self.num_sprouts_eaten += 1


    def __str__(self):
        """
        Return a string representation of the rat in this format:
        Symbol at (row, col) ate num_sprounts_eaten sprounts.
        Eg.
        'J at (4, 3) ate 2 sprounts.'
        :return: str
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

    def __init__(self, maze_contents, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Initialization of a Maze
        :param maze_contents: (list of list of str)
        :param rat_1: the first rat in the maze
        :param rat_2: the second rat in the maze
        """
        self.maze = maze_contents
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for row in maze_contents:
            for col in row:
                if col == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze.
        :param row: int
        :param col: int
        :return: bool
        """
        return self.maze[row][col] == WALL

    def is_sprout(self, row, col):
        """

        :param row:
        :param col:
        :return:
        """
        return self.maze[row][col] == SPROUT

    def get_character(self, row, col):
        """
        Return the character in the maze at the given location.
        :param row:
        :param col:
        :return: a char in the maze given row and column
        """
        if (row, col) == self.rat_1.get_location():
            return self.rat_1.symbol
        elif (row, col) == self.rat_2.get_location():
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, ver, hor):
        """
        Move the rat in the given direction unless there is a wall in the way.
        Check for a Brussels sprout at the location and, if present:
            have the rat eat the Brussels sprout,
            make that location a HALL, and
            decrease the value that num_sprouts_left refers to by one.
            Return True if and only if there wasn't a wall in the way.
        :param rat:
        :param ver: a vertical movement
        :param hor: a horizontal movement
        :return:
        """
        row = rat.row + ver
        col = rat.col + hor
        if self.is_wall(row, col):
            return None
        else:
            rat.set_location(row, col)
            if self.is_sprout(row, col):
                rat.eat_sprout()
                self.maze[row][col] = HALL
                self.num_sprouts_left -= 1
            return True

    def __str__(self):
        """

        :return: a string representation of the maze, using the format shown in this example:
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        return_string = ''
        rows = len(self.maze)
        cols = len(self.maze[0])
        for row in range(rows):
            for col in range(cols):
                if (row, col) == self.rat_1.get_location():
                    return_string += self.rat_1.symbol
                elif (row, col) == self.rat_2.get_location():
                    return_string += self.rat_2.symbol
                else:
                    return_string += self.maze[row][col]
            return_string += '\n'

        return_string += str(self.rat_1)
        return_string += '\n'
        return_string += str(self.rat_2)

        return return_string