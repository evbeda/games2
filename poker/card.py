class Card(object):
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return '{}{}'.format(
            self.value,
            self.color,
        )
