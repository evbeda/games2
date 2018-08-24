import unittest
from . import *
from .player import Player


class TestPlayer(unittest.TestCase):
    def test_choose_combination(self):
        # setup
        player01 = Player('01')
        # test
        player01.choose_combination(GENERALA)
        result = GENERALA in player01.combinations
        # assert
        self.assertEqual(result, True)

    def test_dont_allow_repetition(self):
        # setup
        player01 = Player('01')
        # test
        player01.choose_combination(GENERALA)
        player01.choose_combination(GENERALA)
        result = player01.combinations.count(GENERALA)
        # assert
        self.assertEqual(result, 1)

    # def test_calculate_score(self):
    #     # setup

    #     # test
    #     # assert
