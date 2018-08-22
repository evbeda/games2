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
        hand = Hand(['2', '3'])
        hand.deal_cards()
        self.assertEqual(hand.playersCards, ['2', '3'])

    def test_add_card_5_to_player_one(self):
        hand = Hand(['2', '3'])
        hand.deal_cards()
        hand.add_card_to_player('5')
        self.assertEqual(hand.playersCards, ['2', '3', '5'])

    def test_add_card_A_to_player_one(self):
        hand = Hand(['2', '3'])
        hand.deal_cards()
        hand.add_card_to_player('A')
        self.assertEqual(hand.playersCards, ['2', '3', 'A'])

    def test_finish_hand_true(self):
        hand = Hand(['J', 'J'])
        hand.deal_cards()
        hand.add_card_to_player('5')
        result = hand.is_it_finished()
        self.assertTrue(result)

    def test_finish_hand_false(self):
        hand = Hand(['J', '2'])
        hand.deal_cards()
        hand.add_card_to_player('5')
        result = hand.is_it_finished()
        self.assertFalse(result)

    def test_check_you_can_bet_true(self):
        player = Player(20)
        game = Game(10, player)
        result = game.check_you_can_bet()
        self.assertTrue(result)

    def test_check_you_can_bet_false(self):
        player = Player(10)
        game = Game(10, player)
        result = game.check_you_can_bet()
        self.assertFalse(result)

    def test_check_you_can_play_true(self):
        player1 = Player(10)
        game1 = Game(5, player1)
        self.assertTrue(game1.check_you_can_play())

    def test_check_you_can_play_false(self):
        player1 = Player(2)
        game1 = Game(5, player1)
        self.assertFalse(game1.check_you_can_play())

if __name__ == "__main__":
    unittest.main()
