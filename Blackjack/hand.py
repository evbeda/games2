from . import cardsDictionary


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.counter_as = 0
        self.counter_as_discounted = 0

    def deal_card(self, cards):
        total_value = self.value
        for card in cards:
            self.cards.append(card)
            total_value += cardsDictionary[card[0]]
        self.value = total_value
        for card in self.cards:
            if 'A' in self.cards[self.cards.index(card)]:
                if self.value > 21 and self.counter_as == self.counter_as_discounted:
                        self.value -= 10

        if 'A' in cards[-1]:
            self.sum_cards()

    def sum_cards(self):
        for as_card in ['Ah', 'Ad', 'Ac', 'As']:
            if as_card in self.cards:
                self.counter_as += 1
                if self.value > 21:
                    # Decrease value by 10 because A is going to be 1
                    self.counter_as_discounted += 1
                    self.value -= 10
        return self.value
