import unittest
from unittest.mock import patch
from .poker import (
    combine_card,
    better_hand,
    find_straight_flush,
    find_royal_flush,
    find_repeated_cards,
    find_flush,
    find_cards_suits,
    find_straight,
    sort_cards_by_number,
    get_value,
    PREFLOP,
    FLOP,
    TURN,
    RIVER,
    SHOWDOWN,
)
from .card import Card
from .deck import Deck
from .player import Player
from .game import Game
from .hand import Hand


class PokerTest(unittest.TestCase):
    def test_player1_wins(self):
        player01 = Player(20)
        player02 = Player(20)
        player02.money = 0
        deck = Deck()
        deck.create()
        game = Game(player01, player02, deck)
        game.round = 1
        result = game.deal_players()
        self.assertFalse(result)
    
    def test_player2_wins(self):
        player01 = Player(20)
        player02 = Player(20)
        player01.money = 0
        deck = Deck()
        deck.create()
        game = Game(player01, player02, deck)
        game.round = 1
        result = game.deal_players()
        self.assertFalse(result)

    def test_royal_flush(self):
        # test
        result = find_royal_flush(['Ah', 'Kh', 'Qh', 'Jh', 'Th'])
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
        result = find_repeated_cards(['Kh', '8d', '3c', '3d', '2s'])
        # assert
        self.assertEqual(result, expected)

    def test_trio(self):
        expected = {
            'poker': [],
            'trio': ['K'],
            'par': [],
        }
        result = find_repeated_cards(['Kh', 'Kd', 'Ks', '8h', 'Ts'])
        self.assertEqual(result, expected)

    def test_doblepair(self):
        expected = {
            'poker': [],
            'trio': [],
            'par': ['Q', '8'],
        }
        result = find_repeated_cards(['Qd', 'Qh', '8d', '8s', '4s'])
        self.assertEqual(result, expected)

    def test_poker(self):
        expected = {
            'poker': ['7'],
            'trio': [],
            'par': [],
        }
        result = find_repeated_cards(['7d', '7h', '7d', '7s', '4s'])
        self.assertEqual(result, expected)

    def test_color_true(self):
        result = find_flush(['Ad', '2d', '3d', '7d', '4d'])
        self.assertTrue(result)

    def test_color_false(self):
        result = find_flush(['Ah', '2d', '3d', '7d', '4d'])
        self.assertFalse(result)

    def test_full_house(self):
        expected = {
            'poker': [],
            'trio': ['7'],
            'par': ['2'],
        }
        result = find_repeated_cards(['2d', '2h', '7d', '7s', '7s'])
        self.assertEqual(result, expected)

    def test_straight_true(self):
        result = find_straight(['2h', 'Ad', '3d', '4d', '5d'])
        self.assertTrue(result)

    def test_straight_false(self):
        result = find_straight(['8h', 'Ad', '3d', '4d', '5d'])
        self.assertFalse(result)

    def test_straight_as(self):
        result = find_straight(['Th', 'Ad', 'Kd', 'Jd', 'Qd'])
        self.assertTrue(result)

    def test_straight_flush_true(self):
        result = find_straight_flush(['2h', 'Ah', '3h', '4h', '5h'])
        self.assertTrue(result)

    def test_straight_flush_false_not_color(self):
        result = find_straight_flush(['2d', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_straight_flush_false_not_escalera(self):
        result = find_straight_flush(['8h', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_straight_flush_false_not_any(self):
        result = find_straight_flush(['8d', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_cards_suits(self):
        expected = ['Ad', '3h', '4h', '5h', '8d']
        result = find_cards_suits(['8d', 'Ad', '3h', '4h', '5h'])
        self.assertEqual(result, expected)

    def test_sort_cards_by_number(self):
        expected = [1, 3, 4, 5, 8]
        result = sort_cards_by_number(['8d', 'Ad', '3h', '4h', '5h'])
        self.assertEqual(result, expected)

    def test_create_card(self):
        expected_value = '7'
        expected_suit = 'd'
        result = Card('7', 'd')
        self.assertEqual(result.value, expected_value)
        self.assertEqual(result.suit, expected_suit)

    def test_create_deck(self):
        expected_value = 52
        deck = Deck()
        result = len(deck.cards)
        self.assertEqual(result, expected_value)

    def test_deck_suits(self):
        resultD = 0
        resultS = 0
        resultH = 0
        resultC = 0
        expected_value = 13
        deck = Deck()
        for c in range(0, len(deck.cards)):
            if deck.cards[c].suit == 'd':
                resultD += 1
            if deck.cards[c].suit == 's':
                resultS += 1
            if deck.cards[c].suit == 'h':
                resultH += 1
            if deck.cards[c].suit == 'c':
                resultC += 1
        self.assertEqual(resultD, expected_value)
        self.assertEqual(resultS, expected_value)
        self.assertEqual(resultH, expected_value)
        self.assertEqual(resultC, expected_value)

    def test_deal_cards(self):
        expected_value = 3
        expected_deck_size = 52 - expected_value
        deck = Deck()
        result = deck.deal(expected_value)
        self.assertEqual(len(result), expected_value)
        self.assertEqual(len(deck.cards), expected_deck_size)

    def test_rebuid_deck(self):
        expected_value = 6
        expected_deck_size = 52
        deck = Deck()
        deck.deal(expected_value)
        deck.rebuild()
        self.assertEqual(len(deck.cards), expected_deck_size)

    def test_create_player(self):
        jugador_money = 10
        jugador = Player(jugador_money)
        cards_dealed = 2
        deck = Deck()
        jugador.cards = deck.deal(cards_dealed)
        self.assertEqual(len(jugador.cards), cards_dealed)
        self.assertEqual(jugador.money, jugador_money)

    def test_create_player_without_money(self):
        with self.assertRaises(Exception):
            Player(0)
        self.assertTrue('Player money must be greater than 0')

    def test_take_bets(self):
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

    def test_check_hand(self):
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

    def test_get_value_J_Q_K(self):
        self.assertEqual(get_value('J'),11)
        self.assertEqual(get_value('Q'),12)
        self.assertEqual(get_value('K'),13)

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

    def test_best_hand_royal_flush(self):
        combination = combine_card(['Ah', 'Th', '5h', 'Jh', '7h', 'Qh', 'Kh'])
        result = better_hand(combination)
        self.assertEqual(result, "Escalera Real")

    def test_best_hand_no_royal_flsuh(self):
        combination = combine_card(['Ad', 'Th', '5h', 'Jh', '7h', 'Qh', 'Kh'])
        result = better_hand(combination)
        self.assertEqual(result, "No es Escalera Real")

    def test_poker_hand(self):
        combination = combine_card(['Ad', 'Ac', 'Th', 'Ts', 'Ah', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, "Poker")

    def test_straight_flush_hand(self):
        combination = combine_card(['6d', 'Ac', 'Td', 'Ts', '7d', '8d', '9d'])
        result = better_hand(combination)
        self.assertEqual(result, "Escalera Color")

    def test_one_trio_of_no_faced_cards(self):
        combination = combine_card(['Ad', '3c', 'Th', '3s', '7h', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de 3")
        combination = combine_card(['Jd', '3c', 'Jh', '3s', '7h', '3d', 'Js'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de J")
        combination = combine_card(['Qd', '3c', 'Qh', '3s', 'Qh', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de Q")
        combination = combine_card(['Ad', '3c', 'Kh', '3s', 'Kh', '3d', 'Ks'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de K")


    def test_two_trio_hand(self):
        combination = combine_card(['Td', '3c', 'Th', '3s', '7h', '3d', 'Ts'])
        result = better_hand(combination)
        self.assertEqual(result, "Trio de T")
    
    def test_card_repr(self):
        card = Card('K', 'h')
        result = card.__repr__()
        self.assertEqual(result, 'Kh')

    def test_hand_deal_initial_cards(self):
        hand = Hand()
        self.assertEqual(
            hand.stage,
            PREFLOP,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.player02_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            0,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_deal_flop(self):
        hand = Hand() 
        hand.next_stage()
        hand.deal_cards()
        self.assertEqual(
            hand.stage,
            FLOP,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            3,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_deal_turn(self):
        hand = Hand() 
        hand.next_stage()
        hand.deal_cards()
        hand.next_stage()
        hand.deal_cards()
        self.assertEqual(
            hand.stage,
            TURN,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            4,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_deal_river(self):
        hand = Hand() 
        hand.next_stage()
        hand.deal_cards()
        hand.next_stage()
        hand.deal_cards()
        hand.next_stage()
        hand.deal_cards()
        self.assertEqual(
            hand.stage,
            RIVER,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            5,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_showdown(self):
        hand = Hand() 
        hand.next_stage()
        hand.deal_cards()
        hand.next_stage()
        hand.deal_cards()
        hand.next_stage()
        hand.deal_cards()
        hand.next_stage()
        self.assertEqual(
            hand.stage,
            SHOWDOWN
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.player01_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            5,
        )


if __name__ == "__main__":
    unittest.main()
