import unittest
from guess_number_game.guess_number_game import GuessNumberGame


class TestGuessNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = GuessNumberGame()
        self.game._guess_number = 50

    def test_initial_status(self):
        self.assertTrue(self.game.is_playing)

    def test_play_lower(self):
        play_result = self.game.play(10)
        self.assertEqual(play_result, 'too low')
        self.assertTrue(self.game.is_playing)

    def test_play_higher(self):
        play_result = self.game.play(80)
        self.assertEqual(play_result, 'too high')
        self.assertTrue(self.game.is_playing)

    def test_play_equal(self):
        play_result = self.game.play(50)
        self.assertEqual(play_result, 'you win')
        self.assertFalse(self.game.is_playing)

    def test_initial_next_turn(self):
        self.assertEqual(
            self.game.next_turn(),
            'Give me a number from 0 to 100',
        )

    def test_next_turn_after_play(self):
        self.game.play(10)
        self.assertEqual(
            self.game.next_turn(),
            'Give me a number from 0 to 100',
        )

    def test_next_turn_after_win(self):
        self.game.play(50)
        self.assertEqual(
            self.game.next_turn(),
            'Game Over',
        )

    def test_get_board(self):
        self.assertEqual(
            self.game.board,
            '[]'
        )
        self.game.play(10)
        self.assertEqual(
            self.game.board,
            '[10]'
        )


if __name__ == "__main__":
    unittest.main()
