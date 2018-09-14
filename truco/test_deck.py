import unittest

from .card import Card
from .deck import Deck


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
        carta_correcta = Card('basto', 1)
        self.assertEqual(carta_correcta.suit, result2.suit)
        self.assertEqual(carta_correcta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_4(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Deck()
        mazo.get_card()
        mazo.get_card()
        mazo.get_card()
        result2 = mazo.get_card()
        carta_correcta = Card('oro', 7)
        self.assertEqual(carta_correcta.suit, result2.suit)
        self.assertEqual(carta_correcta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2_de_a_4(self, mock_rand_int):
        mock_rand_int.return_value = 4
        mazo = Deck()
        mazo.get_card()
        result2 = mazo.get_card()
        carta_correcta = Card('basto', 3)
        self.assertEqual(carta_correcta.number, result2.number)
        self.assertEqual(carta_correcta.suit, result2.suit)
