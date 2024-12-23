import math

# The computer is the max player
MAX_PLAYER = "O"
MIN_PLAYER = "X"


def is_terminal(grid):
    is_grid_full = True
    for cell in grid:
        if cell != MAX_PLAYER and cell != MIN_PLAYER:
            is_grid_full = False
            break
    if is_grid_full:
        return 0

    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                         [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                         [0, 4, 8], [2, 4, 6]]
    for winning_position in winning_positions:
        is_winning_postion_valid = True
        for i in winning_position:
            if grid[i] != MAX_PLAYER and grid[i] != MIN_PLAYER:
                is_winning_postion_valid = False
                break
        if is_winning_postion_valid:
            if grid[winning_position[0]] == grid[winning_position[1]] == grid[winning_position[2]]:
                winner = grid[winning_position[0]]
                
                if winner == MAX_PLAYER:
                    return 1
                return -1

def minimax(grid, is_maximising):
    score = is_terminal(grid)
    if score:
        return score

    if is_maximising:
        best_score = -math.inf
        for i in range(len(grid)):
            if grid[i] != MIN_PLAYER and grid[i] != MAX_PLAYER:
                grid[i] = MAX_PLAYER
                score = minimax(grid, False)
                grid[i] = str(i + 1)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(len(grid)):
            if grid[i] != MIN_PLAYER and grid[i] != MAX_PLAYER:
                grid[i] = MIN_PLAYER
                score = minimax(grid, True)
                grid[i] = str(i + 1)
                best_score = min(score, best_score)
        return best_score 

def best_move(grid):
    best_score = -math.inf
    move = None

    for i in range(len(grid)):
        if grid[i] != MIN_PLAYER and grid[i] != MAX_PLAYER:
            grid[i] = MAX_PLAYER
            score = minimax(grid, False)
            grid[i] = str(i + 1)

            if score > best_score:
                best_score = score
                move = i
    return move