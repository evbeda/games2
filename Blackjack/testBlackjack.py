import unittest
from .blackjack import *
from .game import Game
from .player import Player
from .hand import Hand


class TestCards(unittest.TestCase):

    # Sum Cards tests

    def test_cards_sum_normal(self):
        cards = ['2', 'J']
        result = sum_cards(cards)
        self.assertEqual(result, 12)

    def test_cards_sum_as1(self):
        cards = ['A', 'J']
        result = sum_cards(cards)
        self.assertEqual(result, 21)

    def test_cards_sum_as11(self):
        cards = ['A', 'J', 'J']
        result = sum_cards(cards)
        self.assertEqual(result, 21)


class TestBets(unittest.TestCase):
    # Bet tests

    def test_bet_equal(self):
        player = Player(10)
        game = Game(10, player)
        result = compare_bet(game.min_bet, player.money)
        self.assertEqual(result, True)

    def test_bet_minor(self):
        player = Player(5)
        game = Game(10, player)
        result = compare_bet(game.min_bet, player.money)
        self.assertEqual(result, False)

    def test_bet_upper(self):
        player = Player(10)
        game = Game(5, player)
        result = compare_bet(game.min_bet, player.money)
        self.assertEqual(result, True)


class TestHands(unittest.TestCase):

    # Initial Hand

    def test_initial_hand(self):
        hand = Hand(['2', '3', '4', '5'])
        hand.deal_cards()
        self.assertEqual(hand.playersCards, {'1': ['2', '3'], '2': ['4', '5']})

    def test_add_card_5_to_player_one(self):
        hand = Hand(['2', '3', '4', '5'])
        hand.deal_cards()
        hand.add_card_to_player('1', '5')
        self.assertEqual(hand.playersCards, {'1': ['2', '3', '5'], '2': ['4', '5']})

    def test_add_card_A_to_player_two(self):
        hand = Hand(['2', '3', '4', '5'])
        hand.deal_cards()
        hand.add_card_to_player('2', 'A')
        self.assertEqual(hand.playersCards, {'1': ['2', '3'], '2': ['4', '5', 'A']})

    def test_finish_hand_true(self):
        hand = Hand(['J', 'J', '4', '5'])
        hand.deal_cards()
        hand.add_card_to_player('1', '5')
        result = hand.is_it_finished()
        self.assertTrue(result)

    def test_finish_hand_false(self):
        hand = Hand(['J', '2', '4', '5'])
        hand.deal_cards()
        hand.add_card_to_player('1', '5')
        result = hand.is_it_finished()
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
