from .mazo import cardsDictionary
from .blackjack import sum_cards


class Hand():
    def __init__(self, mazo):
        self.mazo = mazo
        self.playersCards = []
        self.bank_cards = []

    def deal_cards(self):

        for index in range(2):
            self.playersCards.append(self.mazo.pop(0))
            self.bank_cards.append(self.mazo.pop(0))

    def add_card_to_player(self):
        self.playersCards.append(self.mazo.pop(0))

    def add_card_to_bank(self):
        self.bank_cards.append(self.mazo.pop(0))

    def is_it_finished(self):
        if (sum_cards(self.playersCards) > 21):
            return True
        else:
            return False
