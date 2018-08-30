

class Player():
    def __init__(self, name):
        self.name = name
        self.hidden_cards = []
        self.score = []
        self.played_cards = []
        self.is_hand = bool

    def play_card(self, index):
        played_card = self.hidden_cards.pop(index)
        self.played_cards.append(played_card)

    def reset_hand(self):
        del self.hidden_cards[:]
        del self.played_cards[:]

    def get_name(self):
        return self.name

    def show_hand_to_board(self):
        hidden = ''
        played = ''
        for i in self.hidden_cards:
            hidden += i.__str__()
            hidden += ', '
        for i in self.played_cards:
            played += i.__str__()
            played += ', '
        return "Cartas en mano: {} \n {}{}".format(
            hidden,
            "Cartas jugadas: ",
            played
        )

    def get_score_envido(self):
        same_suit_cards = set()
        white = []
        for i in range(len(self.hidden_cards) - 1):
            for j in range(len(self.hidden_cards)):
                if i == j:
                    pass
                else:
                    if self.hidden_cards[i].suit == self.hidden_cards[j].suit:
                        same_suit_cards.add(self.hidden_cards[i].number)
                        same_suit_cards.add(self.hidden_cards[j].number)
        if len(same_suit_cards) == 0:
            return max(self.hidden_cards).number
        else:
            for card in same_suit_cards:
                if card < 8:
                    white.append(card)
            if len(white) == 0:
                return 20
            elif len(white) == 1:
                return white[0] + 20
            elif len(white) == 2:
                return white[0] + white[1] + 20
            elif len(white) == 3:
                card = max(white)
                white.remove(card)
                card_two = max(white)
                return card + card_two + 20

        return same_suit_cards
