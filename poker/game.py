class Game(object):
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.shared_cards = []
        self.pot = 0
        self.round = 0

    def start(self):
        if self.deal_players():
            self.shared_cards = self.deck.deal(3)

    def deal_players(self):
        if self.player1.money > 0:
            self.player1.cards = self.deck.deal(2)
            if self.player2.money > 0:
                self.player2.cards = self.deck.deal(2)
                self.round += 1
                return True
            else:
                if round > 0:
                    print("Player 1 Wins!")
                print("Player 2 has no money")
                return False
        else:
            if round > 0:
                print("Player 2 Wins!")
            print("Player 1 has no money")
            return False

    def take_bets(self, player1_bet, player2_bet):
        if self.player1.money >= player1_bet:
            self.pot += player1_bet
        else:
            # print("Not enough money")
            return False
            # deberia ir el metodo que llame a take bets desde la consola
        if self.player2.money >= player2_bet:
            self.pot += player2_bet
        else:
            # print("Not enough money")
            return False
            # deberia ir el metodo que llame a take bets desde la consola
        return True

    