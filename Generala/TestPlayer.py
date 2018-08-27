import unittest
from . import *
from .player import Player


class TestPlayer(unittest.TestCase):
    def test_choose_combination(self):
        # setup
        player01 = Player('01')
        # test
        player01.choose_combination('GENERALA', 50)
        result = player01.combinations['GENERALA']
        # assert
        self.assertEqual(result, 50)

    def test_dont_allow_repetition(self):
        # setup
        player01 = Player('01')
        # test
        player01.choose_combination('GENERALA', 50)
        result = player01.choose_combination('GENERALA', 50)
        # assert
        self.assertFalse(result)

