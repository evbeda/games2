import unittest
from battleship.test_board import test_board
from battleship.test_battleship import test_battleship
from Blackjack.testBlackjack import (
    TestBets,
    TestHands,
    TestDeck,
    TestGame as TestBlackjackGame
)

from truco.test_game import TestGame as TG
from truco.test_deck import TestDeck as TD
from truco.test_cards import TestCards as TCD
from truco.test_hand import TestHand as TestHandTruco
from truco.test_player import TestPlayer as TrucoTestPlayer
from poker.test_poker import PokerTest, PokerGameTest
from guess_number_game import test_guess_number_game
import test_game
from Generala.TestCategories import TestCategories
from Generala.TestThrowDice import TestThrowDice
from Generala.TestPlayer import TestPlayer
from Generala.TestGame import TestGame
from Generala.test_throw_class import TestThrow
from guess_number_game import test_guess_number_game


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
    test_suite.addTest(unittest.makeSuite(PokerGameTest))
    test_suite.addTest(unittest.makeSuite(test_guess_number_game))
    test_suite.addTest(test_game)
    test_suite.addTest(unittest.makeSuite(TestCategories))
    test_suite.addTest(unittest.makeSuite(TestThrowDice))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestGame))
    test_suite.addTest(unittest.makeSuite(TestThrow))
    test_suite.addTest(unittest.makeSuite(test_guess_number_game))
    test_suite.addTest(test_game)
    test_suite.addTest(TG)
    test_suite.addTest(TD)
    test_suite.addTest(TCD)
    test_suite.addTest(TestHandTruco)
    test_suite.addTest(TrucoTestPlayer)
    return test_suite


if __name__ == "__main__":
    unittest.main()
