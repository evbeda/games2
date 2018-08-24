import unittest
from .utils import throw_dice


class test_throw_dice(unittest.TestCase):
    def test_throw(self):
        throwResult = throw_dice(1)
        self.assertTrue(1 <= throwResult[0] <= 6)

    def test_number_of_results(self):
        result = throw_dice(3)
        self.assertEqual(len(result), 3)
