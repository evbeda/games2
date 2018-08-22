import unittest
from battleship.battleship import Board


class test_board(unittest.TestCase):
    def test_inicial(self):
        board = Board()
        result = board.get_board()
        board_expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(result, board_expected)

    def test_insert(self):
        board = Board()
        board.set_boat(2, 3, 1, "horizontal")
        board_expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = board.get_board()
        self.assertEqual(result, board_expected)

    def test_insert_three_horizontal_ship(self):
        board = Board()
        board.set_boat(0, 7, 3, "horizontal")
        board_expected = [
            [0, 0, 0, 0, 0, 0, 0, 3, 3, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = board.get_board()
        self.assertEqual(result, board_expected)

    def test_insert_five_vertifcal_ship(self):
        board = Board()
        board.set_boat(3, 4, 5, "vertical")
        board_expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = board.get_board()
        self.assertEqual(result, board_expected)

    def test_error_position(self):
        board = Board()
        result = board.set_boat(10, 10, 1, "horizontal")
        self.assertEqual(result, False)

    def test_error_position_four_horizontal_ship(self):
        board = Board()
        result = board.set_boat(8, 7, 4, "horizontal")
        self.assertFalse(result)

    def test_error_position_five_vertical_ship(self):
        board = Board()
        result = board.set_boat(7, 7, 5, "vertical")
        self.assertFalse(result)

    def test_error_position_already_has_ship_vertical(self):
        board = Board()
        board.set_boat(3, 3, 4, "vertical")
        result = board.set_boat(4, 3, 2, "vertical")
        self.assertFalse(result)

    def test_error_position_already_has_ship_horizontal(self):
        board = Board()
        board.set_boat(2, 2, 4, "horizontal")
        result = board.set_boat(2, 3, 2, "vertical")
        self.assertFalse(result)

    def test_shoot_water(self):
        board = Board()
        result = board.shoot(3, 3)
        self.assertEqual(result, "water")

    def test_shoot_hit(self):
        board = Board()
        board.set_boat(1, 1, 2, "horizontal")
        result = board.shoot(1, 1)
        self.assertEqual(result, "hit")


if __name__ == '__main__':
    unittest.main()
