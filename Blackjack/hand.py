from .mazo import cardsDictionary
from .blackjack import sum_cards

class Hand():
    def __init__(self, mazo):
        self.mazo = mazo
        self.playersCards = {'1': [], '2': []}

    def deal_cards(self):

        self.playersCards['1'].append(self.mazo[0])
        self.playersCards['1'].append(self.mazo[1])
        self.playersCards['2'].append(self.mazo[2])
        self.playersCards['2'].append(self.mazo[3])

        # Sacar del mazo las 4 primeras cartas ya repartidas
        for i in range(3):
            self.mazo.pop(i - 1)

    def add_card_to_player(self, player, card):
        self.playersCards[player].append(card)

    def is_it_finished(self):
        if (sum_cards(self.playersCards['1']) > 21 or
                sum_cards(self.playersCards['2']) > 21):
            return True
        else:
            return False
