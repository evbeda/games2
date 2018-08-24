from battleship.player import PlayerCPU, PlayerHuman

game_states = ['init', 'war', 'cpu_win','player_win']
possible_turn = ['human', 'cpu']


class Game():
    def __init__(self):
        self.player_cpu = PlayerCPU()
        self.player_human = PlayerHuman()
        self.state = game_states[0]
        self.turn = possible_turn[0]

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
            return 'pone el barco (x, y, boat, hor/ver)'
        elif self.state == game_states[1]:
            return 'shoot x, y'
        elif self.state == game_states[2]:
            return 'gano el cpu'
        else:
            return 'ganaste'

    def play(self, text_input):
        if self.state == game_states[0] and self.turn == possible_turn[0]:
            params = text_input.split(', ')
            if len(params) == 4:
                try:
                    return self.player_human.put_boat_own_board(
                        int(params[0]),
                        int(params[1]),
                        int(params[2]),
                        params[3],
                    )
                except Exception:
                    return "error"
            else:
                return "error"

    def change_turn(self):
        # Si el turno actual es de humano, cambiar a cpu
        if self.turn == possible_turn[0]:
            self.turn = possible_turn[1]
        else:
            # Sino, el turno actual es de cpu,cambiar a humano
            self.turn = possible_turn[0]
