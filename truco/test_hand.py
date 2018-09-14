import unittest

from . import SWORD, COARSE, GOLD
from .card import Card
from .hand import Hand


class TestHand(unittest.TestCase):

    def test_raise_exception(self):
        hand = Hand()
        hand.truco_pending = True
        with self.assertRaises(Exception):
            hand.sing_truco('TRUCO')

    def test_truco_rejected_pending_is_false(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.reject_truco()
        self.assertFalse(hand.truco_pending)

    def test_get_vale_cuatro_points_accepted(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        hand.sing_truco('VALE_CUATRO')
        hand.accept_truco()
        self.assertEqual(hand.get_truco_points(), 4)

    def test_get_vale_cuatro_points_rejected(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        hand.sing_truco('VALE_CUATRO')
        hand.reject_truco()
        self.assertEqual(hand.get_truco_points(1), 3)

    def test_get_re_truco_points_accepted(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        self.assertEqual(hand.get_truco_points(), 3)

    def test_get_re_truco_points_rejected(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        self.assertEqual(hand.get_truco_points(), 3)

    def test_get_truco_points_accepted(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        self.assertEqual(hand.get_truco_points(), 2)

    def test_get_truco_points_rejected(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        self.assertEqual(hand.get_truco_points(1), 1)

    def test_sing_truco_reject(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.reject_truco()
        self.assertEqual(False, hand.is_playing)

    def test_sing_truco(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        self.assertEqual(hand.trucos, ['TRUCO'])

    def test_sing_Truco_change_truco_turn(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        self.assertEqual(hand.truco_turn, 1)
        self.assertTrue(hand.truco_pending)

    def test_sing_truco_and_accept_and_change_turn(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        self.assertFalse(hand.truco_pending)
        self.assertEqual(hand.truco_turn, 1)

    def test_sing_truco_and_then_retruco_and_change_turn(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        self.assertEqual(hand.truco_turn, 0)
        self.assertTrue(hand.truco_pending)

    def test_sing_truco_and_then_retruco_and_accept(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        self.assertEqual(hand.truco_turn, 0)
        self.assertFalse(hand.truco_pending)

    def test_sing_truco_and_then_retruco_and_vale_cuatro(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        hand.sing_truco('VALE_CUATRO')
        self.assertEqual(hand.truco_turn, 1)
        self.assertTrue(hand.truco_pending)

    def test_sing_truco_and_then_retruco_and_vale_cuatro_and_accept(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        hand.accept_truco()
        hand.sing_truco('RE_TRUCO')
        hand.accept_truco()
        hand.sing_truco('VALE_CUATRO')
        hand.accept_truco()
        self.assertEqual(hand.truco_turn, 1)
        self.assertFalse(hand.truco_pending)

    def test_sing_truco_vs_envido(self):
        hand = Hand()
        hand.sing_truco('TRUCO')
        self.assertFalse(hand.envido_fase)

    def test_envido_solved_True_two(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.accept_envido()
        self.assertTrue(hand.envido_solved)

    def test_envido_solved_false(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        self.assertFalse(hand.envido_solved)

    def test_envido_solved_true(self):
        hand = Hand()
        self.assertTrue(hand.envido_solved)

    def test_get_envido_points_ENVIDO_ENVIDO_REAL_ENVIDO_FALTA_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('ENVIDO')
        hand.sing_envido('REAL_ENVIDO')
        hand.sing_envido('FALTA_ENVIDO')
        self.assertEqual(99, hand.get_envido_points())
        self.assertEqual(7, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO_REAL_ENVIDO_FALTA_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('REAL_ENVIDO')
        hand.sing_envido('FALTA_ENVIDO')
        self.assertEqual(99, hand.get_envido_points())
        self.assertEqual(5, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO_ENVIDO_FALTA_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('ENVIDO')
        hand.sing_envido('FALTA_ENVIDO')
        self.assertEqual(99, hand.get_envido_points())
        self.assertEqual(4, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO_ENVIDO_REAL_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('ENVIDO')
        hand.sing_envido('REAL_ENVIDO')
        self.assertEqual(7, hand.get_envido_points())
        self.assertEqual(4, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO_FALTA_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('FALTA_ENVIDO')
        self.assertEqual(99, hand.get_envido_points())
        self.assertEqual(2, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO_REAL_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('REAL_ENVIDO')
        self.assertEqual(5, hand.get_envido_points())
        self.assertEqual(2, hand.get_envido_points(1))

    def test_get_envido_points_REAL_ENVIDO_FALTA_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('REAL_ENVIDO')
        hand.sing_envido('FALTA_ENVIDO')
        # import ipdb; ipdb.set_trace()
        self.assertEqual(99, hand.get_envido_points())
        self.assertEqual(2, hand.get_envido_points(1))

    def test_get_envido_points_FALTA_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('FALTA_ENVIDO')
        self.assertEqual(99, hand.get_envido_points())
        self.assertEqual(1, hand.get_envido_points(1))

    def test_get_envido_points_REAL_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('REAL_ENVIDO')
        self.assertEqual(3, hand.get_envido_points())
        self.assertEqual(1, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('ENVIDO')
        self.assertEqual(4, hand.get_envido_points())
        self.assertEqual(2, hand.get_envido_points(1))

    def test_get_envido_points_ENVIDO(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        self.assertEqual(2, hand.get_envido_points())
        self.assertEqual(1, hand.get_envido_points(1))

    def test_get_envido_winner_p0(self):
        hand = Hand()
        hand.hidden_cards = [[
            Card(COARSE, 1), Card(COARSE, 5), Card(COARSE, 6)], [
            Card(COARSE, 2), Card(COARSE, 3), Card(COARSE, 4)]]
        self.assertEqual(0, hand.get_envido_winner())

    def test_get_envido_winner_p1(self):
        hand = Hand()
        hand.hidden_cards = [[
            Card(COARSE, 2), Card(COARSE, 3), Card(COARSE, 4)],
            [Card(COARSE, 1), Card(COARSE, 5), Card(COARSE, 6)]]
        self.assertEqual(1, hand.get_envido_winner())

    def test_get_envido_winner_p0_for_mano(self):
        hand = Hand()
        hand.hidden_cards = [[
            Card(COARSE, 4), Card(COARSE, 3), Card(COARSE, 5)],
            [Card(SWORD, 1), Card(SWORD, 5), Card(SWORD, 4)]]
        self.assertEqual(0, hand.get_envido_winner())

    def test_get_envido_winner_p1_for_mano(self):
        hand = Hand(mano=1)
        hand.hidden_cards = [[
            Card(COARSE, 4), Card(COARSE, 3), Card(COARSE, 5)],
            [Card(SWORD, 1), Card(SWORD, 5), Card(SWORD, 4)]]
        self.assertEqual(1, hand.get_envido_winner())

    def test_hand_1(self):
        hand = Hand()
        self.assertEqual(3, len(hand.hidden_cards[0]))
        self.assertEqual(3, len(hand.hidden_cards[1]))
        self.assertEqual(0, len(hand.played_cards[0]))
        self.assertEqual(0, len(hand.played_cards[1]))
        hand.play_card(0)
        self.assertEqual(2, len(hand.hidden_cards[0]))
        self.assertEqual(3, len(hand.hidden_cards[1]))
        self.assertEqual(1, len(hand.played_cards[0]))
        self.assertEqual(0, len(hand.played_cards[1]))

    def test_hand_2(self):
        hand = Hand()
        self.assertEqual(3, len(hand.hidden_cards[0]))
        self.assertEqual(3, len(hand.hidden_cards[1]))
        self.assertEqual(0, len(hand.played_cards[0]))
        self.assertEqual(0, len(hand.played_cards[1]))

    def test_hand_envido(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 1), Card(COARSE, 5), Card(COARSE, 6)], [
            Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 31)

    def test_hand_envido_2_whites(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 1), Card(GOLD, 5), Card(COARSE, 6)], [
            Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 27)

    def test_hand_envido_1_white(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 1), Card(GOLD, 5), Card(SWORD, 6)], [
            Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 6)

    def test_hand_envido_3_blacks(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 10), Card(COARSE, 11), Card(COARSE, 12)], [
            Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 20)

    def test_hand_envido_2_blacks_1_white(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 10), Card(COARSE, 5), Card(COARSE, 11)], [
            Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 25)

    def test_hand_envido_high_card(self):
        hand = Hand()
        hand.hidden_cards = [[Card(GOLD, 1), Card(SWORD, 10), Card(COARSE, 6)], [
            Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 6)

    def test_play_one_card_player_one(self):
        hand = Hand()
        hand.deal_cards()
        hand.play_card(0)
        self.assertEqual(2, len(hand.hidden_cards[0]))

    def test_play_one_card_player_two(self):
        hand = Hand()
        hand.deal_cards()
        hand.turn = 1
        hand.play_card(0)
        self.assertEqual(2, len(hand.hidden_cards[1]))

    def test_play_two_card_player_two(self):
        hand = Hand()
        hand.deal_cards()
        hand.turn = 1
        hand.play_card(0)
        hand.turn = 1
        hand.play_card(0)
        self.assertEqual(1, len(hand.hidden_cards[1]))

    def test_play_two_card_player_one(self):
        hand = Hand()
        hand.deal_cards()
        hand.play_card(0)
        hand.turn = 0
        hand.play_card(0)
        self.assertEqual(1, len(hand.hidden_cards[0]))

    def test_play_two_card_player_one_played_cards(self):
        hand = Hand()
        hand.deal_cards()
        hand.play_card(0)
        hand.turn = 0
        hand.play_card(0)
        self.assertEqual(2, len(hand.played_cards[0]))

    def test_play_two_card_player_dos_played_cards(self):
        hand = Hand()
        hand.turn = 1
        hand.deal_cards()
        hand.play_card(0)
        hand.turn = 1
        hand.play_card(0)
        self.assertEqual(2, len(hand.played_cards[1]))

    def test_play_one_card_change_turn(self):
        hand = Hand()
        hand.deal_cards()
        hand.play_card(0)
        self.assertEqual(1, hand.turn)

    def test_play_two_card_change_turn_player_one_bigger(self):
        hand = Hand()
        hand.hidden_cards = [[Card(GOLD, 1),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(COARSE, 4),
                              Card(COARSE, 5),
                              Card(COARSE, 6)]]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()
        self.assertEqual(0, hand.turn)

    def test_play_two_card_change_turn_player_two_bigger(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 4),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(SWORD, 1),
                              Card(COARSE, 5),
                              Card(COARSE, 6)]]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()
        self.assertEqual(1, hand.turn)

    def test_play_two_card_change_turn_players_equals(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 4),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(SWORD, 4),
                              Card(COARSE, 5),
                              Card(COARSE, 6)]]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()
        self.assertEqual(0, hand.turn)

    def test_play_four_card_change_turn_players_equals(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 4),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(SWORD, 4),
                              Card(COARSE, 5),
                              Card(COARSE, 6)]]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        self.assertEqual(0, hand.turn)
        self.assertEqual(3, hand.number_hand)

    def test_play_six_card_change_turn_players_equals(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 5),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(SWORD, 4),
                              Card(SWORD, 1),
                              Card(COARSE, 7)]]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)

        self.assertEqual(1, hand.turn)
        self.assertEqual(3, hand.number_hand)

    def test_play_four_cards_is_playing_false(self):
        hand = Hand()
        hand.hidden_cards = [
            [Card(COARSE, 1), Card(SWORD, 1), Card(COARSE, 7)],
            [Card(COARSE, 5), Card(SWORD, 10), Card(COARSE, 6)],
        ]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        self.assertFalse(hand.is_playing)

    def test_play_four_cards_is_playing_false_two(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 5),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(COARSE, 1),
                              Card(SWORD, 1),
                              Card(COARSE, 7)]
                             ]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        self.assertFalse(hand.is_playing)

    def test_play_two_cards_is_playing_true(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 5),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(COARSE, 1),
                              Card(SWORD, 1),
                              Card(COARSE, 7)]]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()
        self.assertTrue(hand.is_playing)

    def test_show_cards(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 5),
                              Card(SWORD, 10),
                              Card(COARSE, 6)],
                             [Card(COARSE, 1),
                              Card(SWORD, 1),
                              Card(COARSE, 7)]]
        hand.play_card(0)
        hand.play_card(0)
        expected = '\nPlayed Cards: \nHuman: 5 basto \nComputer: 1 basto \n'
        result = hand.show_cards()
        self.assertEqual(result, expected)

    def test_play_six_cards_is_playing_false(self):
        hand = Hand()
        hand.hidden_cards = [
            [Card(COARSE, 5), Card(SWORD, 1), Card(COARSE, 6)],
            [Card(COARSE, 1), Card(SWORD, 10), Card(COARSE, 7)],
        ]
        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        hand.play_card(0)
        hand.play_card(0)
        hand.siguiente_ronda()
        hand.who_is_next()

        self.assertFalse(hand.is_playing)

    def test_get_response_envido_sing_envido(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        expect = ['ACCEPTED', 'REJECTED', 'FALTA_ENVIDO', 'REAL_ENVIDO', 'ENVIDO', ]
        result = hand.get_response_envido()
        self.assertEqual(expect, result)

    def test_get_response_envido_sing_envido_envido(self):
        hand = Hand()
        hand.sing_envido('ENVIDO')
        hand.sing_envido('ENVIDO')
        expect = ['ACCEPTED', 'REJECTED', 'FALTA_ENVIDO', 'REAL_ENVIDO', ]
        result = hand.get_response_envido()
        self.assertEqual(expect, result)

    def test_get_response_envido_sing_real_envido(self):
        hand = Hand()
        hand.sing_envido('REAL_ENVIDO')
        expect = ['ACCEPTED', 'REJECTED', 'FALTA_ENVIDO', ]
        result = hand.get_response_envido()
        self.assertEqual(expect, result)

    def test_get_response_envido_sing_falta_envido(self):
        hand = Hand()
        hand.sing_envido('FALTA_ENVIDO')
        expect = ['ACCEPTED', 'REJECTED', ]
        result = hand.get_response_envido()
        self.assertEqual(expect, result)
