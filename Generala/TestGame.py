from unittest.mock import patch
import unittest
from .game import Game


class TestGame(unittest.TestCase):
    def test_game_finished_true(self):
        game = Game("Lautaro", "Chino")
        game.player1.combinations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'Escalera']
        game.player2.combinations = [1, 2, 3, 4, 5, 6, 'Generala', 8, 9, 'Full', 11, 12, 13]
        self.assertTrue(game.finished())

    def test_game_finished_false(self):
        game = Game("Lautaro", "Chino")
        game.player1.combinations = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'Escalera']
        game.player2.combinations = [2, 3, 4, 5, 6, 'Generala', 8, 9, 'Full', 11, 12, 13]
        self.assertFalse(game.finished())

    @unittest.mock.patch('builtins.input')
    @unittest.mock.patch('random.randint')
    def test_tirar_select_1(self, mock_rand_int, mock_input):
        mock_input.return_value = 1
        mock_rand_int.return_value = 1
        result = [1, 1, 1, 1, 1]
        game = Game("Chino", "Lautaro")
        game.tirar()
        self.assertEqual(game.dados, result)


if __name__ == '__main__':
    unittest.main()
