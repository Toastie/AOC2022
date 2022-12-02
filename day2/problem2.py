
points = 0

def replace(line:str):
    return line.replace("A", "1").replace("B", "2").replace("C","3")

def rpc(game: str):
    game = replace(game).split()

    if game[1] == "Y":
        #DRAW
        return 3 + int(game[0])
    if game[1] == "Z":
        #WIN
        return 6 + (int(game[0]) % 3) + 1
    else:
        #LOSE
        res = int(game[0]) - 1
        return res if res != 0 else 3


with open("./day2/input.txt", "r") as file:
    for line in file:
        points += rpc(line)

print(f"Total Points: {points}")



