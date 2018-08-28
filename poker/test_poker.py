import unittest
from unittest.mock import patch
from .poker import (
    combine_card,
    better_hand,
    encontrar_escalera_color,
    encontrar_escalera_real,
    encontrar_iguales,
    encontrar_color,
    encontrar_cartas_pintas,
    encontrar_escalera,
    ordenar_cartas_numeros,
)
from .card import Card
from .deck import Deck
from .player import Player
from .game import Game


class PokerTest(unittest.TestCase):
    def test_escaleraReal(self):
        # test
        result = encontrar_escalera_real(['Ah', 'Kh', 'Qh', 'Jh', 'Th'])
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

    def test_repartir_cartas(self):
        expected_value = 3
        expected_deck_size = 52 - expected_value
        deck = Deck()
        result = deck.deal(expected_value)
        self.assertEqual(len(result), expected_value)
        self.assertEqual(len(deck.cards), expected_deck_size)

    def test_reconstruir_mazo(self):
        expected_value = 6
        expected_deck_size = 52
        deck = Deck()
        deck.deal(expected_value)
        deck.rebuild()
        self.assertEqual(len(deck.cards), expected_deck_size)

    def test_crear_jugador(self):
        jugador_money = 10
        jugador = Player(jugador_money)
        cards_dealed = 2
        deck = Deck()
        jugador.cards = deck.deal(cards_dealed)
        self.assertEqual(len(jugador.cards), cards_dealed)
        self.assertEqual(jugador.money, jugador_money)

    def test_crear_jugador_sin_dinero(self):
        with self.assertRaises(Exception):
            Player(0)
        self.assertTrue('Player money must be greater than 0')

    def test_tomar_apuestas(self):
        player1_money = 1000
        player2_money = 2000
        player1 = Player(player1_money)
        player2 = Player(player2_money)
        deck = Deck()
        game = Game(player1, player2, deck)
        game.start()
        result_false_player1 = game.take_bets(5500, 500)
        result_false_player2 = game.take_bets(500, 5500)
        result_true = game.take_bets(500, 500)
        self.assertFalse(result_false_player1)
        self.assertFalse(result_false_player2)
        self.assertTrue(result_true)

    def test_pot_correct(self):
        player1_money = 1000
        player2_money = 2000
        player1 = Player(player1_money)
        player2 = Player(player2_money)
        deck = Deck()
        game = Game(player1, player2, deck)
        game.start()
        game.take_bets(500, 500)
        self.assertEqual(game.pot, 1000)

    def test_verificar_mano(self):
        player1_money = 1000
        player2_money = 2000
        player1 = Player(player1_money)
        player2 = Player(player2_money)

        def side_effect(cards):
            return cards
        with unittest.mock.patch('poker.deck.shuffle', side_effect):
            deck = Deck()
        player1.cards.append(deck.cards[48])
        player1.cards.append(deck.cards[49])
        player1.cards.append(deck.cards[50])
        player1.cards.append(deck.cards[28])
        player1.cards.append(deck.cards[38])
        player2.cards = deck.deal(5)

    def test_21combinations(self):
        result = combine_card(['Ah', '2h', '5h', '6h', '7h', '8h', '9h'])
        self.assertEqual(len(result), 21)

    def test_first_combination(self):
        result = combine_card(['Ah', '2h', '5h', '6h', '7h', '8h', '9h'])
        self.assertEqual(result[0], ['Ah', '2h', '5h', '6h', '7h'])
        self.assertEqual(result[1], ['Ah', '2h', '5h', '6h', '8h'])
        self.assertEqual(result[2], ['Ah', '2h', '5h', '6h', '9h'])
        self.assertEqual(result[3], ['Ah', '2h', '5h', '7h', '8h'])
        self.assertEqual(result[4], ['Ah', '2h', '5h', '7h', '9h'])
        self.assertEqual(result[5], ['Ah', '2h', '5h', '8h', '9h'])
        self.assertEqual(result[6], ['Ah', '2h', '6h', '7h', '8h'])
        self.assertEqual(result[7], ['Ah', '2h', '6h', '7h', '9h'])
        self.assertEqual(result[8], ['Ah', '2h', '6h', '8h', '9h'])
        self.assertEqual(result[9], ['Ah', '2h', '7h', '8h', '9h'])
        self.assertEqual(result[10], ['Ah', '5h', '6h', '7h', '8h'])
        self.assertEqual(result[11], ['Ah', '5h', '6h', '7h', '9h'])
        self.assertEqual(result[12], ['Ah', '5h', '6h', '8h', '9h'])
        self.assertEqual(result[13], ['Ah', '5h', '7h', '8h', '9h'])
        self.assertEqual(result[14], ['Ah', '6h', '7h', '8h', '9h'])
        self.assertEqual(result[15], ['2h', '5h', '6h', '7h', '8h'])
        self.assertEqual(result[16], ['2h', '5h', '6h', '7h', '9h'])
        self.assertEqual(result[17], ['2h', '5h', '6h', '8h', '9h'])
        self.assertEqual(result[18], ['2h', '5h', '7h', '8h', '9h'])
        self.assertEqual(result[19], ['2h', '6h', '7h', '8h', '9h'])
        self.assertEqual(result[20], ['5h', '6h', '7h', '8h', '9h'])

    def test_best_hand_escalera_real(self):
        combination = combine_card(['Ah', 'Th', '5h', 'Jh', '7h', 'Qh', 'Kh'])
        result = better_hand(combination)
        self.assertEqual(result, "Escalera Real")

    def test_best_hand_no_escalera_real(self):
        combination = combine_card(['Ad', 'Th', '5h', 'Jh', '7h', 'Qh', 'Kh'])
        result = better_hand(combination)
        self.assertEqual(result, "No es Escalera Real")

    def test_poker_hand(self):
        combination = combine_card(['Ad', 'Ac', 'Th', 'Ts', 'Ah', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, "Poker")

    # TODO replace value '1' for A
    def test_one_trio_hand(self):
        combination = combine_card(['Ad', 'Ac', 'Th', 'Ts', '7h', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de A")

    def test_one_trio_of_no_faced_cards(self):
        combination = combine_card(['Ad', '3c', 'Th', '3s', '7h', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de 3")

    def test_two_trio_hand(self):
        combination = combine_card(['Td', '3c', 'Th', '3s', '7h', '3d', 'Ts'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de T")

if __name__ == "__main__":
    unittest.main()
