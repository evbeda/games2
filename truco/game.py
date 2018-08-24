class Game():
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.cantos_envidos = []
        self.turno_envido = None

    def deal(self):
        self.change_hand()
        self.players[0].reset_hand()
        self.players[1].reset_hand()
        for i in range(3):
            for player in self.players:
                if len(player.hiddenCards) < 3:
                    player.hiddenCards.append(self.deck.get_card())

    def change_hand(self):
        if ((len(self.players[0].playedCards) == 0) and (len(self.players[0].hiddenCards) == 0)) and ((len(self.players[1].playedCards) == 0) and (len(self.players[1].hiddenCards) == 0)):
            self.players[0].is_hand = True
            self.players[1].is_hand = False
        else:
            self.players[0].is_hand = self.players[1].is_hand
            self.players[1].is_hand = not self.players[0].is_hand

    def who_is_next(self):
        card_p1 = self.players[0].playedCards[-1]
        card_p2 = self.players[1].playedCards[-1]
        result = card_p1.compare_with(card_p2)
        if result == 'GREATER':
            return 'PLAYER1'
        elif result == 'LOWER':
            return 'PLAYER2'
        else:
            player_1_hand_state = self.players[0].is_hand
            if player_1_hand_state:
                return 'PLAYER1'
            else:
                return 'PLAYER2'

    def cantos_envido(self, pos, canto):
        if canto == "Envido":
            if len(self.players[0].hiddenCards) == 3 and pos == 0:
                aux = [self.players[pos].get_name(), canto]
                self.cantos_envidos.append(aux)
                self.turno_envido = 1
                return aux
            elif len(self.players[1].hiddenCards) == 3 and len(self.players[0].playedCards) == 1 and pos == 1:
                aux = [self.players[pos].get_name(), canto]
                self.cantos_envidos.append(aux)
                self.turno_envido = 0
                return aux

    def get_cantos_envido(self):
        try:
            return self.cantos_envidos[-1]
        except IndexError:
            return None
