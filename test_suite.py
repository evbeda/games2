import unittest
from battleship.test_board import test_board
from battleship.test_battleship import test_battleship
from Blackjack.testBlackjack import (
    TestBets,
    TestHands,
    TestDeck
)
from Generala.main_test import *
from truco.test_truco import *
from poker.test_poker import *
from guess_number_game import test_guess_number_game
import test_game


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_board))
    test_suite.addTest(unittest.makeSuite(test_battleship))
    test_suite.addTest(unittest.makeSuite(TestCards))
    test_suite.addTest(unittest.makeSuite(TestBets))
    test_suite.addTest(unittest.makeSuite(TestHands))
    test_suite.addTest(unittest.makeSuite(test_categories))
    test_suite.addTest(unittest.makeSuite(TestCartas))
    test_suite.addTest(unittest.makeSuite(TestMazo))
    test_suite.addTest(unittest.makeSuite(PokerTest))
    test_suite.addTest(unittest.makeSuite(test_guess_number_game))
    test_suite.addTest(test_game)
    return test_suite


if __name__ == "__main__":
    unittest.main()
