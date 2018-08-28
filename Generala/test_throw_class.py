import unittest
from .throw import Throw


class TestThrow(unittest.TestCase):

    def test_throw_number(self):
        throw = Throw()
        number_of_dices = len(throw.dice)
        self.assertEqual(number_of_dices, 5)

    def test_throw_conserve_1_2(self):
        throw = Throw()
        conserved_dices = [throw.dice[0], throw.dice[1]]
        throw.roll([2, 3, 4, ])
        self.assertEqual(conserved_dices, [throw.dice[0], throw.dice[1]])
        self.assertTrue(throw.is_possible_to_roll())

    def test_throw_number_bigger_3(self):
        throw = Throw()
        throw.roll([0, 1, 2, 3, 4, ])
        throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(
            throw.roll([0, 1, 2, 3, 4, ]),
            "Error. Max roll number reached."
        )
        self.assertFalse(throw.is_possible_to_roll())


if __name__ == '__main__':
    unittest.main()
