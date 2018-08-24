class Player(object):
    def __init__(self, money):
        if money > 0:
            self.cards = []
            self.money = money
        else:
            raise Exception('Player money must be greater than 0')
