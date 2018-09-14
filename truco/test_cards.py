import unittest

from . import SWORD, COARSE
from .card import Card


class TestCards(unittest.TestCase):

    def test_eq_cards(self):
        card_one = Card(SWORD, 10)
        card_two = Card(SWORD, 10)
        result = card_one.__eq__(card_two)
        self.assertTrue(result)

    def test_not_eq_cards(self):
        card_one = Card(SWORD, 10)
        card_two = Card(SWORD, 9)
        result = card_one.__eq__(card_two)
        self.assertFalse(result)

    def test_eq_cards_false(self):
        card_one = Card(SWORD, 10)
        card_two = Card(SWORD, 9)
        result = card_one.__eq__(card_two)
        self.assertFalse(result)

    # CREACIONES
    def test_si_se_crea_carta(self):
        carta1 = Card(SWORD, 1)
        self.assertIsInstance(carta1, Card)

    # POSICIONES

    def test_obtener_posicion_cero(self):
        carta_macho = Card(SWORD, 1)
        self.assertEqual(carta_macho.get_position(), 0)

    def test_obtener_posicion_uno(self):
        carta_macho = Card(COARSE, 1)
        self.assertEqual(carta_macho.get_position(), 1)

    def test_obtener_posicion_trece(self):
        carta_macho = Card(SWORD, 4)
        self.assertEqual(carta_macho.get_position(), 13)

    # COMPARACIONES
    def test_comparar_as_espadas_con_as_bastos(self):
        carta1 = Card(SWORD, 1)
        carta2 = Card(COARSE, 1)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'GREATER')

    def test_comparar_4_de_espadas_con_4_de_bastos(self):
        carta1 = Card(SWORD, 4)
        carta2 = Card(COARSE, 4)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'EQUAL')

    def test_comparar_7_de_espadas_con_7_de_bastos(self):
        carta1 = Card(SWORD, 7)
        carta2 = Card(COARSE, 7)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'GREATER')

    def test_comparar_5_de_espadas_con_2_de_bastos(self):
        carta1 = Card(SWORD, 5)
        carta2 = Card(COARSE, 2)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'LOWER')

    def test_to_string(self):
        carta1 = Card(SWORD, 5)
        self.assertEqual(carta1.__str__(), "5 espada")


if __name__ == '__main__':
    unittest.main()
