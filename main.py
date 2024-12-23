#!/opt/homebrew/bin/python3
# TODO: add error handling
# TODO: add gui
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


while True:
    print_grid()

    human_move = int(input("Human, enter your move: "))
    grid[human_move - 1] = "X"
    if minimax.is_terminal(grid) == -1:
        print("Human, you won!")
        break
    elif minimax.is_terminal(grid) == 0:
        print("Tie!")
        break

    computer_move = minimax.best_move(grid)
    grid[computer_move] = "O"

    if minimax.is_terminal(grid) == 1:
        print("Human, you're a loser!")
        break
    elif minimax.is_terminal(grid) == 0:
        print("Tie!")
        break
