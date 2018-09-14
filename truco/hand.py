from .deck import Deck

envido_combinations = [
    [['ENVIDO'], 2, 1],
    [['REAL_ENVIDO'], 3, 1],
    [['FALTA_ENVIDO'], 0, 1],
    [['ENVIDO', 'ENVIDO'], 4, 2],
    [['REAL_ENVIDO', 'FALTA_ENVIDO'], 5, 2],
    [['ENVIDO', 'REAL_ENVIDO'], 5, 2],
    [['ENVIDO', 'FALTA_ENVIDO'], 0, 2],
    [['ENVIDO', 'ENVIDO', 'REAL_ENVIDO'], 7, 4],
    [['ENVIDO', 'ENVIDO', 'FALTA_ENVIDO'], 0, 4],
    [['ENVIDO', 'REAL_ENVIDO', 'FALTA_ENVIDO'], 0, 5],
    [['ENVIDO', 'ENVIDO', 'REAL_ENVIDO', 'FALTA_ENVIDO'], 0, 7],
]

truco_combinations = [
    [['TRUCO'], 2, 1],
    [['TRUCO', 'RE_TRUCO'], 3, 2],
    [['TRUCO', 'RE_TRUCO', 'VALE_CUATRO'], 4, 3],
]

envido_posibilities = ["ENVIDO", "REAL_ENVIDO", "FALTA_ENVIDO"]
truco_posibilities = ["TRUCO", "RE_TRUCO", "VALE_CUATRO"]


class Hand(object):

    def __init__(self, mano=0):
        self.turn = 0
        self.number_hand = 1
        self.played_cards = None
        self.hidden_cards = None
        self.envido_fase = True
        self.truco_fase = True
        self.winner_index = None
        self.mano = mano
        self.deal_cards()
        self.envidos = []
        self.trucos = []
        self.truco_turn = 0
        self.truco_pending = False
        self.mazo = False

    @property
    def envido_solved(self):
        if len(self.envidos) > 0 and self.envido_fase:
            return False
        return True

    def limpiar_mesa(self):
        self.hidden_cards = [[], [], ]
        self.played_cards = [[], [], ]
        self.winner_index = None

    def deal_cards(self):
        self.limpiar_mesa()
        deck = Deck()
        for player in range(2):
            for card_index in range(3):
                self.hidden_cards[player].append(deck.get_card())

    def play_card(self, card_index):
        played_card = self.hidden_cards[self.turn][card_index]
        del self.hidden_cards[self.turn][card_index]
        self.played_cards[self.turn].append(played_card)
        self.cambiar_turno()

    def cambiar_turno(self):
        self.turn = 0 if (self.turn == 1) else 1

    def siguiente_ronda(self):
        if len(self.played_cards[0]) == len(self.played_cards[1]):
            self.envido_fase = False
            self.number_hand += 1

    def who_is_next(self):
        if self.played_cards[0][-1].compare_with(self.played_cards[1][-1]) == 'GREATER':
            self.turn = 0
        elif self.played_cards[0][-1].compare_with(self.played_cards[1][-1]) == 'EQUAL':
            pass
        else:
            self.turn = 1

    def get_envido_points(self, won=0):
        for combination in envido_combinations:
            if combination[0] == self.envidos:
                if self.envidos[-1] == 'FALTA_ENVIDO' and won == 0:
                    return 99
                else:
                    return combination[won + 1]

    def get_truco_points(self, won=0):
        if len(self.trucos) == 0:
            return 1
        for combination in truco_combinations:
            if combination[0] == self.trucos:
                return combination[won + 1]

    def accept_envido(self):
        self.envido_fase = False

    def reject_envido(self):
        self.envido_fase = False
        self.envidos = []

    def sing_envido(self, command):
        if not self.envido_fase:
            raise Exception()
        self.envidos.append(command)

    def sing_truco(self, command):
        if self.truco_pending:
            raise Exception('You can not sing truco now')
        self.envido_fase = False
        self.trucos.append(command)
        self.truco_turn = 0 if self.truco_turn == 1 else 1
        self.truco_pending = True

    def accept_truco(self):
        self.truco_pending = False
        self.envido_fase = False

    def reject_truco(self):
        self.truco_pending = False
        self.mazo = True

    @property
    def is_playing(self):
        if self.mazo:
            return False
        if len(self.played_cards[0]) == len(self.played_cards[1]):
            win_hands_1 = 0
            win_hands_0 = 0
            for i in range(len(self.played_cards[0])):
                carta_pc = self.played_cards[1][i]
                carta_humano = self.played_cards[0][i]
                if carta_humano.compare_with(carta_pc) == 'GREATER':
                    win_hands_0 += 1
                if carta_pc.compare_with(carta_humano) == 'GREATER':
                    win_hands_1 += 1
            if win_hands_0 == win_hands_1 and self.number_hand is 4:
                self.winner_index = self.mano
                return False
            if win_hands_0 >= 2 or win_hands_1 >= 2:
                self.winner_index = 0 if win_hands_0 > win_hands_1 else 1
                return False
            return True
        else:
            return True

    def get_envido_winner(self):
        score_p0 = self.get_score_envido(0)
        score_p1 = self.get_score_envido(1)
        if score_p0 > score_p1:
            return 0
        elif score_p0 < score_p1:
            return 1
        else:
            return self.mano

    def get_score_envido(self, player):
        same_suit_cards = set()
        all_cards = self.hidden_cards[player] + self.played_cards[player]
        white = []
        for i in range(len(all_cards) - 1):
            for j in range(len(all_cards)):
                if i != j and all_cards[i].suit == all_cards[j].suit:
                    same_suit_cards.add(all_cards[i].number)
                    same_suit_cards.add(all_cards[j].number)
        if len(same_suit_cards) != 0:
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
        for i in all_cards:
            if i.number > 8:
                all_cards.remove(i)
        return 0 if (len(all_cards) == 0) else max(all_cards).number

    def show_cards(self):
        result = ['\nPlayed Cards: \n']
        contador = 0
        for group in self.played_cards:
            if contador == 0:
                result.append("Human: ")
                contador += 1
            else:
                result.append("Computer: ")
            for card2 in group:
                result.append(str(card2) + ' ')
            result.append('\n')
        return ''.join(result)

    def get_response_envido(self, ):
        envido_possibles = ['ACCEPTED', 'REJECTED', ]
        if 'FALTA_ENVIDO' in self.envidos:
            return envido_possibles
        envido_possibles.append('FALTA_ENVIDO')
        if 'REAL_ENVIDO' in self.envidos:
            return envido_possibles
        envido_possibles.append('REAL_ENVIDO')
        envidos = len([e for e in self.envidos if e == 'ENVIDO'])
        if envidos < 2:
            envido_possibles.append('ENVIDO')
        return envido_possibles

    def get_response_truco(self, ):
        truco_possibles = ['ACCEPTED', 'REJECTED', ]
        if 'VALE_CUATRO' in self.trucos:
            return truco_possibles
        truco_possibles.append('VALE_CUATRO')
        if 'RE_TRUCO' in self.trucos:
            return truco_possibles
        truco_possibles.append('RE_TRUCO')
        return truco_possibles
