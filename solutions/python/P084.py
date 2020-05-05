"""Project Euler Solutions
Problem 84: Monopoly odds
Solved by: Quinn Mortimer (modimore)
"""
import random

class MonopolySquare(object):
    def on_pass_through(self, game, player):
        # This is actually unused but when considering
        # Monopoly I thought it might be useful for the GO
        # square.
        pass
    
    def on_land(self, game, player):
        pass

class BasicMonopolySquare(MonopolySquare):
    pass

class ChanceMonopolySquare(MonopolySquare):
    def on_land(self, game, player):
        game.give_chance_card(player)

class CommunityChestMonopolySquare(MonopolySquare):
    def on_land(self, game, player):
        game.give_community_chest(player)

class GoToJailMonopolySquare(MonopolySquare):
    def on_land(self, game, player):
        game.send_to_jail(player)

class MonopolyGame(object):
    def __init__(self):
        self._board = [
            ("GO", None, BasicMonopolySquare()),
            ("A1", None, BasicMonopolySquare()),
            ("CC1", None, CommunityChestMonopolySquare()),
            ("A2", None, BasicMonopolySquare()),
            ("T1", None, BasicMonopolySquare()),
            ("R1", "R", BasicMonopolySquare()),
            ("B1", None, BasicMonopolySquare()),
            ("CH1", None, ChanceMonopolySquare()),
            ("B2", None, BasicMonopolySquare()),
            ("B3", None, BasicMonopolySquare()),
            ("JAIL", None, BasicMonopolySquare()),
            ("C1", None, BasicMonopolySquare()),
            ("U1", "U", BasicMonopolySquare()),
            ("C2", None, BasicMonopolySquare()),
            ("C3", None, BasicMonopolySquare()),
            ("R2", "R", BasicMonopolySquare()),
            ("D1", None, BasicMonopolySquare()),
            ("CC2", None, CommunityChestMonopolySquare()),
            ("D2", None, BasicMonopolySquare()),
            ("D3", None, BasicMonopolySquare()),
            ("FP", None, BasicMonopolySquare()),
            ("E1", None, BasicMonopolySquare()),
            ("CH2", None, ChanceMonopolySquare()),
            ("E2", None, BasicMonopolySquare()),
            ("E3", None, BasicMonopolySquare()),
            ("R3", "R", BasicMonopolySquare()),
            ("F1", None, BasicMonopolySquare()),
            ("F2", None, BasicMonopolySquare()),
            ("U2", "U", BasicMonopolySquare()),
            ("F3", None, BasicMonopolySquare()),
            ("GOTOJAIL", None, GoToJailMonopolySquare()),
            ("G1", None, BasicMonopolySquare()),
            ("G2", None, BasicMonopolySquare()),
            ("CC3", None, CommunityChestMonopolySquare()),
            ("G3", None, BasicMonopolySquare()),
            ("R4", "R", BasicMonopolySquare()),
            ("CH3", None, ChanceMonopolySquare()),
            ("H1", None, BasicMonopolySquare()),
            ("T2", None, BasicMonopolySquare()),
            ("H2", None, BasicMonopolySquare())
        ]
        self._player_states = []
        self._next_player = 0
        
        self._chance_effects = [None] * 6 + [
            lambda p: self.advance_player_to_square(p, "GO"),
            lambda p: self.send_to_jail(p),
            lambda p: self.advance_player_to_square(p, "C1"),
            lambda p: self.advance_player_to_square(p, "E3"),
            lambda p: self.advance_player_to_square(p, "H2"),
            lambda p: self.advance_player_to_square(p, "R1"),
            lambda p: self.advance_player_to_square_of_type(p, "R"),
            lambda p: self.advance_player_to_square_of_type(p, "R"),
            lambda p: self.advance_player_to_square_of_type(p, "U"),
            lambda p: self.move_player_back_n_squares(p, 3)
        ]
        random.shuffle(self._chance_effects)
        
        self._community_chest_effects = [None] * 14 + [
            lambda p: self.advance_player_to_square(p, "GO"),
            lambda p: self.send_to_jail(p),
        ]
        random.shuffle(self._community_chest_effects)
        
        self._num_turns = 0
        self._board_visits = [0 for s in self._board]
    
    def add_player(self):
        self._player_states.append(PlayerState())
    
    def advance_player_to_square(self, player, square_name):
        player_state = self._player_states[player]
        player_pos = player_state.position
        player_square = self._board[player_pos]
        while True:
            player_pos += 1
            if player_pos == len(self._board):
                player_pos = 0
            player_square = self._board[player_pos]
            if player_square[0] == square_name:
                player_state.position = player_pos
                player_square[2].on_land(self, player)
                break
            else:
                player_square[2].on_pass_through(self, player)
    
    def advance_player_to_square_of_type(self, player, square_type):
        player_state = self._player_states[player]
        player_pos = player_state.position
        player_square = self._board[player_pos]
        while True:
            player_pos += 1
            if player_pos == len(self._board):
                player_pos = 0
            player_square = self._board[player_pos]
            if player_square[1] == square_type:
                player_state.position = player_pos
                player_square[2].on_land(self, player)
                break
            else:
                player_square[2].on_pass_through(self, player)
        
    
    def give_chance_card(self, player):
        card = self._chance_effects.pop(0)
        if card is not None:
            card(player)
        self._chance_effects.append(card)
    
    def give_community_chest(self, player):
        card = self._community_chest_effects.pop(0)
        if card is not None:
            card(player)
        self._community_chest_effects.append(card)
    
    def move_player_n_squares(self, player, n):
        player_state = self._player_states[player]
        player_pos = player_state.position
        for i in range(1, n+1):
            player_pos += 1
            if player_pos == len(self._board):
                player_pos = 0
            square = self._board[player_pos]
            if i < n:
                square[2].on_pass_through(self, player)
            else:
                player_state.position = player_pos
                square[2].on_land(self, player)
        
    
    def move_player_back_n_squares(self, player, n):
        self._player_states[player].position -= n
    
    def play_next_turn(self):
        player = self._next_player
        player_state = self._player_states[player]
        
        r1, r2 = random.randint(1, 4), random.randint(1, 4)
        roll = r1 + r2
        is_double = r1 == r2
        
        # Problem says to assume the player will get out of jail ASAP
        player_state.in_jail = False
        self.move_player_n_squares(player, roll)
        self._count_turn()
        
        turn_doubles = 1 if is_double else 0
        
        while is_double and not player_state.in_jail:
            r1, r2 = random.randint(1, 4), random.randint(1, 4)
            roll = r1 + r2
            is_double = r1 == r2
            
            if is_double:
                turn_doubles += 1
            
            if turn_doubles == 3:
                self.send_to_jail(player)
            else:
                self.move_player_n_squares(player, roll)
            
            self._count_turn()
        
        self._next_player = (player + 1) % len(self._player_states)
    
    def send_to_jail(self, player):
        player_state = self._player_states[player]
        player_pos = player_state.position
        while self._board[player_pos][0] != "JAIL":
            player_pos += 1
            if player_pos == len(self._board):
                player_pos = 0
        player_state.position = player_pos
        player_state.in_jail = True
        player_state.jail_turns = 0
    
    def _count_turn(self):
        self._num_turns += 1
        self._board_visits[self._player_states[self._next_player].position] += 1
    
    def turn_stats(self):
        l = list(zip(range(len(self._board_visits)), self._board_visits))
        l.sort(key=lambda bv: bv[1], reverse=True)
        return l

class PlayerState(object):
    def __init__(self):
        self.position = 0
        self.doubles = 0
        self.in_jail = False
        self.jail_turns = 0

def solve(n_turns=600000, n_players=6):
    game = MonopolyGame()
    for _ in range(n_players):
        game.add_player()
    
    for i in range(n_turns):
        game.play_next_turn()
    
    return "".join("{:02d}".format(index) for index in map(lambda s: s[0], game.turn_stats()[0:3]))

if __name__ == "__main__":
    from sys import argv
    n_turns, n_players = 600000, 6
    if len(argv) > 1:
        try: n_turns = int(argv[1])
        except ValueError: pass
    if len(argv) > 2:
        try: n_players = int(argv[2])
        except ValueError: pass
    print(solve(n_turns, n_players))
