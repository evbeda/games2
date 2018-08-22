import unittest
from unittest.mock import patch

from .carta import Carta
from .mazo import Mazo
from . import ESPADA, BASTO, ORO, COPA
from .player import Player
from .game import Game


class TestCartas (unittest.TestCase):
    # CREACIONES
    def test_si_se_crea_carta(self):
        carta1 = Carta(ESPADA, 1)
        self.assertIsInstance(carta1, Carta)
    # POSICIONES

    def test_obtener_posicion_cero(self):
        cartaMacho = Carta(ESPADA, 1)
        self.assertEqual(cartaMacho.get_position(), 0)

    def test_obtener_posicion_uno(self):
        cartaMacho = Carta(BASTO, 1)
        self.assertEqual(cartaMacho.get_position(), 1)

    def test_obtener_posicion_trece(self):
        cartaMacho = Carta(ESPADA, 4)
        self.assertEqual(cartaMacho.get_position(), 13)

    # COMPARACIONES
    def test_comparar_as_espadas_con_as_bastos(self):
        carta1 = Carta(ESPADA, 1)
        carta2 = Carta(BASTO, 1)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'GREATER')

    def test_comparar_4_de_espadas_con_4_de_bastos(self):
        carta1 = Carta(ESPADA, 4)
        carta2 = Carta(BASTO, 4)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'EQUAL')

    def test_comparar_7_de_espadas_con_7_de_bastos(self):
        carta1 = Carta(ESPADA, 7)
        carta2 = Carta(BASTO, 7)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'GREATER')

    def test_comparar_5_de_espadas_con_2_de_bastos(self):
        carta1 = Carta(ESPADA, 5)
        carta2 = Carta(BASTO, 2)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'LOWER')


class TestMazo(unittest.TestCase):
    def test_repartir_cartas_uno(self):
        mazo = Mazo()
        result = mazo.get_card()
        self.assertIsInstance(result, Carta)

    def test_repartir_dos_cartas_distintas(self):
        mazo = Mazo()
        result1 = mazo.get_card()
        result2 = mazo.get_card()
        self.assertNotEqual(result1, result2)

    def test_contar_cartas_del_mazo_repartiendo_dos(self):
        mazo = Mazo()
        mazo.get_card()
        mazo.get_card()
        self.assertEqual(len(mazo.mazo), 38)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Mazo()
        mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Carta('basto', 1)
        self.assertEqual(cartaCorrecta.suit, result2.suit)
        self.assertEqual(cartaCorrecta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_4(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Mazo()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Carta('oro', 7)
        self.assertEqual(cartaCorrecta.suit, result2.suit)
        self.assertEqual(cartaCorrecta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2_de_a_4(self, mock_rand_int):
        mock_rand_int.return_value = 4
        mazo = Mazo()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Carta('basto', 3)
        self.assertEqual(cartaCorrecta.number, result2.number)
        self.assertEqual(cartaCorrecta.suit, result2.suit)


class TestGame(unittest.TestCase):
    def test_deal_cards(self):
        # setup
        player01 = Player('1')
        player02 = Player('2')
        deck = Mazo()
        game = Game([player01, player02],deck )
        # test
        game.deal()
        # assert
        self.assertEqual(len(player01.cards), 3)
        self.assertEqual(len(player02.cards), 3)

if __name__ == '__main__':
    unittest.main()
