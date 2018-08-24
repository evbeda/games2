import unittest

from .blackjack import *
from .mazo import cardsDictionary, colorDictionary
from .game import Game
from .player import Player
from .hand import Hand
from .deck import Deck


class TestBets(unittest.TestCase):
    player_name = 'John'
    # Bet tests
    def test_bet_equal(self):
        player = Player(self.player_name, 10)
        game = Game()
        game.min_bet = 10
        result = compare_bet(game.min_bet, player.money)
        self.assertEqual(result, True)

    def test_bet_minor(self):
        player = Player(self.player_name, 5)
        game = Game()
        game.min_bet = 10
        result = compare_bet(game.min_bet, player.money)
        self.assertEqual(result, False)

    def test_bet_upper(self):
        player = Player(self.player_name, 10)
        game = Game()
        game.min_bet = 5
        result = compare_bet(game.min_bet, player.money)
        self.assertEqual(result, True)

    def test_bet_balance(self):
        player = Player(self.player_name, 10)
        game = Game()
        game.min_bet = 5
        player.balance(game.min_bet)
        self.assertEqual(player.money, 5)

    def test_bet_win_no_blackjack(self):
        player = Player(self.player_name, 10)
        game = Game()
        game.min_bet = 5
        player.balance(game.min_bet)
        game.pot += game.min_bet
        player.win(game.pot)
        self.assertEqual(player.money, 15)

    def test_check_you_can_bet_true(self):
        player = Player(self.player_name, 20)
        game = Game()
        game.player = player
        game.min_bet = 10
        result = game.check_you_can_bet()
        self.assertTrue(result)

    def test_check_you_can_bet_false(self):
        player = Player(self.player_name, 5)
        game = Game()
        game.min_bet = 10
        game.player = player
        result = game.check_you_can_bet()
        self.assertFalse(result)


class TestHands(unittest.TestCase):
    def test_deal_card(self):
        value = ['3d']
        hand = Hand()
        hand.deal_card(value)
        result = value[0] in hand.cards
        self.assertTrue(result)

    def test_card_value_update(self):
        hand = Hand()
        hand.value = 5
        hand.deal_card(['Ah'])
        result = hand.value
        self.assertEqual(result, 16)
    # Sum Cards tests
    def test_cards_sum_normal(self):
        hand = Hand()
        hand.deal_card(['2h', 'Jh'])
        result = hand.sum_cards()
        self.assertEqual(result, 12)

    def test_as_count_one(self):
        hand = Hand()
        hand.deal_card(['8h', 'Ah', '3d'])
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

    def test_reduce_len_when_deal(self):
        deck = Deck(cardsDictionary, colorDictionary)
        initial_len = len(deck.cards)
        cards = deck.deal(2)
        result = len(deck.cards)
        expected = initial_len - 2
        self.assertEqual(expected, result)

    def test_remove_card_when_deal(self):
        deck = Deck(cardsDictionary, colorDictionary)
        cards = deck.deal(2)
        result = [cards in deck.cards]
        self.assertTrue(result)


class TestGame(unittest.TestCase):
    def test_player_has_two_initial_cards(self):
        game = Game()
        game.start_game()
        result = len(game.player.hand.cards)
        self.assertEqual(result, 2)
    
    def test_dealer_has_two_initial_cards(self):
        game = Game()
        game.start_game()
        result = len(game.dealer_hand.cards)
        self.assertEqual(result, 2)
        

if __name__ == "__main__":
    unittest.main()
