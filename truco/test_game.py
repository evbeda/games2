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

    # def test_change_hand(self):
    #     game = Game([self.player01, self.player02])
    #     self.player01.play_card(0)
    #     self.player02.play_card(0)
    #     self.assertFalse(self.player01.is_hand)
    #     self.assertTrue(self.player02.is_hand)
