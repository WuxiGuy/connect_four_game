"""
This program is to draw a checkerboard for Connect Four
which allows two users to play together. The program can
determine if the checkerboard has been fully filled or give
the winner when there is a row of four pieces in same type.
"""


class ConnectFour:

    def __init__(self):
        """
        give a list of lists which are lines of checkerboard
        :return: self.checkerboard
                self.piece_type: a list of strings which are
                                types of pieces
                self.piece: a string of piece
                self.position: a list of location of piece
        """

        board = []
        for row in range(6):
            board.append([])
            for column in range(7):
                board[row].append(' ')
        self.board = board
        self.piece_type = ['X', 'O']
        self.piece = 'S'
        self.position = [0, 0]
        self.moved_locations = []

    def add_piece(self, column):
        """
        Put a piece to the checkerboard
        :param column: an integer
        :return: self.checkerboard: a list of list
                self.piece: a string
                self.piece_type: a list of strings
                self.position: a list of integers
        """

        if type(column) is not int:
            raise ValueError("Input should be int.")
        if column not in range(0, 7):
            raise ValueError("Invalid number.")
        if self.board[0][column] != ' ':
            raise ValueError("This column is full.")
        if self.is_game_over() is True:
            raise ValueError("Game is over.")

        position = []
        board = self.board
        # a queue that give the type of piece which is going to move
        self.piece = self.piece_type.pop(0)
        self.piece_type.append(self.piece)

        for row in range(5, -1, -1):
            if board[row][column] == ' ':
                board[row][column] = self.piece
                position.append(row)
                position.append(column)
                self.position = position
                self.moved_locations.append(position)
                self.board = board
                return self.board, self.piece, self.piece_type, self.position

    def is_game_over(self):
        """
        Determine if the game is over when the checkerboard is full
        or get the winner.
        :return: True: when the game is over
                False: when the game is not over
        """

        if self.get_winner() in ['X', 'O']:
            return True
        else:
            board = self.board
            space_numbers = 42
            for row in range(6):
                for column in board[row]:
                    if column != ' ':
                        space_numbers -= 1
            if space_numbers == 0:
                return True
            else:
                return False

    def get_winner(self):
        """
        Determine if there is a winner, 'X' or 'O'
        :return: 'X': when winner is X holder
                'O': when winner is O holder
                None: when there is no winner in this round
        """

        vertical_positions = 0
        horizontal_positions = 0
        oblique_position_left = 0
        oblique_position_right = 0
        piece = self.piece
        board = self.board

        # Check if there are consecutive pieces in the vertical direction
        # Check lower level
        position = self.position
        for row in range(position[0], min(position[0] + 3, 5) + 1):
            if board[row][position[1]] == piece:
                vertical_positions += 1
                if vertical_positions == 4:
                    break
            else:
                vertical_positions = 0

        # Check if there are consecutive pieces in the horizontal direction
        for column in range(max(position[1] - 3, 0), min(position[1] + 3, 7)):
            if board[position[0]][column] == piece:
                horizontal_positions += 1
                if horizontal_positions == 4:
                    break
            else:
                horizontal_positions = 0

        # Make a list of all locations in the checkerboard
        locations_list = []
        for r in range(6):
            for c in range(7):
                locations_list.append([r, c])

        # Check if there are consecutive pieces from left up to right down
        locations = []
        row = position[0] - 3
        column = position[1] - 3
        for r in range(7):
            if [row, column] in locations_list:
                locations.append([row, column])
            row += 1
            column += 1
        for point in locations:
            if board[point[0]][point[1]] == piece:
                oblique_position_left += 1
                if oblique_position_left == 4:
                    break
            else:
                oblique_position_left = 0

        # Check if there are consecutive pieces from left down to right up
        locations = []
        row = position[0] + 3
        column = position[1] - 3
        for r in range(7):
            if [row, column] in locations_list:
                locations.append([row, column])
            row -= 1
            column += 1
        for point in locations:
            if board[point[0]][point[1]] == piece:
                oblique_position_right += 1
                if oblique_position_right == 4:
                    break
            else:
                oblique_position_right = 0

        if vertical_positions > 3 or horizontal_positions > 3 or \
                oblique_position_left > 3 or oblique_position_right > 3:
            return piece
        else:
            return None

    def undo(self):
        """
        Return the checkerboard to the previous status so that
        the holder can retry.
        :return: self.checkerboard: a list of lists| the status
                                of the checkerboard before the
                                holder chooses the column
                self.checkerboard: a string| the type of piece of
                                the holder who chooses to retry
        """

        positions_list = []
        for row in range(6):
            for column in self.board[row]:
                positions_list.append(column)
        if self.piece not in positions_list:
            raise ValueError("There is no piece to undo.")

        moved_positions = self.moved_locations
        position = moved_positions.pop()
        self.board[position[0]][position[1]] = ' '
        # Return the type of piece that choose to undo
        previous_piece = self.piece_type.pop(0)
        self.piece_type.append(previous_piece)
        return self.board

    def __str__(self):
        """
        Print out the checkerboard with pieces that have been put on it
        :return: output: a string of checkerboard
        """

        output = ''
        level_line = '-' * 15 + '\n'
        for row in range(6):
            for position in self.board[row]:
                output += '|' + position
            output += '|\n'
            output += level_line
        return output
