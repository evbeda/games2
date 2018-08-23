

class Board(object):
    def __init__(self):
        self.sunked = []
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

    def get_board(self):
        return self.board

    def set_boat(self, row, column, value, boat, orientation):
        if (
            (column >= 0 and column < 10) and
            (row >= 0 and row < 10) and
            self.check_position(row, column, boat, orientation)
        ):
            if (orientation == "horizontal") and ((boat + column) <= 10):
                for index in range(0, boat):
                    self.board[row][column + index] = value
                return True
            elif (orientation == "vertical") and ((boat + row) <= 10):
                for index in range(0, boat):
                    self.board[row + index][column] = value
                return True
        else:
            return False

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
        elif self.board[row][column] != 0:
            result = self.check_cross(self.board[row][column])
            self.board[row][column] = 9
            return result
