import unittest
from unittest.mock import patch

from .card import Card
from .deck import Deck
from . import SWORD, COARSE, GOLD, CUP
from .player import Player
from .game import Game


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

    def test_play_card(self):
        player = Player('Leo')
        player.hidden_cards = [Card(SWORD, 10),
                               Card(SWORD, 11),
                               Card(SWORD, 12)
                               ]
        player.play_card(0)
        expected = Card(SWORD, 10)
        self.assertEqual(expected, player.played_cards[0])

    def test_play_card_not_empty(self):
        player = Player('Leo')
        player.hidden_cards = [Card(SWORD, 10),
                               Card(SWORD, 11),
                               Card(SWORD, 12)
                               ]
        player.play_card(0)
        self.assertEqual(len(player.played_cards), 1)

    def test_show_hand_to_board(self):
        player = Player('Leo')
        player.hidden_cards = [Card(SWORD, 10),
                               Card(SWORD, 11),
                               Card(SWORD, 12)
                               ]
        expected = "Cartas en mano: 10 espada, 11 espada, 12 espada,  \n Cartas jugadas: "
        self.assertEqual(expected, player.show_hand_to_board())

    def test_show_hand_to_board_one_played(self):
        player = Player('Leo')
        player.hidden_cards = [Card(SWORD, 10),
                               Card(SWORD, 11),
                               Card(SWORD, 12)
                               ]
        player.play_card(1)
        expected = "Cartas en mano: 10 espada, 12 espada,  \n Cartas jugadas: 11 espada, "
        self.assertEqual(expected, player.show_hand_to_board())

    # CREACIONES
    def test_si_se_crea_carta(self):
        carta1 = Card(SWORD, 1)
        self.assertIsInstance(carta1, Card)
    # POSICIONES

    def test_obtener_posicion_cero(self):
        cartaMacho = Card(SWORD, 1)
        self.assertEqual(cartaMacho.get_position(), 0)

    def test_obtener_posicion_uno(self):
        cartaMacho = Card(COARSE, 1)
        self.assertEqual(cartaMacho.get_position(), 1)

    def test_obtener_posicion_trece(self):
        cartaMacho = Card(SWORD, 4)
        self.assertEqual(cartaMacho.get_position(), 13)

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
