from .jugadas import combinaciones_envido
from .carta import Carta


class Game():

    name = 'Truco Game'

    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.cantos_envidos = []
        self.turno_juego = None
        self.turno_envido = None
        self.turno_truco = None
        self.turno_retruco = None
        self.turno_vale_cuatro = None
        self.is_playing = True

    def deal(self):
        self.reset_state()
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
            self.turno_juego = 0
        else:
            self.players[0].is_hand = self.players[1].is_hand
            self.players[1].is_hand = not self.players[0].is_hand
            self.turno_juego = 1

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

    # def play(self):
    #     self.deal()
    #     if turno_juego == 0:
    #         print('What do you want to do?')
    #         #falta determinar todas las posiblilidades que tiene (Jugar una carta o cantar)
    #         self.players[self.turno_juego].play_card(position)

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

    def cantos_real_envido(self, pos, canto):
        if canto == "Real Envido":
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

    def cantos_falta_envido(self, pos, canto):
        if canto == "Falta Envido":
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

    def aceptar_canto(self):
        if len(self.cantos_envidos) == 1:
            canto = self.cantos_envidos[0][1]
            print(canto)
        for c in range(len(combinaciones_envido)):
            if combinaciones_envido[c][0] == canto and len(combinaciones_envido[c]) == 3:
                print(combinaciones_envido[c][0])
                self.comparar_puntos()

    def comparar_puntos(self):
        cards_player_01 = []
        cards_player_02 = self.players[1].hiddenCards
        puntaje_player_01 = 0
        puntaje_player_02 = 0
        if len(self.players[0].playedCards) != 0:
            cards_player_01.append(self.players[0].playedCards[0])
            cards_player_01.append(self.players[0].hiddenCards[0])
            cards_player_01.append(self.players[0].hiddenCards[1])
        else:
            cards_player_01 = self.players[0].hiddenCards
        cartas = []
        c = 0
        if cards_player_01[c].suit == cards_player_01[c + 1].suit and cards_player_01[c + 1].suit == cards_player_01[c + 2].suit:
            for card in cards_player_01:
                cartas.append(card.number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    if cartas[c + 2] >= 10:
                        puntaje_player_01 = 20
                    else:
                        puntaje_player_01 = 20 + cartas[c + 2]
                else:
                    puntaje_player_01 = cartas[c + 1] + cartas[c + 2] + 20
            else:
                puntaje_player_01 = cartas[c] + cartas[c + 1] + 20
        elif cards_player_01[c].suit == cards_player_01[c + 1].suit:
            cartas.append(cards_player_01[c].number)
            cartas.append(cards_player_01[c + 1].number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    puntaje_player_01 = 20
                else:
                    puntaje_player_01 = cartas[c + 1] + 20
            else:
                puntaje_player_01 = cartas[c] + cartas[c + 1] + 20
        elif cards_player_01[c].suit == cards_player_01[c + 2].suit:
            cartas.append(cards_player_01[c].number)
            cartas.append(cards_player_01[c + 2].number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    puntaje_player_01 = 20
                else:
                    puntaje_player_01 = cartas[c + 1] + 20
            else:
                puntaje_player_01 = cartas[c] + cartas[c + 1] + 20

        elif cards_player_01[c + 1].suit == cards_player_01[c + 2].suit:
            cartas.append(cards_player_01[c + 1].number)
            cartas.append(cards_player_01[c + 2].number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    puntaje_player_01 = 20
                else:
                    puntaje_player_01 = cartas[c + 1] + 20
            else:
                puntaje_player_01 = cartas[c] + cartas[c + 1] + 20

        cartas = []
        if cards_player_02[c].suit == cards_player_02[c + 1].suit and cards_player_02[c + 1].suit == cards_player_02[c + 2].suit:
            for card in cards_player_02:
                cartas.append(card.number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    if cartas[c + 2] >= 10:
                        puntaje_player_02 = 20
                    else:
                        puntaje_player_02 = 20 + cartas[c + 2]
                else:
                    puntaje_player_02 = cartas[c + 1] + cartas[c + 2] + 20
            else:
                puntaje_player_02 = cartas[c] + cartas[c + 1] + 20
        elif cards_player_02[c].suit == cards_player_02[c + 1].suit:
            cartas.append(cards_player_02[c].number)
            cartas.append(cards_player_02[c + 1].number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    puntaje_player_02 = 20
                else:
                    puntaje_player_02 = cartas[c + 1] + 20
            else:
                puntaje_player_02 = cartas[c] + cartas[c + 1] + 20

        elif cards_player_02[c].suit == cards_player_02[c + 2].suit:
            cartas.append(cards_player_02[c].number)
            cartas.append(cards_player_02[c + 2].number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    puntaje_player_02 = 20
                else:
                    puntaje_player_02 = cartas[c + 1] + 20
            else:
                puntaje_player_02 = cartas[c] + cartas[c + 1] + 20

        elif cards_player_02[c + 1].suit == cards_player_02[c + 2].suit:
            cartas.append(cards_player_02[c + 1].number)
            cartas.append(cards_player_02[c + 2].number)
            cartas.sort(reverse=True)
            if cartas[c] >= 10:
                if cartas[c + 1] >= 10:
                    puntaje_player_02 = 20
                else:
                    puntaje_player_02 = cartas[c + 1] + 20
            else:
                puntaje_player_02 = cartas[c] + cartas[c + 1] + 20
        return [puntaje_player_01, puntaje_player_02]

        # print(cartas)
        # elif 2 son iguales
        # elif 3 distintas
        # c = 0

    def get_cantos_envido(self):
        try:
            return self.cantos_envidos[-1]
        except IndexError:
            return None

    def get_state(self):
        status = [self.turno_juego,
                  self.turno_envido,
                  self.turno_truco,
                  self.turno_retruco,
                  self.turno_vale_cuatro
                  ]
        return status

    def next_turn(self):
        pass

    def play(self, string):
        pass

    def board(self):
        return self.players[self.turno_juego].show_hand_to_board()




    def reset_state(self):
        self.turno_juego = None
        self.turno_envido = None
        self.turno_truco = None
        self.turno_retruco = None
        self.turno_vale_cuatro = None
