class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '{}{}'.format(
            self.value,
            self.suit,
        )
