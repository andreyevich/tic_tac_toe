#!/opt/homebrew/bin/python3
import random
import minimax

grid = []

for i in range(1, 10):
    grid.append(str(i))

def print_grid():
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print("-|-|-")
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print("-|-|-")
    print(grid[6] + "|" + grid[7] + "|" + grid[8])

#TODO: implement function so that the computer will always win
def get_computer_move():
    available_moves = []
    for cell in grid:
        if cell.isnumeric():
            available_moves.append(cell)
    return int(random.choice(available_moves)) - 1

# Checks whether the player won in the given rows
def did_player_win_in_rows(player, rows):
    win = False

    counter = 0
    for i in range(len(rows)):
        if rows[i] == player:
            counter += 1

        if counter == 3:
            win = True
            break

        if (i + 1) % 3 == 0:
            counter = 0
            continue

    return win

def did_player_win(player):
    win = False

    # Did the player win horizontally
    horizontal_rows = grid
    if did_player_win_in_rows(player, horizontal_rows):
        win = True

    # Did the player win vertically
    vertical_rows = []
    for i in range(0, 3):
        vertical_rows.append(grid[i])
        vertical_rows.append(grid[i + 3])
        vertical_rows.append(grid[i + 6])
    if did_player_win_in_rows(player, vertical_rows):
        win = True

    # Did the player win diagonally, baby!
    if grid[0] == grid[4] == grid[8] == player or grid[2] == grid[4] == grid[6] == player:
        win = True

    if win:
        print(player, "won!")
    return win

def is_grid_full():
    for cell in grid:
        if cell != "X" and cell != "O":
            return False
    return True

while True:
    print_grid()

    human_move = int(input("Human: enter your move: "))

    # TODO: don't allow the user to be stupid
    # # In case the user doesn't enter a number
    # try:
    #     human_move = int(input("Human: enter your move: "))
    # except:
    #     print("Invalid move... Please try again.")
    #     continue

    # In case the number is invalid.
    if grid[human_move - 1] == "O" or grid[human_move - 1] == "X" or human_move < 1 or human_move > len(grid):
        print("Invalid move... Please try again.")
        break

    grid[human_move - 1] = "X"
    if did_player_win("X"):
        break

    if is_grid_full():
        break

    computer_move = minimax.best_move(grid)
    grid[computer_move] = "O"
    print("The computer moved...")
    running = not did_player_win("O")