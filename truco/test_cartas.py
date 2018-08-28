import unittest
from unittest.mock import patch

from .carta import Carta
from .mazo import Mazo
from . import ESPADA, BASTO, ORO, COPA
from .player import Player
from .game import Game


class TestCartas (unittest.TestCase):

    def test_eq_cards(self):
        carta_uno = Carta(ESPADA, 10)
        carta_dos = Carta(ESPADA, 10)
        result = carta_uno.__eq__(carta_dos)
        self.assertTrue(result)

    def test_eq_cards_false(self):
        carta_uno = Carta(ESPADA, 10)
        carta_dos = Carta(ESPADA, 9)
        result = carta_uno.__eq__(carta_dos)
        self.assertFalse(result)

    def test_play_card(self):
        player = Player('Leo')
        player.hidden_cards = [Carta(ESPADA, 10),
                               Carta(ESPADA, 11),
                               Carta(ESPADA, 12)
                               ]
        player.play_card(0)
        expected = Carta(ESPADA, 10)
        self.assertEqual(expected, player.played_cards[0])

    def test_play_card_not_empty(self):
        player = Player('Leo')
        player.hidden_cards = [Carta(ESPADA, 10),
                               Carta(ESPADA, 11),
                               Carta(ESPADA, 12)
                               ]
        player.play_card(0)
        self.assertEqual(len(player.played_cards), 1)

    def test_show_hand_to_board(self):
        player = Player('Leo')
        player.hidden_cards = [Carta(ESPADA, 10),
                               Carta(ESPADA, 11),
                               Carta(ESPADA, 12)
                               ]
        expected = "Cartas en mano: 10 espada, 11 espada, 12 espada,  \n Cartas jugadas: "
        self.assertEqual(expected, player.show_hand_to_board())

    def test_show_hand_to_board_one_played(self):
        player = Player('Leo')
        player.hidden_cards = [Carta(ESPADA, 10),
                               Carta(ESPADA, 11),
                               Carta(ESPADA, 12)
                               ]
        player.play_card(1)
        expected = "Cartas en mano: 10 espada, 12 espada,  \n Cartas jugadas: 11 espada, "
        self.assertEqual(expected, player.show_hand_to_board())

    # CREACIONES
    def test_si_se_crea_carta(self):
        carta1 = Carta(ESPADA, 1)
        self.assertIsInstance(carta1, Carta)
    # POSICIONES

    def test_obtener_posicion_cero(self):
        cartaMacho = Carta(ESPADA, 1)
        self.assertEqual(cartaMacho.get_position(), 0)

    def test_obtener_posicion_uno(self):
        cartaMacho = Carta(BASTO, 1)
        self.assertEqual(cartaMacho.get_position(), 1)

    def test_obtener_posicion_trece(self):
        cartaMacho = Carta(ESPADA, 4)
        self.assertEqual(cartaMacho.get_position(), 13)

    # COMPARACIONES
    def test_comparar_as_espadas_con_as_bastos(self):
        carta1 = Carta(ESPADA, 1)
        carta2 = Carta(BASTO, 1)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'GREATER')

    def test_comparar_4_de_espadas_con_4_de_bastos(self):
        carta1 = Carta(ESPADA, 4)
        carta2 = Carta(BASTO, 4)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'EQUAL')

    def test_comparar_7_de_espadas_con_7_de_bastos(self):
        carta1 = Carta(ESPADA, 7)
        carta2 = Carta(BASTO, 7)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'GREATER')

    def test_comparar_5_de_espadas_con_2_de_bastos(self):
        carta1 = Carta(ESPADA, 5)
        carta2 = Carta(BASTO, 2)
        result = carta1.compare_with(carta2)
        self.assertEqual(result, 'LOWER')

    def test_to_string(self):
        carta1 = Carta(ESPADA, 5)
        self.assertEqual(carta1.__str__(), "5 espada")


class TestMazo(unittest.TestCase):
    def test_repartir_cartas_uno(self):
        mazo = Mazo()
        result = mazo.get_card()
        self.assertIsInstance(result, Carta)

    def test_repartir_dos_cartas_distintas(self):
        mazo = Mazo()
        result1 = mazo.get_card()
        result2 = mazo.get_card()
        self.assertNotEqual(result1, result2)

    def test_contar_cartas_del_mazo_repartiendo_dos(self):
        mazo = Mazo()
        mazo.get_card()
        mazo.get_card()
        self.assertEqual(len(mazo.mazo), 38)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Mazo()
        mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Carta('basto', 1)
        self.assertEqual(cartaCorrecta.suit, result2.suit)
        self.assertEqual(cartaCorrecta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_4(self, mock_rand_int):
        mock_rand_int.return_value = 0
        mazo = Mazo()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Carta('oro', 7)
        self.assertEqual(cartaCorrecta.suit, result2.suit)
        self.assertEqual(cartaCorrecta.number, result2.number)

    @unittest.mock.patch('random.randint')
    def test_verificar_cartas_sacadas_2_de_a_4(self, mock_rand_int):
        mock_rand_int.return_value = 4
        mazo = Mazo()
        result2 = mazo.get_card()
        result2 = mazo.get_card()
        cartaCorrecta = Carta('basto', 3)
        self.assertEqual(cartaCorrecta.number, result2.number)
        self.assertEqual(cartaCorrecta.suit, result2.suit)

    def test_states(self):
        player01 = Player('1')
        player02 = Player('2')
        deck = Mazo()
        game = Game([player01, player02], deck)
        game.deal()
        self.assertEqual(game.get_state(), [0, None, None, None, None])


class TestGame(unittest.TestCase):
    player01 = Player('1')
    player02 = Player('2')

    def test_deal_cards(self):
        # setup
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        # test
        game.deal()
        # assert
        self.assertEqual(len(self.player01.hidden_cards), 3)
        self.assertEqual(len(self.player02.hidden_cards), 3)

    def test_reset_hand(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.play_card(1)
        self.player01.reset_hand()
        self.assertEqual(len(self.player01.hidden_cards), 0)
        self.assertEqual(len(self.player01.played_cards), 0)

    def test_change_hand(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.play_card(0)
        self.player02.play_card(0)
        game.deal()
        self.assertFalse(self.player01.is_hand)
        self.assertTrue(self.player02.is_hand)

    def test_play_first_card_p1(self):
        del self.player01.hidden_cards[:]
        del self.player01.played_cards[:]
        carta_0 = Carta(ESPADA, 3)
        carta_1 = Carta(BASTO, 7)
        carta_2 = Carta(ESPADA, 5)
        self.player01.hidden_cards = [carta_0, carta_1, carta_2]
        # test
        self.player01.play_card(1)
        # assert
        self.assertEqual(
            self.player01.hidden_cards,
            [carta_0, carta_2],
        )
        self.assertEqual(
            self.player01.played_cards,
            [carta_1]
        )

    def test_who_is_next_greater_p1(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.hidden_cards = []
        carta_0 = Carta(ESPADA, 3)
        carta_1 = Carta(BASTO, 7)
        carta_2 = Carta(ESPADA, 5)
        self.player01.hidden_cards = [carta_0, carta_1, carta_2]
        self.player01.play_card(1)
        carta_3 = Carta(ORO, 2)
        carta_4 = Carta(BASTO, 4)
        carta_5 = Carta(COPA, 5)
        self.player02.hidden_cards = []
        self.player02.hidden_cards = [carta_3, carta_4, carta_5]
        self.player02.play_card(1)
        result = game.who_is_next()
        self.assertEqual(result, "PLAYER1")

    def test_who_is_next_same_card_p2(self):
        deck = Mazo()
        self.player01 = Player('1')
        self.player02 = Player('2')
        game = Game([self.player01, self.player02], deck)

        game.deal()
        game.deal()
        self.player01.reset_hand()
        self.player02.reset_hand()

        carta_0 = Carta(ESPADA, 3)
        carta_1 = Carta(BASTO, 7)
        carta_2 = Carta(ESPADA, 5)
        self.player01.hidden_cards = [carta_0, carta_1, carta_2]
        self.player01.play_card(0)

        carta_3 = Carta(ORO, 3)
        carta_4 = Carta(BASTO, 4)
        carta_5 = Carta(COPA, 5)
        self.player02.hidden_cards = [carta_3, carta_4, carta_5]
        self.player02.play_card(0)

        result = game.who_is_next()
        self.assertEqual(result, "PLAYER2")


class test_cantos(unittest.TestCase):
    player01 = Player('1')
    player02 = Player('2')

    def test_envido_player_01(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_envido(0, "Envido")
        self.assertEqual(resultado, ["1", "Envido"])

    def test_not_envido_player_02(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_envido(1, "Envido")
        self.assertEqual(resultado, None)

    def test_envido_player_02(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.played_cards.append(self.player01.hidden_cards[1])
        resultado = game.cantos_envido(1, "Envido")
        self.assertEqual(resultado, ["2", "Envido"])

    def test_real_envido_player_01(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_real_envido(0, "Real Envido")
        self.assertEqual(resultado, ["1", "Real Envido"])

    def test_not_real_envido_player_02(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_real_envido(1, "Real Envido")
        self.assertEqual(resultado, None)

    def test_real_envido_player_02(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.played_cards.append(self.player01.hidden_cards[1])
        resultado = game.cantos_real_envido(1, "Real Envido")
        self.assertEqual(resultado, ["2", "Real Envido"])

    def test_falta_envido_player_01(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_falta_envido(0, "Falta Envido")
        self.assertEqual(resultado, ["1", "Falta Envido"])

    def test_not_falta_envido_player_02(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        resultado = game.cantos_falta_envido(1, "Falta Envido")
        self.assertEqual(resultado, None)

    def test_falta_envido_player_02(self):
        deck = Mazo()
        game = Game([self.player01, self.player02], deck)
        game.deal()
        self.player01.played_cards.append(self.player01.hidden_cards[1])
        resultado = game.cantos_falta_envido(1, "Falta Envido")
        self.assertEqual(resultado, ["2", "Falta Envido"])

    def test_calcular_envido_pintas_iguales(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Carta(ESPADA, 1), Carta(
            ESPADA, 10), Carta(ESPADA, 4)]
        player2.hidden_cards = [
            Carta(BASTO, 1), Carta(BASTO, 5), Carta(BASTO, 2)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [25, 27])

    def test_calcular_envido_pintas_iguales_2(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Carta(ESPADA, 10), Carta(
            ESPADA, 11), Carta(ESPADA, 12)]
        player2.hidden_cards = [
            Carta(BASTO, 10), Carta(BASTO, 12), Carta(BASTO, 5)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [20, 25])

    def test_calcular_envido_pintas_iguales_3(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Carta(ESPADA, 1), Carta(ESPADA, 2), Carta(ESPADA, 3)]
        player2.hidden_cards = [
            Carta(BASTO, 1), Carta(BASTO, 10), Carta(BASTO, 5)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [25, 26])

    def test_calcular_envido_pintas_iguales_4(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Carta(ESPADA, 10), Carta(
            ESPADA, 12), Carta(ESPADA, 3)]
        player2.hidden_cards = [
            Carta(BASTO, 11), Carta(BASTO, 10), Carta(BASTO, 12)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [23, 20])

    def test_calcular_envido_2_iguales(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Carta(ESPADA, 2), Carta(ORO, 12), Carta(ESPADA, 3)]
        player2.hidden_cards = [Carta(BASTO, 11), Carta(
            ESPADA, 10), Carta(BASTO, 12)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [25, 20])

    def test_calcular_envido_2_iguales_2(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Carta(ESPADA, 10), Carta(
            BASTO, 12), Carta(ESPADA, 11)]
        player2.hidden_cards = [Carta(BASTO, 5), Carta(
            ESPADA, 10), Carta(BASTO, 12)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [20, 25])

    def test_calcular_envido_2_iguales_3(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [Carta(COPA, 10), Carta(
            ESPADA, 12), Carta(ESPADA, 3)]
        player2.hidden_cards = [
            Carta(BASTO, 1), Carta(COPA, 3), Carta(BASTO, 5)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [23, 26])

    def test_calcular_envido_2_iguales_4(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Carta(ESPADA, 10), Carta(ESPADA, 1), Carta(BASTO, 1)]
        player2.hidden_cards = [
            Carta(BASTO, 6), Carta(COPA, 10), Carta(BASTO, 7)]
        game = Game([player1, player2], deck)
        resultado = game.comparar_puntos()
        self.assertEqual(resultado, [21, 33])

    def test_return_board(self):
        deck = Mazo()
        player1 = Player('1')
        player2 = Player('2')
        player1.hidden_cards = [
            Carta(ESPADA, 10), Carta(ESPADA, 1), Carta(BASTO, 1)]
        player2.hidden_cards = [
            Carta(BASTO, 6), Carta(COPA, 10), Carta(BASTO, 7)]
        game = Game([player1, player2], deck)
        game.change_hand()
        result = game.board()
        self.assertEqual(result, 'Cartas en mano: 6 basto, 10 copa, 7 basto,  \n Cartas jugadas: ')


if __name__ == '__main__':
    unittest.main()
