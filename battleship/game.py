from battleship.player import PlayerCPU, PlayerHuman

game_states = ['init', 'war', 'cpu_win', 'player_win']
possible_turn = ['human', 'cpu']
messages_player_human = {
    'init': 'pone el barco (x, y, boat, horizontal/vertical)',
    'shoot': 'shoot (x, y)',
    'cpu_win': 'gano el cpu',
    'player_win': 'ganaste',
}


class GameBattleship():

    name = 'Battle Ship Game'

    def __init__(self):
        self.turn = possible_turn[0]
        self.player_cpu = PlayerCPU()
        self.player_human = PlayerHuman()
        self.state = game_states[0]
        self.is_playing = True

    def get_players(self):
        return [self.player_cpu, self.player_human]

    def set_boat(self, text_input):
        params = text_input.split(', ')
        if len(params) == 4:
            try:
                result = self.player_human.put_boat_own_board(
                    int(params[0]),
                    int(params[1]),
                    int(params[2]),
                    params[3],
                )
                # Si ya seteo todos los barcos de su tablero inicial
                if self.player_human.board_own.is_ready_to_war():
                    # Llenar el tablero de la cpu
                    self.player_cpu.fill_own_board()
                    if self.is_ready_to_war():
                        self.state = game_states[1]
                return result
            except Exception:
                return "error"
        else:
            return "error, mas parametros de los requeridos (4)"

    def war_human(self, text_input):
        params = text_input.split(', ')
        if len(params) == 2:
            result = self.player_cpu.board_own.shoot(
                int(params[0]),
                int(params[1])
            )
            if result == 'water':
                self.player_human.board_opponent.mark_shoot(
                    int(params[0]),
                    int(params[1]),
                    False
                )
                self.turn = possible_turn[1]
                self.player_human.messages.append(
                    'You only hit water! CPU turn')
                self.war_cpu()
                for message in self.player_cpu.messages:
                    self.player_human.messages.append(message)
                result = self.player_human.messages
            elif result == 'already shoot':
                self.player_human.messages.append('You already shoot in this place. Try again')

                result = self.player_human.messages
            elif result == 'sunked':
                self.player_human.board_opponent.mark_shoot(
                    int(params[0]),
                    int(params[1]),
                    True
                )
                self.player_human.messages.append(
                    'Congratulations! You sunk a boat.')
                result = self.player_human.messages
            elif result == 'hit':
                self.player_human.board_opponent.mark_shoot(
                    int(params[0]),
                    int(params[1]),
                    True
                )
                self.player_human.messages.append('You hit a boat')
                result = self.player_human.messages
            if not self.player_cpu.board_own.there_are_boats():
                self.state = game_states[3]
                self.player_human.messages.append('You Win')
                result = self.player_human.messages
            return result
        else:
            return "error, mas parametros de los requeridos (2)"

    def war_cpu(self):
        coordenate = self.player_cpu.pick_coordenate()
        result = self.player_human.board_own.shoot(*coordenate)
        if result == 'water':
            self.player_cpu.board_opponent.mark_shoot(
                *coordenate,
                False
            )
            self.turn = possible_turn[0]
            self.player_cpu.messages.append('Water! Now is your turn.')
            result = self.player_cpu.messages
        elif result == 'sunked':
            self.player_cpu.board_opponent.mark_shoot(
                *coordenate,
                True
            )
            self.player_cpu.messages.append('Your boat was sunk.')
            result = self.player_cpu.messages
        elif result == 'hit':
            self.player_cpu.board_opponent.mark_shoot(
                *coordenate,
                True
            )
            self.player_cpu.messages.append('Your boat was hit.')
            result = self.player_cpu.messages
        if not self.player_human.board_own.there_are_boats():
            self.state = game_states[2]
            self.player_cpu.messages.append('You lose.')
            result = self.player_cpu.messages
            return result
        else:
            return result

    def is_ready_to_war(self):
        if (
            self.player_cpu.board_own.is_ready_to_war() and
            self.player_human.board_own.is_ready_to_war()
        ):
            return True

    def next_turn(self):
        if self.is_playing:
            if self.state == game_states[0] and self.turn == possible_turn[0]:
                return messages_player_human['init']
            elif self.state == game_states[1] and self.turn == possible_turn[0]:
                return messages_player_human['shoot']

    def play(self, text_input):
        if self.state == game_states[0]:
            return self.set_boat(text_input)
        elif self.state == game_states[1] and self.turn == possible_turn[0]:
            return self.war_human(text_input)
        elif self.state == game_states[1] and self.turn == possible_turn[1]:
            return self.war_cpu()
