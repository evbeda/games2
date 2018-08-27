from .mazo import cardsDictionary, colorDictionary
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

    def start_game(self):
        deck = Deck(cardsDictionary, colorDictionary)
        name = 'Martin'
        buy_in = 100

        self.player = Player(name, buy_in)
        player_hand = Hand()
        self.dealer_hand = Hand()
        player_hand.deal_card(deck.deal(2))
        self.dealer_hand.deal_card(deck.deal(2))
        self.player.hand = player_hand

    def check_you_can_bet(self):
        if self.player.money >= self.min_bet:
            return True
        else:
            self.is_playing = False
            return False

    def who_wins(self):
        if self.dealer_hand.value == 21 and len(self.dealer_hand.cards) == 2:
            if self.player.hand.value == 21 and len(self.player.hand.cards) == 2:
                self.is_playing = False
                return 'TIE!'
            self.is_playing = False
            return 'Dealer Wins!'
        elif self.player.hand.value == 21 and len(self.player.hand.cards) == 2:
            self.is_playing = False
            return 'Player Wins!'
        elif self.dealer_hand.value > 21:
            self.is_playing = False
            return 'Player Wins!'
        elif self.player.hand.value > 21:
            self.is_playing = False
            return 'Dealer Wins!'
        elif self.player.hand.value > self.dealer_hand.value:
            self.is_playing = False
            return 'Player Wins!'
        elif self.dealer_hand.value > self.player.hand.value:
            self.is_playing = False
            return 'Dealer Wins!'
        elif self.dealer_hand.value >= 17 and (self.dealer_hand.value == self.player.hand.value):
            self.is_playing = False
            return 'TIE!'
        else:
            self.is_playing = True

    def play(self, command):
        self.who_wins()
        self.check_you_can_bet()
