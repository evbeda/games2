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

    def is_ready_to_war(self):
        if (
            self.player_cpu.board_own.is_ready_to_war() and
            self.player_human.board_own.is_ready_to_war()
        ):
            return True
        else:
            return False

    def check_state_message(self):
        if self.state == game_states[0]:
            return messages_player_human['init']
        elif self.state == game_states[1]:
            return messages_player_human['shoot']
        elif self.state == game_states[2]:
            return messages_player_human['cpu_win']
        else:
            return messages_player_human['player_win']

    def next_turn(self):
        return 'Hacer metodo'

    @property
    def board(self):
        return 'board'

    def play(self, text_input):
        if self.state == game_states[0]:
            return self.set_boat(text_input)
        elif self.state == game_states[1]:
            params = text_input.split(', ')
            # TODO Should check number of params only for human turn
            if self.turn == possible_turn[0]:
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
                        result = 'You only hit water! CPU turn'
                    elif result == 'Already shoot':
                        result = 'You already shoot in this place. Try again'
                    elif result == 'sunked':
                        self.player_human.board_opponent.mark_shoot(
                            int(params[0]),
                            int(params[1]),
                            True
                        )
                        result = 'Congratulations! You sunk a boat.'
                    elif result == 'hit':
                        self.player_human.board_opponent.mark_shoot(
                            int(params[0]),
                            int(params[1]),
                            True
                        )
                        result = 'You hit a boat'
                    if not self.player_cpu.board_own.there_are_boats():
                        self.state = game_states[3]
                    return result
                else:
                    return "error, mas parametros de los requeridos (2)"
            elif self.turn == possible_turn[1]:
                coordenate = self.player_cpu.pick_coordenate()
                result = self.player_human.board_own.shoot(*coordenate)
                if result == 'water':
                        self.player_cpu.board_opponent.mark_shoot(*coordenate, False)
                        self.turn = possible_turn[0]
                        result = 'Water! Now is your turn.'
                elif result == 'sunked':
                    self.player_cpu.board_opponent.mark_shoot(*coordenate, True)
                    result = 'Your boat was sunk.'
                elif result == 'hit':
                    self.player_cpu.board_opponent.mark_shoot(*coordenate, True)
                    result = 'Your boat was hit.'
                if not self.player_cpu.board_own.there_are_boats():
                    self.state = game_states[2]
                    return 'You lose.'
                else:
                    return result
        elif self.state == game_states[2]:
            return 'La CPU gano!'
        elif self.state == game_states[3]:
            return 'Felicitaciones! Ganaste!'
