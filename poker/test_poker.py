import unittest
from .poker import *
from .card import Card
from .deck import Deck


class PokerTest(unittest.TestCase):
    def test_escaleraReal(self):
        # test
        result = encontrarEscaleraReal(['Ah', 'Kh', 'Qh', 'Jh', 'Th'])
        # assert
        self.assertTrue(result)

    def test_pares(self):
        # setup
        expected = {
            'poker': [],
            'trio': [],
            'par': ['3'],
        }
        # test
        result = encontrar_iguales(['Kh', '8d', '3c', '3d', '2s'])
        # assert
        self.assertEqual(result, expected)

    def test_trio(self):
        expected = {
            'poker': [],
            'trio': ['K'],
            'par': [],
        }
        result = encontrar_iguales(['Kh', 'Kd', 'Ks', '8h', 'Ts'])
        self.assertEqual(result, expected)

    def test_doblepar(self):
        expected = {
            'poker': [],
            'trio': [],
            'par': ['Q', '8'],
        }
        result = encontrar_iguales(['Qd', 'Qh', '8d', '8s', '4s'])
        self.assertEqual(result, expected)

    def test_poker(self):
        expected = {
            'poker': ['7'],
            'trio': [],
            'par': [],
        }
        result = encontrar_iguales(['7d', '7h', '7d', '7s', '4s'])
        self.assertEqual(result, expected)

    def test_color_true(self):
        result = encontrar_color(['Ad', '2d', '3d', '7d', '4d'])
        self.assertTrue(result)

    def test_color_false(self):
        result = encontrar_color(['Ah', '2d', '3d', '7d', '4d'])
        self.assertFalse(result)

    def test_full_house(self):
        expected = {
            'poker': [],
            'trio': ['7'],
            'par': ['2'],
        }
        result = encontrar_iguales(['2d', '2h', '7d', '7s', '7s'])
        self.assertEqual(result, expected)

    def test_escalera_true(self):
        result = encontrar_escalera(['2h', 'Ad', '3d', '4d', '5d'])
        self.assertTrue(result)

    def test_escalera_false(self):
        result = encontrar_escalera(['8h', 'Ad', '3d', '4d', '5d'])
        self.assertFalse(result)

    def test_escalera_as(self):
        result = encontrar_escalera(['Th', 'Ad', 'Kd', 'Jd', 'Qd'])
        self.assertTrue(result)

    def test_escalera_color_true(self):
        result = encontrar_escalera_color(['2h', 'Ah', '3h', '4h', '5h'])
        self.assertTrue(result)

    def test_escalera_color_false_not_color(self):
        result = encontrar_escalera_color(['2d', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_escalera_color_false_not_escalera(self):
        result = encontrar_escalera_color(['8h', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_escalera_color_false_not_any(self):
        result = encontrar_escalera_color(['8d', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_carta_cartas_pintas(self):
        expected = ['Ad', '3h', '4h', '5h', '8d']
        result = encontrar_cartas_pintas(['8d', 'Ad', '3h', '4h', '5h'])
        self.assertEqual(result, expected)

    def test_ordenar_cartas_numeros(self):
        expected = [1, 3, 4, 5, 8]
        result = ordenar_cartas_numeros(['8d', 'Ad', '3h', '4h', '5h'])
        self.assertEqual(result, expected)

    def test_crear_carta(self):
        expected_value = '7'
        expected_color = 'd'
        result = Card('7', 'd')
        self.assertEqual(result.value, expected_value)
        self.assertEqual(result.color, expected_color)

    def test_crear_mazo(self):
        expected_value = 52
        deck = Deck()
        result = len(deck.cards)
        self.assertEqual(result, expected_value)

    def test_pintas_mazo(self):
        resultD = 0
        resultS = 0
        resultH = 0
        resultC = 0
        expected_value = 13
        deck = Deck()
        for c in range(0, len(deck.cards)):
            if deck.cards[c].color == 'd':
                resultD += 1
            if deck.cards[c].color == 's':
                resultS += 1
            if deck.cards[c].color == 'h':
                resultH += 1
            if deck.cards[c].color == 'c':
                resultC += 1
        self.assertEqual(resultD, expected_value)
        self.assertEqual(resultS, expected_value)
        self.assertEqual(resultH, expected_value)
        self.assertEqual(resultC, expected_value)


if __name__ == "__main__":
    unittest.main()
