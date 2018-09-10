import unittest

from truco import *
from truco.card import Card
from truco.game import Game


class TestGame(unittest.TestCase):
    def test_cantar_envido_gana_humano(self):
        game = Game()
        game.hand.hidden_cards = [
            [Card(SWORD, 1), Card(CUP, 6), Card(CUP, 7)],
            [Card(COARSE, 4), Card(COARSE, 3), Card(COARSE, 2)]
        ]
        game.play("E")
        self.assertEqual(game.players[0].score, 2)
        self.assertEqual(game.players[1].score, 0)

    def test_cantar_envido_gana_pc(self):
        game = Game()
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 3), Card(COARSE, 2)],
            [Card(SWORD, 1), Card(CUP, 6), Card(CUP, 7)],
        ]
        game.play("E")
        self.assertEqual(game.players[0].score, 0)
        self.assertEqual(game.players[1].score, 2)

    def test_cantar_truco_gana_humano(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(SWORD, 1), Card(CUP, 3), Card(CUP, 2)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        game.play("T")
        game.board
        game.play("0")
        game.board
        game.play("0")
        game.board
        game.play("0")
        game.board
        self.assertEqual(game.players[0].score, 2)
        self.assertEqual(game.players[1].score, 0)

    def test_cantar_truco_gana_pc(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(SWORD, 1), Card(CUP, 3), Card(CUP, 2)],
        ]
        game.play("T")
        game.board
        game.play("0")
        game.board
        game.play("0")
        game.board
        game.play("0")
        game.board
        self.assertEqual(game.players[0].score, 0)
        self.assertEqual(game.players[1].score, 2)

    def test_terminar_partida_gana_humano_por_envido(self):
        game = Game()
        for i in range(10):
            game.board
            game.hand.hidden_cards = [
                [Card(CUP, 4), Card(CUP, 7), Card(CUP, 6)],
                [Card(SWORD, 1), Card(SWORD, 7), Card(SWORD, 5)],
            ]
            game.play("E")
            game.play("0")
            game.play("0")
        self.assertEqual(game.players[0].score, 20)
        self.assertEqual(game.players[1].score, 10)
        self.assertEqual(game.is_playing, False)
        result = game.next_turn()
        self.assertEqual(result, "\nGame Over!")

    def test_terminar_partida_gana_pc_por_envido(self):
        game = Game()
        for i in range(10):
            game.board
            game.hand.hidden_cards = [
                [Card(SWORD, 1), Card(SWORD, 1), Card(COARSE, 4)],
                [Card(SWORD, 4), Card(CUP, 7), Card(CUP, 6)],
            ]
            game.play("E")
            game.play("0")
            game.play("0")
        self.assertEqual(game.players[1].score, 20)
        self.assertEqual(game.players[0].score, 10)
        self.assertEqual(game.is_playing, False)

    def test_terminar_partida_gana_humano_por_truco(self):
        game = Game()
        for i in range(10):
            game.board
            game.hand.hidden_cards = [
                [Card(SWORD, 1), Card(CUP, 3), Card(CUP, 2)],
                [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            ]
            game.play("T")
            game.play("0")
            game.play("0")
        self.assertEqual(game.players[0].score, 20)
        self.assertEqual(game.players[1].score, 0)
        self.assertEqual(game.is_playing, False)

    def test_ganar_por_ser_mano_humano(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        game.play("0")
        game.play("0")
        game.play("0")
        self.assertEqual(game.players[0].score, 1)
        self.assertEqual(game.players[1].score, 0)

    def test_ganar_por_ser_mano_pc(self):
        game = Game()
        game.board
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        game.play("0")
        game.play("0")
        game.play("0")
        game.board
        game.hand.hidden_cards = [
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
            [Card(COARSE, 4), Card(COARSE, 4), Card(COARSE, 4)],
        ]
        game.play("0")
        game.play("0")
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
                         "\nE: Para cantar envido \nT: Para cantar Truco \n0: Para jugar la primer carta \n1: Para jugar la segunda carta\n2: Para jugar la tercer carta")
