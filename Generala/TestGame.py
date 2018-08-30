from unittest.mock import patch
import unittest
from .game import Game


class TestGame(unittest.TestCase):
    def test_game_finished_true(self):
        game = Game("Santi", "Beto")
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

    def test_game_finished_p1_false(self):
        game = Game("Santi", "Beto")
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

    def test_game_finished_p2_false(self):
        game = Game("Santi", "Beto")
        game.player1.combinations = {
            'UNO': 3,
            'DOS': 4,
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
        game = Game("Santi", "Beto")
        game.next_turn()
        game.throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(game.throw.dice, result)

    @unittest.mock.patch('builtins.input')
    @unittest.mock.patch('random.randint')
    def test_next_turn_possible(self, mock_rand_int, mock_input):
        mock_input.return_value = 1
        mock_rand_int.return_value = 1
        result = [1, 1, 1, 1, 1]
        game = Game("Santi", "Beto")
        game.throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(game.next_turn(), '{}\nTu tirada: {} \nIngrese CONSERVAR X, ANOTAR CATEGORIA\
 o TIRAR YA\nx'.format(
            game.turno.name,
            game.throw.dice,
        ))

    @unittest.mock.patch('builtins.input')
    @unittest.mock.patch('random.randint')
    def test_next_turn_not_possible(self, mock_rand_int, mock_input):
        mock_input.return_value = 1
        mock_rand_int.return_value = 1
        game = Game("Santi", "Beto")
        game.throw.roll([0, 1, 2, 3, 4, ])
        game.throw.number = 5
        result = game.next_turn()
        self.assertEqual(result, '{}\nTu tirada: {} \nElija la categoria\n\
                 que desea llenar (Ej: POKER, GENERALA, ETC.)'.format(game.turno.name, game.throw.dice,))

    def test_conservar_1(self):
        game = Game("Santi", "Beto")
        game.throw.dice = [3, 5, 2, 4, 2]
        game.play('CONSERVAR', '1')
        # with unittest.mock.patch('random.randint', return_value=2):
        #     self.assertEqual(
        #         game.next_turn(),
        #         'Santi Tu tirada: [1, 2, 2, 2, 2] INGRESE CONSERVAR X, Y O ANOTAR CATEGORIA'
        #     )
        self.assertEqual(game.throw.dice[1], 5)

    @unittest.mock.patch('builtins.input')
    @unittest.mock.patch('random.randint')
    def test_tirar_ya(self, mock_rand_int, mock_input):
        mock_input.return_value = 1
        mock_rand_int.return_value = 1
        game = Game("Santi", "Beto")
        game.throw.dice = [3, 5, 2, 4, 2]
        game.play('TIRAR', 'YA')
        self.assertEqual(game.throw.dice, [1, 1, 1, 1, 1])

    @unittest.mock.patch('builtins.input')
    @unittest.mock.patch('random.randint')
    def test_anotar_generala(self, mock_rand_int, mock_input):
        mock_input.return_value = 1
        mock_rand_int.return_value = 1
        game = Game("Santi", "Beto")
        game.throw.dice = [1, 1, 1, 1, 1]
        game.throw.number = 2
        game.play('ANOTAR', 'GENERALA')
        self.assertEqual(game.player1.score, 50)
        game.play('ANOTAR', 'POKER')
        #import ipdb; ipdb.set_trace()
        self.assertEqual(
            game.play('ANOTAR', 'GENERALA'),
            'Categoria ya asignada'
        )

    def test_random_comand(self):
        game = Game("Santi", "Beto")
        self.assertEqual(
            game.play('HOLAQUETAL', 'POKER'),
            'Ingrese ANOTAR (TIRADA), CONSERVAR (1,2..), o TIRAR',
        )

    def test_board(self):
        game = Game("Santi", "Beto")
        self.assertEqual(
            game.board(),
            'Santi TIENE 0 PUNTOS \nBeto TIENE 0 PUNTOS\nRONDA 1',
        )


if __name__ == '__main__':
    unittest.main()
