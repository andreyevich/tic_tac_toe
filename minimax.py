"""
X - min player
O - max player (computer)

Implementation:

s0 - initial state
player(s) - returns which player to move in state s
actions(s) - returns legal moves in state s
result(s, a) - returns the state after action a taken in state s
terminal(s) - checks if the state s is a terminal state
"""
import sys

MIN_PLAYER = "O"
MAX_PLAYER = "X"

def player(state):
    max_player_count = 0
    min_player_count = 0
    for cell in state:
        if cell == MAX_PLAYER:
            max_player_count += 1
        elif cell == MIN_PLAYER:
            min_player_count += 1

    if max_player_count <= min_player_count:
        return MAX_PLAYER
    else:
        return MIN_PLAYER

def actions(state):
    result = []
    for cell in state:
        if cell != MAX_PLAYER and cell != MIN_PLAYER:
            result.append(state.index(cell))
    return result

def result(state=list, action=int, player=str):
    state[action] = player
    return state

def terminal(state):
    full = True
    for cell in state:
        if cell != MAX_PLAYER and cell != MIN_PLAYER:
            full = False
            break
    if full:
        return True, 0
    # TODO: unhardcode??
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                         [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                         [0, 4, 8], [2, 4, 6]]
    for winning_position in winning_positions:
        valid = True
        for cell_index in winning_position:
            if state[cell_index] != MAX_PLAYER or state[cell_index] != MIN_PLAYER:
                valid = False
                break
        if valid:
            if state[winning_position[0]] == state[winning_position[1]] == state[winning_position[2]]:
                winning_player = state[winning_position[0]]
                
                if winning_player == MAX_PLAYER:
                    return True, 1
                return True, -1

    return False, 0


def max_value(state):
    is_terminal, utility = terminal(state)
    if is_terminal:
        return utility
    state_value = -sys.maxsize # the interpreter's word size (i.e. the max length of strings, lists, etc.)
    for action in actions(state):
        state_value = max(state_value, min_value(result(state, action, MAX_PLAYER)))
    return state_value

def min_value(state):
    is_terminal, utility = terminal(state)
    if is_terminal:
        return utility
    state_value = sys.maxsize # the interpreter's word size (i.e. the max length of strings, lists, etc.)
    for action in actions(state):
        state_value = min(state_value, max_value(result(state, action, MIN_PLAYER)))
    return state_value

