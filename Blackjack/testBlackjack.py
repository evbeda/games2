import unittest

from .blackjack import *
from .mazo import cardsDictionary, colorDictionary
from .game import Game
from .player import Player
from .hand import Hand
from .deck import Deck


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

    def test_bet_balance(self):
        player = Player(10)
        game = Game(5, player)
        player.balance(game.min_bet)
        self.assertEqual(player.money, 5)

    def test_bet_win_no_blackjack(self):
        player = Player(10)
        game = Game(5, player)
        player.balance(game.min_bet)
        player.win(game.pot)
        self.assertEqual(player.money, 15)

    def test_check_you_can_bet_true(self):
        player = Player(20)
        game = Game(10, player)
        result = game.check_you_can_bet()
        self.assertTrue(result)

    def test_check_you_can_bet_false(self):
        player = Player(1)
        game = Game(10, player)
        result = game.check_you_can_bet()
        self.assertFalse(result)


class TestHands(unittest.TestCase):
    def test_deal_card(self):
        value = '3d'
        hand = Hand()
        hand.deal_card(value)
        result = value in hand.cards
        self.assertTrue(result)

    def test_card_value_update(self):
        hand = Hand()
        hand.value = 5
        hand.deal_card('Ah')
        result = hand.value
        self.assertEqual(result, 16)
    # Sum Cards tests
    def test_cards_sum_normal(self):
        hand = Hand()
        hand.deal_card('2h')
        hand.deal_card('Jh')
        result = hand.sum_cards()
        self.assertEqual(result, 12)

    def test_as_count_one(self):
        hand = Hand()
        hand.deal_card('8h')
        hand.deal_card('Ah')
        hand.deal_card('3d')
        result = hand.sum_cards()
        self.assertEqual(result, 12)


class TestDeck(unittest.TestCase):
    def test_create_deck(self):
        deck = Deck(cardsDictionary, colorDictionary)
        result = len(deck.cards)
        self.assertEqual(result, 52)

    def test_shuffle_deck(self):
        deck = Deck(cardsDictionary, colorDictionary)
        initial_cards = deck.cards
        deck.shuffle()
        result = False
        for i in range(len(deck.cards)):
            if initial_cards[i] != deck.cards[i]:
                result = False
            result = True
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
