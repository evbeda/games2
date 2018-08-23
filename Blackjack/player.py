class Player():
    def __init__(self, money):
        self.money = money

    def balance(self, bet):
        self.money -= bet

    def win(self, pot):
        self.money += pot * 2
