class Game():
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
    
    def deal(self):
        for i in range(3):
            for player in self.players:
                player.hiddenCards.append(self.deck.get_card())
