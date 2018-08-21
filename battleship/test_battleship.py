import unittest


class TestBattleship(unittest.TestCase):
    def test_hit(self):
        posicion = [0, 0]
        resultado = shoot(posicion)
        self.assertEqual(resultado, "Hit")


if __name__ == "__main__":
    unittest.main()
