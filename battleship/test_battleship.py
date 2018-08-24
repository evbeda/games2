import unittest

from battleship.board import Board, board_states
from battleship.game import Game, game_states
from .player import Player


class test_battleship(unittest.TestCase):

    def test_shoot_water(self):
        board = Board()
        result = board.shoot(3, 3)
        self.assertEqual(result, "water")

    def test_shoot_sunked_1(self):
        board = Board()
        board.set_boat(1, 1, 1, "horizontal")
        result = board.shoot(1, 1)
        self.assertEqual(result, "sunked")

    def test_shoot_sunked_2(self):
        board = Board()
        result = []
        board.set_boat(0, 0, 2, "horizontal")
        for i in range(0, 2):
            result.append(board.shoot(0, i))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_31(self):
        board = Board()
        result = []
        board.set_boat(1, 2, 3, "vertical")
        for i in range(1, 4):
            result.append(board.shoot(i, 2))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_32(self):
        board = Board()
        result = []
        board.set_boat(5, 7, 3, "horizontal")
        for i in range(7, 10):
            result.append(board.shoot(5, i))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_4(self):
        board = Board()
        result = []
        result2 = []
        result3 = []
        board.set_boat(9, 5, 4, "horizontal")
        for i in range(5, 9):
            result.append(board.shoot(9, i))
        board.set_boat(0, 0, 3, "horizontal")
        for i in range(0, 1):
            result2.append(board.shoot(0, i))
        board.set_boat(4, 5, 3, "horizontal")
        for i in range(5, 8):
            result3.append(board.shoot(4, i))
        self.assertEqual(result[len(result) - 1], "sunked")
        self.assertEqual(result2[len(result2) - 1], "hit")
        self.assertEqual(result3[len(result3) - 1], "sunked")

    def test_shoot_sunked_5(self):
        board = Board()
        result = []
        board.set_boat(5, 5, 5, "vertical")
        for i in range(5, 10):
            result.append(board.shoot(i, 5))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_player_boards(self):
        player = Player()
        result = player.get_boards()
        self.assertEqual(len(result), 2)

    def test_game_players(self):
        game = Game()
        result = game.get_players()
        self.assertEqual(len(result), 2)

    def test_own_board_is_ready(self):
        p1 = Player()
        p1.fill_own_board()
        result = p1.board_own.state
        self.assertEqual(result, board_states[1])

    def test_game_state_init(self):
        game = Game()
        result = game.state
        self.assertEqual(result, game_states[0])

    def test_game_state_war(self):
        game = Game()
        game.player1.fill_own_board()
        game.player2.fill_own_board()
        result = game.is_ready_to_war()
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
