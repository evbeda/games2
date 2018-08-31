from .deck import Deck


class Hand():
    def __init__(self):
        self.deal_cards()
        self.turn = 0
        self.points = 0

    def deal_cards(self):
        self.hidden_cards = [[],[]]
        self.played_cards = [[],[]]
        deck = Deck()
        for player in range(2):
            for card_index in range(3):
                self.hidden_cards[player].append(deck.get_card)

    def play_card(self, card_index):
        played_card = self.hidden_cards[self.turn].pop(card_index)
        self.played_cards[self.turn].append(played_card)
        self.turn = (self.turn + 1) % 2

    def next_hand(self):
        self.number_hand += 1

    def get_score_envido(self, player):
        same_suit_cards = set()
        all_cards = self.hidden_cards[player] + self.played_cards[player]
        white = []
        for i in range(len(all_cards) - 1):
            for j in range(len(all_cards)):
                if i == j:
                    pass
                else:
                    if all_cards[i].suit == all_cards[j].suit:
                        same_suit_cards.add(all_cards[i].number)
                        same_suit_cards.add(all_cards[j].number)
        if len(same_suit_cards) == 0:
            for i in all_cards:
                if i.number > 8:
                    all_cards.remove(i)
            return 0 if (len(all_cards) == 0) else max(all_cards).number
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

    @property
    def envido(self):
        return True
