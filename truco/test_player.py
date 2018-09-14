import unittest

from truco.player import CPUPlayer


class TestPlayer(unittest.TestCase):

    @unittest.mock.patch("truco.player.CPUPlayer.choose_one_action", return_value=['ACCEPTED', 'REJECTED'])
    def test_ask_envido_one(self, mock):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.ask_envido("ANY")
        self.assertTrue(result in ['ACCEPTED', 'REJECTED'])

    @unittest.mock.patch("truco.player.CPUPlayer.choose_one_action", return_value=['ACCEPTED', 'REJECTED'])
    def test_ask_envido_two(self, mock):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.ask_envido("ANY")
        self.assertTrue(result in ['ACCEPTED', 'REJECTED'])

    @unittest.mock.patch("truco.player.CPUPlayer.choose_one_action", return_value=['ACCEPTED', 'REJECTED'])
    def test_ask_envido_three(self, mock):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.ask_envido("ANY")
        self.assertTrue(result in ['ACCEPTED', 'REJECTED'])

    def test_choose_one_action_one(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.choose_one_action(["FALTA_ENVIDO"])
        self.assertEqual(result, ['ACCEPTED', 'REJECTED'])

    def test_choose_one_action_two(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.choose_one_action(["REAL_ENVIDO"])
        self.assertEqual(result, ['ACCEPTED', 'REJECTED', "FALTA_ENVIDO"])

    def test_choose_one_action_three(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.choose_one_action(["ENVIDO"])
        self.assertEqual(
            result, ['ACCEPTED', 'REJECTED', "FALTA_ENVIDO", "REAL_ENVIDO", "ENVIDO"])

    def test_choose_one_action_ford(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.choose_one_action(["ENVIDO", "ENVIDO"])
        self.assertEqual(
            result, ['ACCEPTED', 'REJECTED', "FALTA_ENVIDO", "REAL_ENVIDO"])

    def test_ask_truco_one(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.ask_trucos(["TRUCO"])
        self.assertTrue(
            result in ['ACCEPTED', 'REJECTED', 'RE_TRUCO', 'VALE_CUATRO'])

    def test_ask_truco_two(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.ask_trucos(["TRUCO", "RE_TRUCO"])
        self.assertTrue(result in ['ACCEPTED', 'REJECTED', 'VALE_CUATRO'])

    def test_ask_truco_three(self):
        cpu = CPUPlayer('NOMBRE')
        result = cpu.ask_trucos(["TRUCO", "RE_TRUCO", "VALE_CUATRO"])
        self.assertTrue(result in ['ACCEPTED', 'REJECTED'])
