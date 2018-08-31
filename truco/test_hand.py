import unittest
from .card import Card
from .deck import Deck
from . import SWORD, COARSE, GOLD, CUP
from .hand import Hand


class TestHand(unittest.TestCase):

    def test_hand_1(self):
        hand = Hand()
        self.assertEqual(3, len(hand.hidden_cards[0]))
        self.assertEqual(3, len(hand.hidden_cards[1]))
        self.assertEqual(0, len(hand.played_cards[0]))
        self.assertEqual(0, len(hand.played_cards[1]))
        self.assertEqual(0, hand.points)
        self.assertTrue(hand.envido)
        # ---------------
        # jugador uno tira la carta 0
        hand.play_card(0)
        # es mano 1?
        # es fase envido?
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
        self.assertEqual(0, hand.points)
        self.assertTrue(hand.envido)

    def test_hand_envido(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 1), Card(COARSE, 5), Card(COARSE, 6)], [Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 31)

    def test_hand_envido_2_whites(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 1), Card(GOLD, 5), Card(COARSE, 6)], [Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 27)

    def test_hand_envido_1_white(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 1), Card(GOLD, 5), Card(SWORD, 6)], [Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 6)

    def test_hand_envido_3_blacks(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 10), Card(COARSE, 11), Card(COARSE, 12)], [Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 20)

    def test_hand_envido_2_blacks_1_white(self):
        hand = Hand()
        hand.hidden_cards = [[Card(COARSE, 10), Card(COARSE, 5), Card(COARSE, 11)], [Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
        result = hand.get_score_envido(0)
        self.assertEqual(result, 25)

    def test_hand_envido_high_card(self):
        hand = Hand()
        hand.hidden_cards = [[Card(GOLD, 1), Card(SWORD, 10), Card(COARSE, 6)], [Card(COARSE, 5), Card(COARSE, 5), Card(COARSE, 5)]]
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
