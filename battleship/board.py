board_states = ['empty', 'ready_to_war', 'in_war']


class Board(object):

    def __init__(self):
        self.sunked = []
        self.boats = [0, 0, 0, 0, 0, 0]
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.state = board_states[0]

    def get_board(self):
        return self.board

    def set_boat(self, row, column, boat, orientation):
        if (
                (column >= 0 and column < 10) and
                (row >= 0 and row < 10) and
                self.check_position(row, column, boat, orientation)
        ):
            if (orientation == "horizontal") and ((boat + column) <= 10):
                value = self.check_boat(boat)
                for index in range(0, boat):
                    self.board[row][column + index] = value
                return True
            elif (orientation == "vertical") and ((boat + row) <= 10):
                value = self.check_boat(boat)
                for index in range(0, boat):
                    self.board[row + index][column] = value
                return True
        else:
            return False

    def check_boat(self, boat):
        sum_boats = 0
        if boat == 1:
            self.boats[0] = 1
            return 1
        elif boat == 2:
            self.boats[1] = 1
            return 2
        elif boat == 3:
            if self.boats[2] == 0:
                self.boats[2] = 1
                return 31
            else:
                self.boats[3] = 1
                return 32
        elif boat == 4:
            self.boats[4] = 1
            return 4
        elif boat == 5:
            self.boats[5] = 1
            return 5
        for i in range(0, len(self.boats) - 1):
            sum_boats += self.boats[i]
        if sum_boats == 6:
            self.boats = [0, 0, 0, 0, 0]

    def check_position(self, row, column, boat, orientation):
        if (column >= 0 and column < 10) and (row >= 0 and row < 10):
            if (orientation == "horizontal") and ((boat + column) <= 10):
                for index in range(0, boat):
                    if self.board[row][column + index] != 0:
                        return False
                return True
            elif (orientation == "vertical") and ((boat + row) <= 10):
                for index in range(0, boat):
                    if self.board[row + index][column] != 0:
                        return False
                return True
        else:
            return False

    def check_cross(self, value):
        self.sunked.append(value)
        if value == 1:
            return "sunked"
        elif value == 2:
            if self.sunked.count(value) == 2:
                return "sunked"
            else:
                return "hit"
        elif value == 31:
            if self.sunked.count(value) == 3:
                return "sunked"
            else:
                return "hit"
        elif value == 32:
            if self.sunked.count(value) == 3:
                return "sunked"
            else:
                return "hit"
        elif value == 4:
            if self.sunked.count(value) == 4:
                return "sunked"
            else:
                return "hit"
        elif value == 5:
            if self.sunked.count(value) == 5:
                return "sunked"
            else:
                return "hit"

    def shoot(self, row, column):
        if self.board[row][column] == 0:
            return "water"
        elif self.board[row][column] == 9:
            return "already shoot"
        elif self.board[row][column] != 0 and self.board[row][column] != 9:
            result = self.check_cross(self.board[row][column])
            self.board[row][column] = 9
            return result

    def turn_decision_hit(self, result):
        if result == 'hit':
            return True
        return False

    def is_ready_to_war(self):
        if self.boats == [1, 1, 1, 1, 1, 1, ]:
            self.state = board_states[1]
            return True
        else:
            return False

    def mark_shoot(self, row, column, is_hit):
        if self.board[row][column] == 0:
            if is_hit:
                character = 'x'
            else:
                character = '-'
            self.board[row][column] = character

    def there_are_boats(self):
        for i in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[i][x] != 0 and self.board[i][x] != 9:
                    return True
        return False
