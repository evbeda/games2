import unittest
from poker import *


class PokerTest(unittest.TestCase):
    def test_escaleraReal(self):
        # setup
        expected = True
        # test
        result = encontrarEscaleraReal(['Ah', 'Kh', 'Qh', 'Jh', 'Th'])
        # assert
        self.assertEqual(result, expected)

    def test_pares(self):
        # setup
        expected = ['3']
        # test
        result = encontrarPares(['Kh', '8d', '3c', '3d', '2s'])
        # assert
        self.assertEqual(result, expected)

    def test_trio(self):
        expected = ['K']
        result = encontrarTrio(['Kh', 'Kd', 'Ks', '8h', '10s'])
        self.assertEqual(result, expected)

    def test_doblepar(self):
        expected = ['Q', '8']
        result = encontrarPares(['Qd', 'Qh', '8d', '8s', '4s'])
        self.assertEqual(result, expected)



# master
# def definirMano(self):
#     # setup

#     # test

#     # assert
if __name__ == "__main__":
    unittest.main()
