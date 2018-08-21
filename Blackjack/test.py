import unittest
from blackjack import sum_cards

class TestClass(unittest.TestCase):

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
    
    

if __name__ == "__main__":
    unittest.main()
