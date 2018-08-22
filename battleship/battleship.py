

class Board(object):
    def __init__(self):
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

    def set_boat(self, row, column, value, orientation):
        if (
            (column >= 0 and column < 10) and
            (row >= 0 and row < 10) and
            self.check_position(row, column, value, orientation)
        ):
            if (orientation == "horizontal") and ((value + column) <= 10):
                for index in range(0, value):
                    self.board[row][column + index] = value
                return True
            elif (orientation == "vertical") and ((value + row) <= 10):
                for index in range(0, value):
                    self.board[row + index][column] = value
                return True
        else:
            return False

    def check_position(self, row, column, value, orientation):
        if (column >= 0 and column < 10) and (row >= 0 and row < 10):
            if (orientation == "horizontal") and ((value + column) <= 10):
                for index in range(0, value):
                    if self.board[row][column + index] != 0:
                        return False
                return True
            elif (orientation == "vertical") and ((value + row) <= 10):
                for index in range(0, value):
                    if self.board[row + index][column] != 0:
                        return False
                return True
        else:
            return False