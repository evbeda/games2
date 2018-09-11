import unittest
from unittest.mock import patch
from .poker import (
    combine_card,
    better_hand,
    find_straight_flush,
    find_royal_flush,
    find_repeated_cards,
    find_flush,
    find_cards_suits,
    find_straight,
    sort_cards_by_number,
    compare_combinations,
    compare_hands,
    transform_cards_to_str,
    get_value,
    PREFLOP, FLOP, TURN, RIVER, SHOWDOWN,
    CHECK, BET, FOLD, RAISE, CALL, NONE,
    PLAYER, CPU,
    FIRST,
    SECOND,
    EQUAL,
    ROYAL_FLUSH,
    STRAIGHT_FLUSH,
    POKER,
    FULL_HOUSE,
    FLUSH,
    STRAIGHT,
    SET,
    DOUBLE_PAIR,
    PAIR,
    HIGH_CARD,
)
from .card import Card
from .deck import Deck
from .player import Player
from .game import PokerGame
from .hand import Hand


class PokerTest(unittest.TestCase):

    def test_card_repr(self):
        card = Card('K', 'h')
        result = card.__repr__()
        self.assertEqual(result, 'Kh')

    def test_royal_flush(self):
        # test
        result = find_royal_flush(['Ah', 'Kh', 'Qh', 'Jh', 'Th'])
        # assert
        self.assertTrue(result)

    def test_pares(self):
        # setup
        expected = {
            'poker': [],
            'trio': [],
            'par': ['3'],
        }
        # test
        result = find_repeated_cards(['Kh', '8d', '3c', '3d', '2s'])
        # assert
        self.assertEqual(result, expected)

    def test_trio(self):
        expected = {
            'poker': [],
            'trio': ['K'],
            'par': [],
        }
        result = find_repeated_cards(['Kh', 'Kd', 'Ks', '8h', 'Ts'])
        self.assertEqual(result, expected)

    def test_doblepair(self):
        expected = {
            'poker': [],
            'trio': [],
            'par': ['Q', '8'],
        }
        result = find_repeated_cards(['Qd', 'Qh', '8d', '8s', '4s'])
        self.assertEqual(result, expected)

    def test_poker(self):
        expected = {
            'poker': ['7'],
            'trio': [],
            'par': [],
        }
        result = find_repeated_cards(['7d', '7h', '7d', '7s', '4s'])
        self.assertEqual(result, expected)

    def test_color_true(self):
        result = find_flush(['Ad', '2d', '3d', '7d', '4d'])
        self.assertTrue(result)

    def test_color_false(self):
        result = find_flush(['Ah', '2d', '3d', '7d', '4d'])
        self.assertFalse(result)

    def test_full_house(self):
        expected = {
            'poker': [],
            'trio': ['6'],
            'par': ['T'],
        }
        result = find_repeated_cards(['6d', '6c', '6h', 'Ts', 'Td'])
        self.assertEqual(result, expected)

    def test_straight_true(self):
        result = find_straight(['2h', 'Ad', '3d', '4d', '5d'])
        self.assertTrue(result)

    def test_straight_as(self):
        result = find_straight(['Th', 'Ad', 'Kd', 'Jd', 'Qd'])
        self.assertTrue(result)

    def test_straight_flush_true(self):
        result = find_straight_flush(['2h', 'Ah', '3h', '4h', '5h'])
        self.assertTrue(result)

    def test_straight_flush_false_not_color(self):
        result = find_straight_flush(['2d', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_straight_flush_false_not_escalera(self):
        result = find_straight_flush(['8h', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_straight_flush_false_not_any(self):
        result = find_straight_flush(['8d', 'Ah', '3h', '4h', '5h'])
        self.assertFalse(result)

    def test_cards_suits(self):
        expected = ['3h', '4h', '5h', '8d', 'Ad']
        result = find_cards_suits(['8d', 'Ad', '3h', '4h', '5h'])
        self.assertEqual(result, expected)

    def test_sort_cards_by_number(self):
        expected = [3, 4, 5, 8, 14]
        result = sort_cards_by_number(['8d', 'Ad', '3h', '4h', '5h'])
        self.assertEqual(result, expected)

    def test_create_card(self):
        expected_value = '7'
        expected_suit = 'd'
        result = Card('7', 'd')
        self.assertEqual(result.value, expected_value)
        self.assertEqual(result.suit, expected_suit)

    def test_create_deck(self):
        expected_value = 52
        deck = Deck()
        result = len(deck.cards)
        self.assertEqual(result, expected_value)

    def test_deck_suits(self):
        resultD = 0
        resultS = 0
        resultH = 0
        resultC = 0
        expected_value = 13
        deck = Deck()
        for c in range(0, len(deck.cards)):
            if deck.cards[c].suit == 'd':
                resultD += 1
            if deck.cards[c].suit == 's':
                resultS += 1
            if deck.cards[c].suit == 'h':
                resultH += 1
            if deck.cards[c].suit == 'c':
                resultC += 1
        self.assertEqual(resultD, expected_value)
        self.assertEqual(resultS, expected_value)
        self.assertEqual(resultH, expected_value)
        self.assertEqual(resultC, expected_value)

    def test_deal_cards(self):
        expected_value = 3
        expected_deck_size = 52 - expected_value
        deck = Deck()
        result = deck.deal(expected_value)
        self.assertEqual(len(result), expected_value)
        self.assertEqual(len(deck.cards), expected_deck_size)

    def test_rebuid_deck(self):
        expected_value = 6
        expected_deck_size = 52
        deck = Deck()
        deck.deal(expected_value)
        deck.rebuild()
        self.assertEqual(len(deck.cards), expected_deck_size)

    def test_create_player(self):
        jugador_money = 10
        jugador = Player(jugador_money)
        cards_dealed = 2
        deck = Deck()
        jugador.cards = deck.deal(cards_dealed)
        self.assertEqual(len(jugador.cards), cards_dealed)
        self.assertEqual(jugador.money, jugador_money)

    def test_create_player_without_money(self):
        with self.assertRaises(Exception):
            Player(0)
        self.assertTrue('Player money must be greater than 0')

    def test_check_hand(self):
        player1_money = 1000
        player2_money = 2000
        player1 = Player(player1_money)
        player2 = Player(player2_money)

        def side_effect(cards):
            return cards
        with unittest.mock.patch('poker.deck.shuffle', side_effect):
            deck = Deck()
        player1.cards.append(deck.cards[48])
        player1.cards.append(deck.cards[49])
        player1.cards.append(deck.cards[50])
        player1.cards.append(deck.cards[28])
        player1.cards.append(deck.cards[38])
        player2.cards = deck.deal(5)

    def test_get_value_J_Q_K(self):
        self.assertEqual(get_value('J'), 11)
        self.assertEqual(get_value('Q'), 12)
        self.assertEqual(get_value('K'), 13)

    def test_21combinations(self):
        result = combine_card(['Ah', '2h', '5h', '6h', '7h', '8h', '9h'])
        self.assertEqual(len(result), 21)

    def test_first_combination(self):
        result = combine_card(['Ah', '2h', '5h', '6h', '7h', '8h', '9h'])
        self.assertEqual(result[0], ['Ah', '2h', '5h', '6h', '7h'])
        self.assertEqual(result[1], ['Ah', '2h', '5h', '6h', '8h'])
        self.assertEqual(result[2], ['Ah', '2h', '5h', '6h', '9h'])
        self.assertEqual(result[3], ['Ah', '2h', '5h', '7h', '8h'])
        self.assertEqual(result[4], ['Ah', '2h', '5h', '7h', '9h'])
        self.assertEqual(result[5], ['Ah', '2h', '5h', '8h', '9h'])
        self.assertEqual(result[6], ['Ah', '2h', '6h', '7h', '8h'])
        self.assertEqual(result[7], ['Ah', '2h', '6h', '7h', '9h'])
        self.assertEqual(result[8], ['Ah', '2h', '6h', '8h', '9h'])
        self.assertEqual(result[9], ['Ah', '2h', '7h', '8h', '9h'])
        self.assertEqual(result[10], ['Ah', '5h', '6h', '7h', '8h'])
        self.assertEqual(result[11], ['Ah', '5h', '6h', '7h', '9h'])
        self.assertEqual(result[12], ['Ah', '5h', '6h', '8h', '9h'])
        self.assertEqual(result[13], ['Ah', '5h', '7h', '8h', '9h'])
        self.assertEqual(result[14], ['Ah', '6h', '7h', '8h', '9h'])
        self.assertEqual(result[15], ['2h', '5h', '6h', '7h', '8h'])
        self.assertEqual(result[16], ['2h', '5h', '6h', '7h', '9h'])
        self.assertEqual(result[17], ['2h', '5h', '6h', '8h', '9h'])
        self.assertEqual(result[18], ['2h', '5h', '7h', '8h', '9h'])
        self.assertEqual(result[19], ['2h', '6h', '7h', '8h', '9h'])
        self.assertEqual(result[20], ['5h', '6h', '7h', '8h', '9h'])

    def test_best_hand_royal_flush(self):
        combination = combine_card(['Ah', 'Th', '5h', 'Jh', '7h', 'Qh', 'Kh'])
        result = better_hand(combination)
        self.assertEqual(result, (ROYAL_FLUSH, ['Ah', 'Th', 'Jh', 'Qh', 'Kh']))

    def test_poker_hand(self):
        combination = combine_card(['Ad', 'Ac', 'Th', 'Ts', 'Ah', '3d', 'As'])
        result = better_hand(combination)
        self.assertEqual(result, (POKER, ['Ad', 'Ac', 'Th', 'Ah', 'As']))

    def test_straight_flush_hand(self):
        combination = combine_card(['6d', 'Ac', 'Td', 'Ts', '7d', '8d', '9d'])
        result = better_hand(combination)
        self.assertEqual(result, (STRAIGHT_FLUSH, ['6d', 'Ac', 'Td', 'Ts', '9d']))

    def test_full_house_6_T_hand(self):
        combination = combine_card(['6d', '6c', '6h', 'Ts', 'Td', '8d', '9d'])
        result = better_hand(combination)
        self.assertEqual(result, (FULL_HOUSE, ['6d', '6c', '6h', 'Ts', 'Td']))

    def test_full_house_6_3_hand(self):
        combination = combine_card(['6d', '6c', '6h', '3s', '3d', '8d', '9d'])
        result = better_hand(combination)
        self.assertEqual(result, (FULL_HOUSE, ['6d', '6c', '6h', '3s', '3d']) )

    def test_one_pair_hand(self):
        combination = combine_card(['Jd', 'Jc', '6h', '2s', '7h', '8d', 'Ts'])
        result = better_hand(combination)
        self.assertEqual(result, (PAIR, ['Jd', 'Jc', '7h', '8d', 'Ts']))

    def test_player_wins(self):
        hand_1 = (FULL_HOUSE, ['6d', '6c', '6h', '3s', '3d'])
        hand_2 = (PAIR, ['Jd', 'Jc', '7h', '8d', 'Ts'])
        result = compare_hands(hand_1, hand_2)
        self.assertEqual(result, 'PLAYER WINS!')

    def test_cpu_wins(self):
        hand_1 = (FULL_HOUSE, ['6d', '6c', '6h', '3s', '3d'])
        hand_2 = (PAIR, ['Jd', 'Jc', '7h', '8d', 'Ts'])
        result = compare_hands(hand_2, hand_1)
        self.assertEqual(result, 'CPU WINS!')

    def test_player_cpu_tie(self):
        hand_1 = (FULL_HOUSE, ['6d', '6c', '6h', '3s', '3d'])
        result = compare_hands(hand_1, hand_1)
        self.assertEqual(result, 'TIE')

    def test_transform_card_to_str(self):
        cards = [Card(1, 'h'), Card(2, 'h'), Card(3, 'h'), Card(4, 'h'), Card(5, 'h')]
        expected = ['1h', '2h', '3h', '4h', '5h']
        result = transform_cards_to_str(cards)
        self.assertEqual(result, expected)

    def test_hand_deal_initial_cards(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        self.assertEqual(
            hand.stage,
            PREFLOP,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.cpu_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            0,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_deal_flop(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.next_stage()
        self.assertEqual(
            hand.stage,
            FLOP,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            3,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_deal_turn(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.next_stage()
        hand.next_stage()
        self.assertEqual(
            hand.stage,
            TURN,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            4,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_deal_river(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.next_stage()
        hand.next_stage()
        hand.next_stage()
        self.assertEqual(
            hand.stage,
            RIVER,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            5,
        )
        # ----
        # ronda apuestas o retira
        # ----

    def test_hand_showdown(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.next_stage()
        hand.next_stage()
        hand.next_stage()
        hand.next_stage()
        self.assertEqual(
            hand.stage,
            SHOWDOWN
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            5,
        )

    def test_hand_showdown_better_hand(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.next_stage()
        hand.next_stage()
        hand.next_stage()
        hand.next_stage()
        hand.next_stage()
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.player_cards),
            2,
        )
        self.assertEqual(
            len(hand.common_cards),
            5,
        )

    def test_player_check(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(CHECK)
        self.assertEqual(hand.turn, CPU)
        self.assertEqual(hand.last_action, CHECK)

    def test_player_check_cpu_check(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(CHECK)
        hand.take_action(CHECK)
        self.assertEqual(hand.turn, PLAYER)
        self.assertEqual(
            hand.stage,
            FLOP
        )
        self.assertEqual(hand.last_action, NONE)

    def test_player_bet(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(BET, 50)
        self.assertEqual(hand.turn, CPU)
        self.assertEqual(
            hand.stage,
            PREFLOP
        )
        self.assertEqual(hand.last_action, BET)
        self.assertEqual(hand.pot, 50)
        self.assertEqual(hand.last_bet, 50)

    def test_player_bet_cpu_call(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(BET, 50)
        hand.take_action(CALL)
        self.assertEqual(hand.turn, PLAYER)
        self.assertEqual(
            hand.stage,
            FLOP
        )
        self.assertEqual(hand.last_action, NONE)
        self.assertEqual(hand.pot, 100)
        self.assertEqual(hand.last_bet, 0)

    def test_player_bet_cpu_raise(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(BET, 50)
        hand.take_action(RAISE, 100)
        self.assertEqual(hand.turn, PLAYER)
        self.assertEqual(
            hand.stage,
            PREFLOP
        )
        self.assertEqual(hand.last_action, RAISE)
        self.assertEqual(hand.pot, 150)
        self.assertEqual(hand.last_bet, 50)

    def test_player_bet_cpu_raise_not_enough(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(BET, 50)
        result = hand.take_action(RAISE, 70)
        self.assertEqual(hand.turn, CPU)
        self.assertEqual(
            hand.stage,
            PREFLOP
        )
        self.assertEqual(hand.last_action, BET)
        self.assertEqual(hand.pot, 50)
        self.assertEqual(hand.last_bet, 50)
        self.assertEqual(result, "You must raise at least twice last bet")

    def test_player_bet_cpu_fold(self):
        players = []
        players.append(Player(100))
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(BET, 50)
        result = hand.take_action(FOLD)
        self.assertEqual(hand.last_action, BET)
        self.assertEqual(hand.pot, 50)
        self.assertEqual(result, "the player win")

    def test_compare_combinations_first(self):
        first_combination = ['2h', '7d', 'Kd', 'Tc', 'Ks']
        second_combination = ['Qs', '8h', '4d', 'Jc', '2s']
        result = compare_combinations(first_combination, second_combination)
        self.assertEqual(result, FIRST)

    def test_compare_combinations_second(self):
        first_combination = ['2h', '7d', 'Kd', 'Tc', 'Ks']
        second_combination = ['Qs', '8h', '4d', 'Jc', '2s']
        result = compare_combinations(second_combination, first_combination)
        self.assertEqual(result, SECOND)

    def test_compare_combinations_equal(self):
        first_combination = ['2h', '7d', 'Kd', 'Tc', 'Ks']
        result = compare_combinations(first_combination, first_combination)
        self.assertEqual(result, EQUAL)

    def test_reduce_bank_on_bet(self):
        players = []
        player = Player(100)
        players.append(player)
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(BET, 10)
        self.assertEqual(player.money, 90)

    def test_reduce_bank_on_raise(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(BET, 10)
        hand.take_action(RAISE, 30)
        self.assertEqual(cpu.money, 70)

    def test_bet_greater_than_money(self):
        players = []
        player = Player(100)
        players.append(player)
        players.append(Player(100))
        hand = Hand(players)
        result = hand.take_action(BET, 200)
        self.assertEqual(result, "You don't have enough money")

    def test_raise_greater_than_money(self):
        players = []
        player = Player(100)
        players.append(player)
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(CHECK)
        hand.take_action(BET, 50)
        result = hand.take_action(RAISE, 200)
        self.assertEqual(result, "You don't have enough money")

    def test_reduce_bank_on_call(self):
        players = []
        player = Player(100)
        players.append(player)
        players.append(Player(100))
        hand = Hand(players)
        hand.take_action(CHECK)
        hand.take_action(BET, 10)
        hand.take_action(CALL)
        self.assertEqual(player.money, 90)

    def test_reduce_cpu_bank_on_call(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(BET, 10)
        hand.take_action(CALL)
        self.assertEqual(cpu.money, 90)

    def test_player_fold(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(BET, 10)
        hand.take_action(RAISE, 30)
        hand.take_action(FOLD)
        self.assertEqual(cpu.money, 110)

    def test_cpu_fold(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(BET, 10)
        hand.take_action(RAISE, 30)
        hand.take_action(RAISE, 80)
        hand.take_action(FOLD)
        self.assertEqual(player.money, 130)

    def test_possible_action_after_check(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(CHECK)
        result = hand.possibles_actions()
        self.assertEqual(result, [CHECK, BET])

    def test_possible_action_after_bet(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(BET, 50)
        result = hand.possibles_actions()
        self.assertEqual(result, [CALL, RAISE, FOLD])

    def test_possible_action_after_raise(self):
        players = []
        player = Player(100)
        cpu = Player(100)
        players.append(player)
        players.append(cpu)
        hand = Hand(players)
        hand.take_action(BET, 20)
        hand.take_action(RAISE, 50)
        result = hand.possibles_actions()
        self.assertEqual(result, [CALL, RAISE, FOLD])

class PokerGameTest(unittest.TestCase):
    def test_player_no_money_money(self):
        game = PokerGame()
        game.player.money = 0
        self.assertEqual(game.player_no_money(), 'Player loses')

    def test_player_no_money(self):
        game = PokerGame()
        game.cpu.money = 0
        self.assertEqual(game.player_no_money(), 'CPU loses')

    def test_players_with_money(self):
        game = PokerGame()
        self.assertFalse(game.player_no_money())

    def test_next_turn_player_no_money(self):
        game = PokerGame()
        game.player.money = 0
        self.assertEqual(game.next_turn(), 'Player loses')

    def test_next_turn_cpu_no_money(self):
        game = PokerGame()
        game.cpu.money = 0
        self.assertEqual(game.next_turn(), 'CPU loses')

if __name__ == "__main__":
    unittest.main()
