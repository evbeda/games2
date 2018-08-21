import unittest
from blackjack import *
from game import Game
from player import Player

class TestClass(unittest.TestCase):

    #Sum Cards tests

    def test_cards_sum_normal(self):
        cards = ['2','J']
        result = sum_cards(cards)
        self.assertEqual(result,12)

    def test_cards_sum_as1(self):
        cards = ['A','J']
        result = sum_cards(cards)
        self.assertEqual(result,21)

    def test_cards_sum_as11(self):
        cards = ['A','J','J']
        result = sum_cards(cards)
        self.assertEqual(result,21)
    
    # Bet tests

    def test_bet_equal(self):
        player = Player(10)
        game = Game(10,player)
        result = compare_bet(game.min_bet,player.money)
        self.assertEqual(result,True)
    def test_bet_minor(self):
        player = Player(5)
        game = Game(10,player)
        result = compare_bet(game.min_bet,player.money)
        self.assertEqual(result,False)
    def test_bet_upper(self):
        player = Player(10)
        game = Game(5,player)
        result = compare_bet(game.min_bet,player.money)
        self.assertEqual(result,True)

if __name__ == "__main__":
    unittest.main()
