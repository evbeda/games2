from . import cardsDictionary


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.counter_as = 0
        self.counter_as_discounted = 0

    def deal_card(self, cards):
        # sumar valor
        total_value = self.value
        cards_without_as = []
        for card in self.cards:
            if not ('A' in card):
                cards_without_as.append(card)
        for card in cards:
            self.cards.append(card)
            if not ('A' in card):
                cards_without_as.append(card)
            else:
                self.counter_as += 1
            total_value += cardsDictionary[card[0]]
        self.value = total_value

        # sumar valor sin ases
        value_without_as = 0
        for card in cards_without_as:
            value_without_as += cardsDictionary[card[0]]
        if self.counter_as == 1:
            if value_without_as + 11 == self.value:
                if self.value > 21:
                    self.value -= 10

        elif self.counter_as == 2:
            if value_without_as + 22 == self.value:
                if self.value > 21:
                    self.value -= 10
            if value_without_as + 12 == self.value:
                if self.value > 21:
                    self.value -= 10

        elif self.counter_as == 3:
            if value_without_as + 23 == self.value:
                if self.value > 21:
                    self.value -= 10
            if value_without_as + 13 == self.value:
                if self.value > 21:
                    self.value -= 10

        elif self.counter_as == 4:
            if value_without_as + 24 == self.value:
                if self.value > 21:
                    self.value -= 10
            if value_without_as + 14 == self.value:
                if self.value > 21:
                    self.value -= 10
