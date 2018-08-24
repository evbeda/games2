from .game import Game
import unittest


class TestGame(unittest.TestCase):

    def test_game_finished_true(self):
        game = Game("Lautaro", "Chino")
        game.player1.combinations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'Escalera']
        game.player2.combinations = [1, 2, 3, 4, 5, 6, 'Generala', 8, 9, 'Full', 11, 12, 13]
        self.assertTrue(game.finished())
