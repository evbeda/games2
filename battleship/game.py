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
    def __init__(self):
        self.player_cpu = PlayerCPU()
        self.player_human = PlayerHuman()
        self.state = game_states[0]

    def get_players(self):
        return [self.player_cpu, self.player_human]

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

    def play(self, text_input):
        if self.state == game_states[0]:
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

        if self.state == game_states[1]:
            params = text_input.split(', ')
            if len(params) == 2:
                pass
                # TODO agregar logica de shoot del usuario
            else:
                return "error, mas parametros de los requeridos (2)"
