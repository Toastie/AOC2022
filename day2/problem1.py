
points = 0

def rpc(game: str):
    game = game.replace(" ","").strip("\n")

    if game == "AX" or game == "BY" or game == "CZ":
        return 3
    elif game == "AY" or game == "BZ" or game == "CX":
        return 6
    else:
        return 0

def value(hand:str):
    if hand == "X":
        return 1
    elif hand == "Y":
        return 2
    else:
        return 3


with open("./day2/input.txt", "r") as file:
    for line in file:
        points += rpc(line) + value(line.split()[1])

print(f"Total Points: {points}")



