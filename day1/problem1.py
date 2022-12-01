
elves = []

with open('./input1.txt', "r") as f:
    calories = 0
    for line in f:
        if len(line.strip()) == 0:
            #empty line, new elf
            elves.append(calories)
            calories = 0
        else:
            calories += int(line)

elves.sort()

#Problem 1:
print(f"Solution 1: {elves[-1:][0]}")
#Problem 2:
print(f"Solution 2: {sum(elves[-3:])}")  