import unittest

from . import SWORD, COARSE, GOLD
from .card import Card
from .hand import Hand


class TestHand(unittest.TestCase):

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
        expected = '\nMis Cartas: \n10 espada 6 basto \nCartas jugadas: \nH: 5 basto \nC: 1 basto \n'
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
