from unittest.mock import patch
import unittest
from .game import Game


class TestGame(unittest.TestCase):
    def test_game_finished_true(self):
        game = Game("Lautaro", "Chino")
        game.player1.combinations = {
            'UNO': 1,
            'DOS': 2,
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        game.player2.combinations = {
            'UNO': 1,
            'DOS': 2,
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        self.assertTrue(game.finished())

    def test_game_finished_false(self):
        game = Game("Lautaro", "Chino")
        game.player1.combinations = {
            'UNO': '',
            'DOS': '',
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        game.player2.combinations = {
            'UNO': '',
            'DOS': '',
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
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

    def test_tirada_1(self):
        game = Game("Santi", "Beto")
        with unittest.mock.patch('random.randint', return_value=1):
            self.assertEqual(
                game.next_turn(),
                'Santi Tu tirada: [1, 1, 1, 1, 1] INGRESE CONSERVAR X, Y O ANOTAR CATEGORIA'
            )
        game.play('CONSERVAR 1')
        with unittest.mock.patch('random.randint', return_value=2):
            self.assertEqual(
                game.next_turn(),
                'Santi Tu tirada: [1, 2, 2, 2, 2] INGRESE CONSERVAR X, Y O ANOTAR CATEGORIA'
            )
        game.play('CONSERVAR 1')
        with unittest.mock.patch('random.randint', return_value=3):
            self.assertEqual(
                game.next_turn(),
                'Santi Tu tirada: [1, 3, 3, 3, 3] INGRESE CONSERVAR X, Y O ANOTAR CATEGORIA'
            )
        result = game.play('ANOTAR TRES')
        self.assertEqual(
            result,
            'ANOTADO EN: TRES PUNTAJE: 12'
        )
        self.assertEqual(
            game.player1.combinations['TRES'],
            12,
        )
        self.assertEqual(game.player1.tirada, 1)
        self.assertEqual(game.turno.name, 'Beto')


if __name__ == '__main__':
    unittest.main()
