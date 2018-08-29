from . import cardsDictionary


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0

    def deal_card(self, cards):
        total_value = self.value
        for card in cards:
            self.cards.append(card)
            total_value += cardsDictionary[card[0]]
        self.value = total_value
        self.sum_cards()

    def sum_cards(self):
        for as_card in ['Ah', 'Ad', 'Ac', 'As']:
            if as_card in self.cards:
                if self.value > 21:
                    # Decrease value by 10 because A is going to be 1
                    self.value -= 10
        return self.value
