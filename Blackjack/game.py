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
        self.deck = Deck(cardsDictionary, colorDictionary)

    def start_game(self):
        name = 'Martin'
        buy_in = 100
        self.min_bet = 5
        self.player = Player(name, buy_in)
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

    def who_wins(self):
        #print(self.board())
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
        elif self.dealer_hand.value == 21:
            self.is_playing = False
            return 'Dealer Wins!'
        elif self.player.hand.value == 21:
            self.is_playing = False
            return 'Player Wins!'
        elif self.dealer_hand.value >= 17 and (self.player.hand.value > self.dealer_hand.value):
            self.is_playing = False
            return 'Player Wins!'
        elif self.dealer_hand.value >= 17 and (self.dealer_hand.value > self.player.hand.value):
            self.is_playing = False
            return 'Dealer Wins!'
        elif self.dealer_hand.value >= 17  and (self.dealer_hand.value == self.player.hand.value):
            self.is_playing = False
            return 'TIE!'
        elif self.dealer_hand.value < 17:
            self.is_playing = True
            return 'CONTINUE'

    def next_turn(self):
        if self.is_playing:
            return 'Do you want to stop (=) or have another card (+)?'
        else:
            return 'Game Over'

    def board(self):
        return 'Dealer: ' + str(self.dealer_hand.cards) + '\nPlayer: ' + str(self.player.hand.cards) + '\nPlayer Money: ' + str(self.player.money)

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
            else:
                return 'Wrong command, please use + or = .'
