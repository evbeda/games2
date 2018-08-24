from .mazo import cardsDictionary


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

    def sum_cards(self):
        sum = self.value
        if [['Ah', 'Ad', 'Ac', 'Ad'] in self.cards]:
            if self.value > 21:
                # Decrease value by 10 because A is going to be 1
                sum -= 10
        return sum
