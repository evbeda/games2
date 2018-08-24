class Player():
    def __init__(self, money):
        self.money = money
        self.hand = None

    def balance(self, bet):
        self.money -= bet

    def win(self, pot):
        self.money += pot * 2
