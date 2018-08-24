from battleship.board import Board
from random import randint, choice
from . import orientation


class PlayerCPU(object):
    def __init__(self):
        self.board_own = Board()
        self.board_opponent = Board()

    def get_boards(self):
        return [self.board_own, self.board_opponent]

    # Llena el board con todos los barcos de forma random
    def fill_own_board(self):
        if self.board_own.state == 'empty':
            boats = [1, 2, 3, 3, 4, 5]
            i = 0
            while not self.board_own.is_ready_to_war():
                row = randint(0, 9)
                column = randint(0, 9)
                orientation_own = choice(orientation)
                is_possible = self.board_own.set_boat(
                    row, column, boats[i], orientation_own)
                if is_possible:
                    i += 1

            return True

        else:
            return False


class PlayerHuman(object):
    def __init__(self):
        self.board_own = Board()
        self.board_opponent = Board()

    def get_boards(self):
        return [self.board_own, self.board_opponent]

    def put_boat_own_board(self, row, column, boat, orientation_own):
        is_possible = self.board_own.set_boat(
            row, column, boat, orientation_own)
        if is_possible:
            return True
        else:
            return False
