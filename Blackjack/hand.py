from .mazo import cardsDictionary
from .blackjack import sum_cards


class Hand():
    def __init__(self, mazo):
        self.mazo = mazo
        self.playersCards = []

    def deal_cards(self):

        self.playersCards.append(self.mazo[0])
        self.playersCards.append(self.mazo[1])

        # Sacar del mazo las 4 primeras cartas ya repartidas
        for i in range(2):
            self.mazo.pop(i - 1)

    def add_card_to_player(self, card):
        self.playersCards.append(card)

    def is_it_finished(self):
        if (sum_cards(self.playersCards) > 21):
            return True
        else:
            return False
