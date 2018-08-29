import unittest
from unittest.mock import patch

from .card import Card
from .deck import Deck
from . import SWORD, COARSE, GOLD, CUP
from .player import Player
from .game import Game


class TestCantos(unittest.TestCase):
    player01 = Player('1')
    player02 = Player('2')

    def test_envido_player_01(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_envido(0, "Envido")
        self.assertEqual(resultado, ["1", "Envido"])

    def test_not_envido_player_02(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_envido(1, "Envido")
        self.assertEqual(resultado, None)

    def test_envido_player_02(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.played_cards.append(self.player01.hidden_cards[1])
        resultado = game.cantos_envido(1, "Envido")
        self.assertEqual(resultado, ["2", "Envido"])

    def test_real_envido_player_01(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_real_envido(0, "Real Envido")
        self.assertEqual(resultado, ["1", "Real Envido"])

    def test_not_real_envido_player_02(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_real_envido(1, "Real Envido")
        self.assertEqual(resultado, None)

    def test_real_envido_player_02(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.played_cards.append(self.player01.hidden_cards[1])
        resultado = game.cantos_real_envido(1, "Real Envido")
        self.assertEqual(resultado, ["2", "Real Envido"])

    def test_falta_envido_player_01(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_falta_envido(0, "Falta Envido")
        self.assertEqual(resultado, ["1", "Falta Envido"])

    def test_not_falta_envido_player_02(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_falta_envido(1, "Falta Envido")
        self.assertEqual(resultado, None)

    def test_falta_envido_player_02(self):
        deck = Deck()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.played_cards.append(self.player01.hidden_cards[1])
        resultado = game.cantos_falta_envido(1, "Falta Envido")
        self.assertEqual(resultado, ["2", "Falta Envido"])

    def test_calcular_envido_pintas_iguales(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Card(SWORD, 1), Card(
            SWORD, 10), Card(SWORD, 4)]
        player2.hidden_cards = [
            Card(COARSE, 1), Card(COARSE, 5), Card(COARSE, 2)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [25, 27])

    def test_calcular_envido_pintas_iguales_2(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Card(SWORD, 10), Card(
            SWORD, 11), Card(SWORD, 12)]
        player2.hidden_cards = [
            Card(COARSE, 10), Card(COARSE, 12), Card(COARSE, 5)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [20, 25])

    def test_calcular_envido_pintas_iguales_3(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Card(SWORD, 1), Card(SWORD, 2), Card(SWORD, 3)]
        player2.hidden_cards = [
            Card(COARSE, 1), Card(COARSE, 10), Card(COARSE, 5)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [25, 26])

    def test_calcular_envido_pintas_iguales_4(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Card(SWORD, 10), Card(
            SWORD, 12), Card(SWORD, 3)]
        player2.hidden_cards = [
            Card(COARSE, 11), Card(COARSE, 10), Card(COARSE, 12)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [23, 20])

    def test_calcular_envido_2_iguales(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Card(SWORD, 2), Card(GOLD, 12), Card(SWORD, 3)]
        player2.hidden_cards = [Card(COARSE, 11), Card(
            SWORD, 10), Card(COARSE, 12)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [25, 20])

    def test_calcular_envido_2_iguales_2(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Card(SWORD, 10), Card(
            COARSE, 12), Card(SWORD, 11)]
        player2.hidden_cards = [Card(COARSE, 5), Card(
            SWORD, 10), Card(COARSE, 12)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [20, 25])

    def test_calcular_envido_2_iguales_3(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Card(CUP, 10), Card(
            SWORD, 12), Card(SWORD, 3)]
        player2.hidden_cards = [
            Card(COARSE, 1), Card(CUP, 3), Card(COARSE, 5)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [23, 26])

    def test_calcular_envido_2_iguales_4(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Card(SWORD, 10), Card(SWORD, 1), Card(COARSE, 1)]
        player2.hidden_cards = [
            Card(COARSE, 6), Card(CUP, 10), Card(COARSE, 7)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [21, 33])

    def test_return_board(self):
        deck = Deck()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Card(SWORD, 10), Card(SWORD, 1), Card(COARSE, 1)]
        player2.hidden_cards = [
            Card(COARSE, 6), Card(CUP, 10), Card(COARSE, 7)]
        game = Game([player1, player2], deck)
        game.change_hand()
        result = game.board()
        self.assertEqual(result, 'Cartas en mano: 6 basto, 10 copa, 7 basto,  \n Cartas jugadas: ')
