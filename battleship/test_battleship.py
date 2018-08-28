import unittest
from unittest.mock import patch

from battleship.board import Board
from battleship.game import GameBattleship
from .player import PlayerCPU, PlayerHuman
from .game import game_states, possible_turn


class test_battleship(unittest.TestCase):

    def setUp(self):
        self.game = GameBattleship()
        input_user = [
            '1, 1, 1, vertical',
            '1, 2, 2, vertical',
            '1, 3, 3, vertical',
            '1, 4, 3, vertical',
            '1, 5, 4, vertical',
            '1, 6, 5, vertical',
        ]
        board = Board()
        board_table = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 31, 32, 4, 5, 0, 0, 0],
            [0, 0, 2, 31, 32, 4, 5, 0, 0, 0],
            [0, 0, 0, 31, 32, 4, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 5, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board.board = board_table
        for single_input in input_user:
            self.game.play(single_input)
        self.game.player_cpu.board_own = board

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
        game = GameBattleship()
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
        game = GameBattleship()
        result = game.state
        self.assertEqual(result, 'init')

    def test_game_state_war(self):
        game = GameBattleship()
        input_user = [
            '1, 1, 1, vertical',
            '1, 2, 2, vertical',
            '1, 3, 3, vertical',
            '1, 4, 3, vertical',
            '1, 5, 4, vertical',
            '1, 6, 5, vertical',
        ]
        # Ir corriendo cada uno de los inputs del user
        for single_input in input_user:
            result = game.state
            self.assertEqual(result, 'init')
            game.play(single_input)

        result = game.state
        self.assertEqual(result, 'war')

    def test_turn_init_player(self):
        game = GameBattleship()
        result = game.check_state_message()
        self.assertEqual(result,
                         'pone el barco (x, y, boat, horizontal/vertical)')

    def test_turn_init_player_wrong_param_amount_of(self):
        game = GameBattleship()
        result = game.play('1, 1, 1, vertical, extrabadparam')
        self.assertEqual(result, 'error, mas parametros de los requeridos (4)')

    def test_turn_war_player(self):
        game = GameBattleship()
        result = game.play('1, 2, 1, vertical')
        self.assertTrue(result)

    def test_turn_war_player_wrong_param_letter(self):
        game = GameBattleship()
        result = game.play('A, B, 1, vertical')
        self.assertEqual(result, 'error')

    def test_turn_war_player_wrong_number(self):
        game = GameBattleship()
        result = game.play('10, 1, 1, vertical')
        self.assertFalse(result)

    def test_turn_war_player_wrong_param_amount_of(self):
        game = GameBattleship()
        game.state = 'war'
        result = game.play('1, 1, extrabadparam')
        self.assertEqual(result, 'error, mas parametros de los requeridos (2)')

    def test_game_war_player_can_sunk_boat_player_cpu(self):
        expected = 'Congratulations! You sunk a boat'
        result = self.game.play('1, 1')
        self.assertEqual(expected, result)

    def test_game_war_player_can_water_boat_player_cpu(self):
        expected = 'You only hit water! Try it again'
        result = self.game.play('0, 0')
        self.assertEqual(expected, result)

    def test_game_war_player_can_hit_boat_player_cpu(self):
        expected = 'You hit a boat'
        result = self.game.play('2, 2')
        self.assertEqual(expected, result)

    def test_game_dont_change_state(self):
        board_cpu = Board()
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        board_cpu.board = board
        self.game.player_cpu.board_own = board_cpu
        expected = self.game.state
        self.game.play('1, 2')
        self.assertEqual(expected, self.game.state)

    def test_game_dont_change_state_hit(self):
        board_cpu = Board()
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board_cpu.board = board
        self.game.player_cpu.board_own = board_cpu
        expected = self.game.state
        self.game.play('0, 0')
        self.assertEqual(expected, self.game.state)

    def test_game_change_state_hit(self):
        board_cpu = Board()
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        board_cpu.board = board
        self.game.player_cpu.board_own = board_cpu
        expected = self.game.state
        self.game.play('0, 0')
        self.assertNotEqual(expected, self.game.state)

    # @unittest.mock.patch('random.randint')
    # def test_game_change_state_cpu_hit(self, mock_randint):
    #         board_player = Board()
    #         board = [
    #             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         ]
    #         board_player.board = board
    #         self.game.player_human.board_own = board_player
    #         self.game.turn = possible_turn[1]
    #         mock_randint = 0
    #         self.game.play('')
    #         self.assertEqual(self.game.state, game_states[2])

    @unittest.mock.patch('random.randint')
    def test_game_check_cpu_hit(self, mock_randint):
            board_player = Board()
            board = [
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
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
            board_player.board = board
            self.game.player_human.board_own = board_player
            self.game.turn = 'cpu'
            mock_randint = 0
            self.game.play('')
            result = self.game.player_human.board_own.board[0][0]
            self.assertNotEqual(9, result)

    def test_player_cpu_pick_coordenate(self):
        cpu_player = PlayerCPU()
        coordenate = cpu_player.pick_coordenate()
        self.assertTrue(0 <= coordenate[0] < 10)
        self.assertTrue(0 <= coordenate[1] < 10)

    def test_doblehit(self):
        board_cpu = Board()
        board = [
            [31, 9, 31, 0, 0, 0, 0, 0, 0, 0],
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
        board_cpu.board = board
        result = board_cpu.shoot(0, 1)
        self.assertEqual(result, 'already shoot')


if __name__ == "__main__":
    unittest.main()
