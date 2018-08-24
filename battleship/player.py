from battleship.board import Board


class Player(object):
    def __init__(self):
        self.board_own = Board()
        self.board_opponent = Board()

    def get_boards(self):
        return [self.board_own, self.board_opponent]

    def fill_own_board(self):
        if self.board_own.state == 'empty':
            self.board_own.set_boat(0, 0, 1, "vertical")
            self.board_own.set_boat(0, 1, 2, "vertical")
            self.board_own.set_boat(0, 2, 3, "vertical")
            self.board_own.set_boat(0, 5, 3, "vertical")
            self.board_own.set_boat(0, 3, 4, "vertical")
            self.board_own.set_boat(0, 4, 5, "vertical")
            if self.board_own.is_ready_to_war():
                return True
            else:
                return False
        else:
            return False
