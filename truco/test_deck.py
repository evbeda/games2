import unittest
from unittest.mock import patch

from .card import Card
from .deck import Deck
from . import SWORD, COARSE, GOLD, CUP
from .player import Player
from .game import Game


class TestDeck(unittest.TestCase):
    def test_repartir_cartas_uno(self):
        mazo = Deck()
        result = mazo.get_card()
        self.assertIsInstance(result, Card)

    def test_repartir_dos_cartas_distintas(self):
        mazo = Deck()
        result1 = mazo.get_card()
        result2 = mazo.get_card()
        self.assertNotEqual(result1, result2)

    def test_contar_cartas_del_mazo_repartiendo_dos(self):
        mazo = Deck()
        mazo.get_card()
        mazo.get_card()
        self.assertEqual(len(mazo.ordered_deck), 38)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Deck()
        mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Card('basto', 1)
        self.assertEqual(cartaCorrecta.suit, result2.suit)
        self.assertEqual(cartaCorrecta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_4(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Deck()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Card('oro', 7)
        self.assertEqual(cartaCorrecta.suit, result2.suit)
        self.assertEqual(cartaCorrecta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2_de_a_4(self, mock_rand_int):
        mock_rand_int.return_value = 4
        mazo = Deck()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Card('basto', 3)
        self.assertEqual(cartaCorrecta.number, result2.number)
        self.assertEqual(cartaCorrecta.suit, result2.suit)

    def test_states(self):
        player01 = Player('1')
        player02 = Player('2')
        deck = Deck()
        game = Game([player01, player02], deck)
        game.deal()
        self.assertEqual(game.get_state(), [0, None, None, None, None])
