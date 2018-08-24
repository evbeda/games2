import unittest

from battleship.board import Board
from battleship.game import Game
from .player import PlayerCPU, PlayerHuman


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
        player = PlayerHuman()
        result = player.get_boards()
        self.assertEqual(len(result), 2)

    def test_game_players(self):
        game = Game()
        result = game.get_players()
        self.assertEqual(len(result), 2)

    def test_own_board_is_ready_cpu(self):
        p1 = PlayerCPU()
        p1.fill_own_board()
        result = p1.board_own.state
        self.assertEqual(result, 'ready_to_war')

    # def test_own_board_is_ready_human(self):
    #     p1 = PlayerHuman()
    #     p1.fill_own_board()
    #     result = p1.board_own.state
    #     self.assertEqual(result, board_states[1])

    def test_game_state_init(self):
        game = Game()
        result = game.state
        self.assertEqual(result, 'init')

    # def test_game_state_war(self):
    #     game = Game()
    #     game.player_cpu.fill_own_board()
    #     game.player_human.fill_own_board()
    #     result = game.is_ready_to_war()
    #     self.assertTrue(result)

    def test_turn_initial(self):
        game = Game()
        result = game.turn
        self.assertEqual(result, 'human')

    def test_turn_change(self):
        game = Game()
        game.change_turn()
        result = game.turn
        self.assertEqual(result, 'cpu')

    def test_turn_init_player(self):
        game = Game()
        result = game.check_state_message()
        self.assertEqual(result, 'pone el barco (x, y, boat, hor/ver)')

    def test_turn_war_player(self):
        game = Game()
        result = game.play('1, 2, 1, vertical')
        self.assertTrue(result)

    def test_turn_war_player_wrong_param(self):
        game = Game()
        result = game.play('A, B, 1, vertical')
        self.assertEqual(result, 'error')

    def test_turn_war_player_wrong_number(self):
        game = Game()
        result = game.play('10, 1, 1, vertical')
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
