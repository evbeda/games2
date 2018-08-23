import unittest
from battleship.battleship import Board


class test_battleship(unittest.TestCase):

    def test_shoot_water(self):
        board = Board()
        result = board.shoot(3, 3)
        self.assertEqual(result, "water")

    def test_shoot_sunked_1(self):
        board = Board()
        board.set_boat(1, 1, 1, "horizontal")
        result = board.shoot(1, 1)
        self.assertEqual(result, "sunked")

    def test_shoot_sunked_2(self):
        board = Board()
        result = []
        board.set_boat(0, 0, 2, "horizontal")
        for i in range(0, 2):
            result.append(board.shoot(0, i))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_31(self):
        board = Board()
        result = []
        board.set_boat(1, 2, 3, "vertical")
        for i in range(1, 4):
            result.append(board.shoot(i, 2))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_32(self):
        board = Board()
        result = []
        board.set_boat(5, 7, 3, "horizontal")
        for i in range(7, 10):
            result.append(board.shoot(5, i))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_4(self):
        board = Board()
        result = []
        result2 = []
        result3 = []
        board.set_boat(9, 5, 4, "horizontal")
        for i in range(5, 9):
            result.append(board.shoot(9, i))
        board.set_boat(0, 0, 3, "horizontal")
        for i in range(0, 1):
            result2.append(board.shoot(0, i))
        board.set_boat(4, 5, 3, "horizontal")
        for i in range(5, 8):
            result3.append(board.shoot(4, i))
        self.assertEqual(result[len(result) - 1], "sunked")
        self.assertEqual(result2[len(result2) - 1], "hit")
        self.assertEqual(result3[len(result3) - 1], "sunked")

    def test_shoot_sunked_5(self):
        board = Board()
        result = []
        board.set_boat(5, 5, 5, "vertical")
        for i in range(5, 10):
            result.append(board.shoot(i, 5))
        self.assertEqual(result[len(result) - 1], "sunked")


if __name__ == "__main__":
    unittest.main()
