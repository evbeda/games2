from . import cardsDictionary, colorDictionary, cards_colors
from .player import Player
from .deck import Deck
from .hand import Hand


class Game():
    name = 'Blackjack'
    input_args = 1

    def __init__(self):
        self.min_bet = 0
        self.player = None
        self.dealer_hand = None  # have to be a Hand
        self.pot = 0
        self.is_playing = True
        self.is_finished = False
        self.deck = Deck(cardsDictionary, colorDictionary)
        self.start_game()

    def start_game(self):
        name = 'Martin'
        buy_in = 100
        self.min_bet = 5
        self.player = Player(name, buy_in)
        self.reset_round()

    def reset_round(self):
        player_hand = Hand()
        self.dealer_hand = Hand()
        player_hand.deal_card(self.deck.deal(2))
        self.dealer_hand.deal_card(self.deck.deal(2))
        self.player.hand = player_hand

    def check_you_can_bet(self):
        if self.player.money >= self.min_bet:
            return True
        else:
            self.is_playing = False
            return False

    def compare_bet(self, min_bet, bet):
        if(bet >= min_bet):
            return True
        else:
            return False

    def who_wins(self):
        if self.dealer_hand.value == 21 and len(self.dealer_hand.cards) == 2:
            if (self.player.hand.value == 21 and
                    len(self.player.hand.cards) == 2):
                self.is_finished = True
                return 'TIE!'
            self.is_finished = True
            return 'Dealer Wins!'
        elif self.player.hand.value == 21 and len(self.player.hand.cards) == 2:
            self.is_finished = True
            return 'Player Wins!'
        elif self.dealer_hand.value > 21:
            self.is_finished = True
            return 'Player Wins!'
        elif self.player.hand.value > 21:
            self.is_finished = True
            return 'Dealer Wins!'
        elif self.dealer_hand.value == 21:
            self.is_finished = True
            return 'Dealer Wins!'
        elif self.player.hand.value == 21:
            self.is_finished = True
            return 'Player Wins!'
        elif (
            self.dealer_hand.value >= 17 and
            self.player.hand.value > self.dealer_hand.value
        ):
            self.is_finished = True
            return 'Player Wins!'
        elif (
            self.dealer_hand.value >= 17 and
            self.dealer_hand.value > self.player.hand.value
        ):
            self.is_finished = True
            return 'Dealer Wins!'
        elif (
                self.dealer_hand.value >= 17 and
                self.dealer_hand.value < 21 and
                self.player.hand.value > self.dealer_hand.value
        ):
            self.is_finished = True
            return 'Player Wins!'
        elif (
                self.dealer_hand.value >= 17 and
                self.dealer_hand.value == self.player.hand.value
        ):
            self.is_finished = True
            return 'TIE!'
        elif self.dealer_hand.value < 17:
            self.is_playing = True
            return 'CONTINUE'

    def next_turn(self):
        if self.is_playing:
            if self.is_finished:
                return 'Do you want to start a new game? y(yes) / q(quit)'
            else:
                return ('Do you want to stop (=) '
                        'or have another card (+)?, q to quit')
        else:
            return 'Game Over'

    @property
    def board(self):
        dealer_cards = []
        player_cards = []
        for card in self.dealer_hand.cards:
            if(card[0] == 'T'):
                dealer_cards.append('10' + cards_colors[card[1]])
            else:
                dealer_cards.append(card[0] + cards_colors[card[1]])

        for card in self.player.hand.cards:
            if(card[0] == 'T'):
                player_cards.append('10' + cards_colors[card[1]])
            else:
                player_cards.append(card[0] + cards_colors[card[1]])

        return ('\n\nDealer: {dealer_cards}'
                '\nPlayer: {player_cards}\n'
                'Money: {player_money} \n\n').format(
            dealer_cards=dealer_cards,
            player_cards=player_cards,
            player_money=self.player.money,
        )

    def play(self, command):
        if not self.check_you_can_bet():
            self.is_playing = False
            return 'You dont have money.'
        else:
            if command == '=':
                if self.who_wins() == 'CONTINUE':
                    self.dealer_hand.deal_card(self.deck.deal(1))
                    return self.play('=')
                else:
                    return self.who_wins()
            elif command == '+':
                self.player.hand.deal_card(self.deck.deal(1))
                if self.who_wins() == 'CONTINUE':
                    return self.who_wins()
                else:
                    return self.who_wins()
            elif command == 'y':
                self.reset_round()
                self.is_finished = False
                return 'New Round'
            elif command == 'q':
                self.is_playing = False
                return 'You left the game'
            else:
                return 'Wrong command, please use + or = .'
