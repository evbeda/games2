import unittest
from unittest.mock import patch

from .card import Card
from .deck import Deck
from . import SWORD, COARSE, GOLD, CUP
from .player import Player
from .game import Game


class TestGame(unittest.TestCase):
    player01 = Player('1')
    player02 = Player('2')

    def test_deal_cards(self):
        # setup
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        # test
        game.deal()
        # assert
        self.assertEqual(len(self.player01.hidden_cards), 3)
        self.assertEqual(len(self.player02.hidden_cards), 3)

    def test_reset_hand(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.play_card(1)
        self.player01.reset_hand()
        self.assertEqual(len(self.player01.hidden_cards), 0)
        self.assertEqual(len(self.player01.played_cards), 0)

    def test_change_hand(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.play_card(0)
        self.player02.play_card(0)
        game.deal()
        self.assertFalse(self.player01.is_hand)
        self.assertTrue(self.player02.is_hand)

    def test_play_first_card_p1(self):
        del self.player01.hidden_cards[:]
        del self.player01.played_cards[:]
        carta_0 = Card(SWORD, 3)
        carta_1 = Card(COARSE, 7)
        carta_2 = Card(SWORD, 5)
        self.player01.hidden_cards = [carta_0, carta_1, carta_2]
        # test
        self.player01.play_card(1)
        # assert
        self.assertEqual(
            self.player01.hidden_cards,
            [carta_0, carta_2],
        )
        self.assertEqual(
            self.player01.played_cards,
            [carta_1]
        )

    def test_who_is_next_greater_p1(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.hidden_cards = []
        carta_0 = Card(SWORD, 3)
        carta_1 = Card(COARSE, 7)
        carta_2 = Card(SWORD, 5)
        self.player01.hidden_cards = [carta_0, carta_1, carta_2]
        self.player01.play_card(1)
        carta_3 = Card(GOLD, 2)
        carta_4 = Card(COARSE, 4)
        carta_5 = Card(CUP, 5)
        self.player02.hidden_cards = []
        self.player02.hidden_cards = [carta_3, carta_4, carta_5]
        self.player02.play_card(1)
        result = game.who_is_next()
        self.assertEqual(result, "PLAYER1")

    def test_who_is_next_same_card_p2(self):
        deck = Deck()
        self.player01 = Player('1')
        self.player02 = Player('2')
        game = Game([self.player01, self.player02], deck)

        game.deal()
        game.deal()
        self.player01.reset_hand()
        self.player02.reset_hand()

        carta_0 = Card(SWORD, 3)
        carta_1 = Card(COARSE, 7)
        carta_2 = Card(SWORD, 5)
        self.player01.hidden_cards = [carta_0, carta_1, carta_2]
        self.player01.play_card(0)

        carta_3 = Card(GOLD, 3)
        carta_4 = Card(COARSE, 4)
        carta_5 = Card(CUP, 5)
        self.player02.hidden_cards = [carta_3, carta_4, carta_5]
        self.player02.play_card(0)

        result = game.who_is_next()
        self.assertEqual(result, "PLAYER2")
