import unittest
from . import cardsDictionary, colorDictionary
from .game import Game
from .player import Player
from .hand import Hand
from .deck import Deck


class TestBets(unittest.TestCase):
    player_name = 'John'
    # Bet tests

    def test_bet_equal(self):
        bet = 50
        game = Game()
        game.start_game()
        result = game.check_bet(bet)
        self.assertEqual(result, 'NEW ROUND!')

    def test_bet_upper(self):
        bet = 120
        game = Game()
        game.start_game()
        result = game.check_bet(bet)
        self.assertEqual(result, 'You dont have enough money')

    def test_bet_lower_than_min_bet(self):
        bet = 1
        game = Game()
        game.start_game()
        result = game.check_bet(bet)
        self.assertEqual(result, 'The bet is too low, the min bet is 5')

    def test_bet_win_no_blackjack(self):
        player = Player(self.player_name, 10)
        game = Game()
        game.min_bet = 5
        player.balance(game.min_bet)
        game.pot += game.min_bet
        player.win(game.pot)
        self.assertEqual(player.money, 15)

    def test_check_you_can_bet_true(self):
        player = Player(self.player_name, 20)
        game = Game()
        game.player = player
        game.min_bet = 10
        result = game.check_you_can_bet()
        self.assertTrue(result)

    def test_check_you_can_bet_false(self):
        player = Player(self.player_name, 5)
        game = Game()
        game.min_bet = 10
        game.player = player
        result = game.check_you_can_bet()
        self.assertFalse(result)


class TestHands(unittest.TestCase):
    def test_deal_card(self):
        value = ['3d']
        hand = Hand()
        hand.deal_card(value)
        result = value[0] in hand.cards
        self.assertTrue(result)

    def test_card_value_update(self):
        hand = Hand()
        hand.value = 5
        hand.deal_card(['Ah'])
        result = hand.value
        self.assertEqual(result, 16)
    # Sum Cards tests

    def test_cards_sum_normal(self):
        hand = Hand()
        hand.deal_card(['2h', 'Jh'])
        result = hand.value
        self.assertEqual(result, 12)

    def test_as_count_one(self):
        hand = Hand()
        hand.deal_card(['8h', '3d', 'Ah'])
        result = hand.value
        self.assertEqual(result, 12)


class TestDeck(unittest.TestCase):
    def test_create_deck(self):
        deck = Deck(cardsDictionary, colorDictionary)
        result = len(deck.cards)
        self.assertEqual(result, 52)

    def test_shuffle_deck(self):
        deck = Deck(cardsDictionary, colorDictionary)
        initial_cards = deck.cards
        deck.shuffle()
        result = False
        for i in range(len(deck.cards)):
            if initial_cards[i] != deck.cards[i]:
                result = False
            result = True
        self.assertTrue(result)

    def test_reduce_len_when_deal(self):
        deck = Deck(cardsDictionary, colorDictionary)
        initial_len = len(deck.cards)
        deck.deal(2)
        result = len(deck.cards)
        expected = initial_len - 2
        self.assertEqual(expected, result)

    def test_remove_card_when_deal(self):
        deck = Deck(cardsDictionary, colorDictionary)
        cards = deck.deal(2)
        result = [cards in deck.cards]
        self.assertTrue(result)


class TestGame(unittest.TestCase):
    def test_player_has_two_initial_cards(self):
        game = Game()
        game.start_game()
        result = len(game.player.hand.cards)
        self.assertEqual(result, 2)

    def test_dealer_has_two_initial_cards(self):
        game = Game()
        game.start_game()
        result = len(game.dealer_hand.cards)
        self.assertEqual(result, 2)

    def test_dealer_has_BJ_first(self):
        game = Game()
        game.start_game()
        game.dealer_hand.cards = ['Ah', 'Jd']
        game.dealer_hand.value = 21
        game.player.hand.cards = ['Ad', '8d']
        game.player.hand.value = 18
        result = game.who_wins()
        self.assertEqual('Dealer Wins!', result)

    def test_both_have_BJ_first(self):
        game = Game()
        game.start_game()
        game.dealer_hand.cards = ['Ah', 'Jd']
        game.dealer_hand.value = 21
        game.player.hand.cards = ['Ad', 'Jh']
        game.player.hand.value = 21
        result = game.who_wins()
        self.assertEqual('TIE!', result)

    def test_player_has_BJ_first(self):
        game = Game()
        game.start_game()
        game.dealer_hand.cards = ['Ah', '8d']
        game.dealer_hand.value = 18
        game.player.hand.cards = ['Ad', 'Jh']
        game.player.hand.value = 21
        result = game.who_wins()
        self.assertEqual('Player Wins!', result)

    def test_player_has_more_than_21(self):
        game = Game()
        game.start_game()
        game.dealer_hand.cards = ['Kd', '7d', '3d']
        game.dealer_hand.value = 20
        game.player.hand.cards = ['Kd', 'Jh', '7d']
        game.player.hand.value = 27
        result = game.who_wins()
        self.assertEqual('Dealer Wins!', result)

    def test_dealer_has_more_than_21(self):
        game = Game()
        game.start_game()
        game.player.hand.cards = ['Kd', '7d', '3d']
        game.player.hand.value = 20
        game.dealer_hand.cards = ['Kd', 'Jh', '7d']
        game.dealer_hand.value = 27
        result = game.who_wins()
        self.assertEqual('Player Wins!', result)

    def test_dealer_has_better_hand(self):
        game = Game()
        game.start_game()
        game.dealer_hand.cards = ['Kd', '7d', '3d']
        game.dealer_hand.value = 20
        game.player.hand.cards = ['Kd', '8d']
        game.player.hand.value = 18
        result = game.who_wins()
        self.assertEqual('Dealer Wins!', result)

    def test_player_has_better_hand(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['Kd', '7d', '3d']
        game.player.hand.value = 20
        game.dealer_hand.cards = ['Kd', '8d']
        game.dealer_hand.value = 18
        result = game.who_wins()
        self.assertEqual('Player Wins!', result)

    def test_player_dealer_same_cards(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['Kh', '7d']
        game.player.hand.value = 17
        game.dealer_hand.cards = ['Kd', '7h']
        game.dealer_hand.value = 17
        result = game.who_wins()
        self.assertEqual('TIE!', result)

    def test_should_continue_playing(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['Kh', '8d']
        game.player.hand.value = 18
        game.dealer_hand.cards = ['Kd', '4h']
        game.dealer_hand.value = 14
        result = game.who_wins()
        self.assertEqual('CONTINUE', result)

    def test_play_no_money(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.money = 0
        result = game.play('=')
        self.assertEqual('You dont have money.', result)

    def test_play_wrong_command(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.money = 5
        result = game.play('AAA')
        self.assertEqual('Wrong command, please use + or = .', result)

    def test_play_stand(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.money = 5
        game.player.hand.cards = ['Kh', 'Qd']
        game.player.hand.value = 20
        game.dealer_hand.cards = ['Kd', '8h']
        game.dealer_hand.value = 18
        self.assertEqual('Player Wins!', game.play('='))

    def test_play_one_more(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.money = 5
        game.player.hand.cards = ['Kh', '9d']
        game.player.hand.value = 19
        game.dealer_hand.cards = ['Kd', 'Th']
        game.dealer_hand.value = 20
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['3d']):
            self.assertEqual(game.play('+'), 'Dealer Wins!')

    def test_play_one_more_wins(self):
        game = Game()
        game.deck.cards = ['As', '6h', 'Jd', 'Qd', 'Kh']
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.money = 5
        result = game.play('+')
        self.assertEqual('Player Wins!', result)

    def test_player_dealer_21(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['Kh', '7d']
        game.player.hand.value = 17
        game.dealer_hand.cards = ['Kd', 'Ah']
        game.dealer_hand.value = 21
        result = game.who_wins()
        self.assertEqual('Dealer Wins!', result)

    def test_next_turn(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        self.assertEqual(
            game.next_turn(),
            'Do you want to stop (=) or have another card (+)?, q to quit')

    def test_next_turn_game_finished(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.is_playing = False
        self.assertEqual(game.next_turn(), 'Game Over')

    def test_next_turn_game_continue(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['Kh', '6d']
        game.player.hand.value = 16
        game.dealer_hand.cards = ['Kd', '5h']
        game.dealer_hand.value = 15
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['2d']):
            self.assertEqual(game.play('+'), 'CONTINUE')

    def test_force_quit(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        self.assertEqual(
            game.next_turn(),
            'Do you want to stop (=) or have another card (+)?, q to quit')
        self.assertEqual(game.play('q'), 'You left the game')
        self.assertFalse(game.is_playing)

    def test_game_with_as(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['4h', 'Ad']
        game.player.hand.value = 15
        game.dealer_hand.cards = ['4d', '5h']
        game.dealer_hand.value = 9
        game.player.hand.counter_as = 1
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['9d']):
            self.assertEqual(game.play('+'), 'CONTINUE')
            self.assertEqual(game.player.hand.value, 14)
            self.assertEqual(game.dealer_hand.value, 9)

    def test_game_with_as_2(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['4h', 'Ad', 'Ah']
        game.player.hand.value = 16
        game.dealer_hand.cards = ['4d', '5h']
        game.dealer_hand.value = 9
        game.player.hand.counter_as = 2
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['8d']):
            self.assertEqual(game.play('+'), 'CONTINUE')

    def test_game_with_as_mock(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['4h', 'Ad', '9d']
        game.player.hand.value = 14
        game.dealer_hand.cards = ['4d', '5h']
        game.dealer_hand.value = 9
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['8d']):
            game.play('+')
            self.assertEqual(game.player.hand.cards, ['4h', 'Ad', '9d', '8d'])
            self.assertEqual(game.player.hand.value, 22)

    def test_game_with_as_3(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['4h', 'Ah', 'Ad']
        game.player.hand.value = 16
        game.dealer_hand.cards = ['4d', '5h']
        game.dealer_hand.value = 9
        game.player.hand.counter_as = 2
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['Ac']):
            self.assertEqual(game.play('+'), 'CONTINUE')

    def test_game_with_as_4(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.player.hand.cards = ['As', 'Ah', 'Ad']
        game.player.hand.value = 13
        game.dealer_hand.cards = ['4d', '5h']
        game.dealer_hand.value = 9
        game.player.hand.counter_as = 3
        with unittest.mock.patch('Blackjack.deck.Deck.deal',
                                 return_value=['Ac']):
            self.assertEqual(game.play('+'), 'CONTINUE')

    def test_money_winner(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.bet = 20
        game.give_money_to_winner('Player Wins!')
        self.assertEqual(game.player.money, 120)

    def test_money_lose(self):
        game = Game()
        game.bet_time = False
        game.is_finished = False
        game.start_game()
        game.bet = 20
        game.give_money_to_winner('Dealer Wins!')
        self.assertEqual(game.player.money, 80)


if __name__ == "__main__":
    unittest.main()
