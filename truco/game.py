from truco.hand import envido_combinations, Hand
from truco.player import Player


class Game(object):
    name = 'Truco Game'
    input_args = 1

    def __init__(self):
        self.players = [Player('P1'), Player('P2')]
        self.cantos_envidos = []
        self.is_playing = True
        self.hand = Hand()

    # def cantos_envido(self, pos, canto):
    #     if canto == "Envido":
    #         if len(self.players[0].hidden_cards) == 3 and pos == 0:
    #             aux = [self.players[pos].get_name(), canto]
    #             self.cantos_envidos.append(aux)
    #             self.turno_envido = 1
    #             return aux
    #         elif len(self.players[1].hidden_cards) == 3 and len(
    #                 self.players[0].played_cards) == 1 and pos == 1:
    #             aux = [self.players[pos].get_name(), canto]
    #             self.cantos_envidos.append(aux)
    #             self.turno_envido = 0
    #             return aux

    # def cantos_real_envido(self, pos, canto):
    #     if canto == "Real Envido":
    #         if len(self.players[0].hidden_cards) == 3 and pos == 0:
    #             aux = [self.players[pos].get_name(), canto]
    #             self.cantos_envidos.append(aux)
    #             self.turno_envido = 1
    #             return aux
    #         elif len(self.players[1].hidden_cards) == 3 and len(self.players[0].played_cards) == 1 and pos == 1:
    #             aux = [self.players[pos].get_name(), canto]
    #             self.cantos_envidos.append(aux)
    #             self.turno_envido = 0
    #             return aux

    # def cantos_falta_envido(self, pos, canto):
    #     if canto == "Falta Envido":
    #         if len(self.players[0].hidden_cards) == 3 and pos == 0:
    #             aux = [self.players[pos].get_name(), canto]
    #             self.cantos_envidos.append(aux)
    #             self.turno_envido = 1
    #             return aux
    #         elif len(self.players[1].hidden_cards) == 3 and len(self.players[0].played_cards) == 1 and pos == 1:
    #             aux = [self.players[pos].get_name(), canto]
    #             self.cantos_envidos.append(aux)
    #             self.turno_envido = 0
    #             return aux

    # def aceptar_canto(self):
    #     if len(self.cantos_envidos) == 1:
    #         canto = self.cantos_envidos[0][1]
    #         for c in range(len(envido_combinations)):
    #             if envido_combinations[c][0] == canto and len(envido_combinations[c]) == 3:
    #                 self.comparar_puntos()

    # def get_cantos_envido(self):
    #     try:
    #         return self.cantos_envidos[-1]
    #     except IndexError:
    #         return None


    @property
    def board(self):
        if self.hand.is_playing is False:

            self.hand.deal_cards()
        return self.hand.show_cards()

    def next_turn(self):
        if self.is_playing == True:
            return '\nE: Para cantar envido \nT: Para cantar Truco \n0: Para jugar la primer carta \n1: Para jugar la segunda carta\n2: Para jugar la tercer carta\n'
        else:
            return '\nGame Over!\n'

    def play(self, command):
        self.hand.play_card(int(command))
        self.hand.play_card(int(command))  # PC
        self.hand.next_hand()
        self.hand.who_is_next()
        if self.hand.is_playing is False:
            return "\nLa mano termino\n{}{}".format(self.hand.show_cards(), "-----------")
        return "\nSiguiente ronda\n"
