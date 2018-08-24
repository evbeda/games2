from .mazo import cardsDictionary, colorDictionary
from .player import Player
from .deck import Deck
from .hand import Hand

class Game():
    def __init__(self):
        self.min_bet = 0
        self.player = None
        self.dealer_hand = None # have to be a Hand
        self.pot = 0

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
            return False
