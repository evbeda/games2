import unittest

from truco import *
from truco.card import Card
from truco.game import Game
from truco.player import CPUPlayer


class TestGame(unittest.TestCase):

    def test_arraise_exception_truco_logic(self):
        game = Game()
        with unittest.mock.patch("truco.player.CPUPlayer.ask_trucos", return_value='REJECTED'):
            game.play("TRUCO")
        with self.assertRaises(Exception):
            game.sing_truco('TRUCO')

    def test_truco_relive_re_truco(self):
        game = Game()
        with unittest.mock.patch("truco.player.CPUPlayer.ask_trucos", return_value='RE TRUCO'):
            game.play("TRUCO")
        game.play("ACCEPTED")
        self.assertEqual(game.hand.trucos, ['TRUCO', 'RE TRUCO'])
        self.assertFalse(game.hand.truco_pending)

    def test_player_ask_falta_envido(self):
        player = CPUPlayer('CPY')
        all_ready_envidos = ['REAL ENVIDO', 'ENVIDO', 'ENVIDO']
        self.assertEqual(
            player.choose_one_action(all_ready_envidos),
            ['ACCEPTED', 'REJECTED', 'FALTA ENVIDO'],
        )

    def test_player_ask_envido_when_there_are_not_more_sings(self):
        player = CPUPlayer('CPY')
        all_ready_envidos = ['FALTA ENVIDO']
        self.assertEqual(
            player.choose_one_action(all_ready_envidos),
            ['ACCEPTED', 'REJECTED'],
        )

    def test_sing_real_envido_and_only_can_sing_falta_envido(self):
        player = CPUPlayer('mocky')
        all_ready_envidos = ['REAL ENVIDO']
        self.assertEqual(
            player.choose_one_action(all_ready_envidos),
            ['ACCEPTED', 'REJECTED', 'FALTA ENVIDO'],
        )

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ACCEPTED')
    def test_p1_sing_falta_envido(self, mocky):
        game = Game()
        game.play("FALTA ENVIDO")
        self.assertFalse(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['FALTA ENVIDO'])

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='REAL ENVIDO')
    def test_cpu_canta_real_envido(self, mocksito):
        game = Game()
        game.play("ENVIDO")
        self.assertTrue(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['ENVIDO', 'REAL ENVIDO'])

    def test_cantar_envido_no_fase_envido(self):
        game = Game()
        game.hand.envido_fase = False
        result = game.play("ENVIDO")
        self.assertEqual(result, "No en fase de envido")

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ACCEPTED')
    def test_cantar_fases_envido_and_accept(self, mock_ask_envido):
        game = Game()
        self.assertTrue(game.hand.envido_fase)
        game.play("ENVIDO")
        # cpu accept envido... force random
        self.assertFalse(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['ENVIDO'])

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='REJECTED')
    def test_cantar_fases_envido_and_not_accept(self, mock_ask_envido):
        game = Game()
        self.assertTrue(game.hand.envido_fase)
        game.play("ENVIDO")
        # cpu accept envido... force random
        self.assertFalse(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, [])
        # CPU lose 1 point ... TODO

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ENVIDO')
    def test_cantar_fases_envido_and_envido(self, mock_ask_envido):
        game = Game()
        self.assertTrue(game.hand.envido_fase)
        game.play("ENVIDO")
        # cpu accept envido... force random
        self.assertTrue(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['ENVIDO', 'ENVIDO'])

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ENVIDO')
    def test_cantar_fases_envido_envido_envido_accept(self, mock_ask_envido):
        game = Game()
        self.assertTrue(game.hand.envido_fase)
        game.play("ENVIDO")
        game.play("ACCEPTED")
        # cpu accept envido... force random
        self.assertFalse(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['ENVIDO', 'ENVIDO'])

    @unittest.mock.patch("truco.hand.Hand.sing_envido", return_value='ENVIDO')
    def test_cpu_cantar_fases_envido_and_accept(self, mock_sing_envido):
        game = Game()
        self.assertTrue(game.hand.envido_fase)
        game.play("0")
        # cpu accept envido... force random
        self.assertTrue(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['ENVIDO'])

    @unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='ENVIDO')
    @unittest.mock.patch("random.choice", return_value='ENVIDO')
    def test_cpu_cantar_fases_envido_and_accept(self, mock_random_choice_, mock_cpu_play):
        game = Game()
        self.assertTrue(game.hand.envido_fase)
        game.play("0")
        game.play("ACCEPTED")
        # cpu accept envido... force random
        self.assertFalse(game.hand.envido_fase)
        self.assertEqual(game.hand.envidos, ['ENVIDO'])

    def test_init(self):
        game = Game()
        self.assertEqual(game.players[0].score, 0)
        self.assertEqual(game.players[1].score, 0)

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ACCEPTED')
    def test_cantar_envido_gana_humano(self, mock_ask_envido):
        game = Game()
        game.hand.hidden_cards = [
            [Card(SWORD, 1), Card(CUP, 6), Card(CUP, 7)],
            [Card(COARSE, 4), Card(COARSE, 3), Card(COARSE, 2)],
        ]
        game.play("ENVIDO")
        # cpu accept envido... force random
        self.assertEqual(game.players[0].score, 2)
        self.assertEqual(game.players[1].score, 0)

    @unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ACCEPTED')
    def test_cantar_envido_gana_cpu(self, mock_ask_envido):
        game = Game()
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 3), Card(COARSE, 2)],
            [Card(SWORD, 1), Card(CUP, 6), Card(CUP, 7)],
        ]
        game.play("ENVIDO")
        # cpu accept envido... force random
        self.assertEqual(game.players[0].score, 0)
        self.assertEqual(game.players[1].score, 2)

    def test_cantar_truco_gana_humano(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(SWORD, 1), Card(CUP, 3), Card(CUP, 2)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        with unittest.mock.patch("truco.player.CPUPlayer.ask_trucos", return_value='ACCEPTED'):
            game.play("TRUCO")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        self.assertEqual(game.players[0].score, 2)
        self.assertEqual(game.players[1].score, 0)

    def test_cantar_truco_gana_pc(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(SWORD, 1), Card(CUP, 3), Card(CUP, 2)],
        ]
        with unittest.mock.patch("truco.player.CPUPlayer.ask_trucos", return_value='ACCEPTED'):
            game.play("TRUCO")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        self.assertEqual(game.players[0].score, 0)
        self.assertEqual(game.players[1].score, 2)

    def test_terminar_partida_gana_humano_por_envido(self):
        game = Game()
        for i in range(5):
            game.hand.hidden_cards = [
                [Card(CUP, 1), Card(CUP, 7), Card(CUP, 6)],
                [Card(SWORD, 4), Card(SWORD, 4), Card(SWORD, 4)],
            ]
            with unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ACCEPTED'):
                game.play("ENVIDO")
            with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
                game.play("0")
            with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
                game.play("0")

        self.assertEqual(game.players[1].score, 0)
        self.assertEqual(game.players[0].score, 15)
        self.assertEqual(game.is_playing, False)
        result = game.next_turn()
        self.assertEqual(result, "\nGame Over!")

    def test_terminar_partida_gana_pc_por_envido(self):
        game = Game()
        for i in range(5):
            game.hand.hidden_cards = [
                [Card(SWORD, 4), Card(SWORD, 4), Card(SWORD, 4)],
                [Card(CUP, 1), Card(CUP, 7), Card(CUP, 6)],
            ]
            with unittest.mock.patch("truco.player.CPUPlayer.ask_envido", return_value='ACCEPTED'):
                game.play("ENVIDO")
            with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
                game.play("0")
            with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
                game.play("0")

        self.assertEqual(game.players[1].score, 15)
        self.assertEqual(game.players[0].score, 0)
        self.assertEqual(game.is_playing, False)
        result = game.next_turn()
        self.assertEqual(result, "\nGame Over!")

    def test_terminar_partida_gana_humano_por_truco(self):
        game = Game()
        for i in range(8):
            game.hand.hidden_cards = [
                [Card(SWORD, 1), Card(CUP, 3), Card(CUP, 2)],
                [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            ]
            with unittest.mock.patch("truco.player.CPUPlayer.ask_trucos", return_value='ACCEPTED'):
                game.play("TRUCO")
            with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
                game.play("0")
            with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
                game.play("0")

        self.assertEqual(game.players[0].score, 16)
        self.assertEqual(game.players[1].score, 0)
        self.assertEqual(game.is_playing, False)
        result = game.next_turn()
        self.assertEqual(result, "\nGame Over!")

    def test_ganar_por_ser_mano_humano(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        self.assertEqual(game.players[0].score, 1)
        self.assertEqual(game.players[1].score, 0)

    def test_ganar_por_ser_mano_pc(self):
        game = Game()
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        with unittest.mock.patch("truco.player.CPUPlayer.cpu_play", return_value='JUGAR'):
            game.play("0")
        self.assertEqual(game.players[0].score, 1)
        self.assertEqual(game.players[1].score, 1)

    def test_tirar_fruta_al_play(self):
        game = Game()
        game.board
        result = game.play("D")
        self.assertEqual(result, "\nComando Erroneo")

    def test_mensaje_next_turn(self):
        game = Game()
        game.board
        result = game.next_turn()
        self.assertEqual(result,
                         "\nENVIDO: Para cantar envido \nTRUCO: Para cantar Truco \n0: Para jugar la primer carta \n1: Para jugar la segunda carta\n2: Para jugar la tercer carta")
