#!/opt/homebrew/bin/python3
import minimax
state = [
        "X", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
]

print(minimax.min_value(state))
