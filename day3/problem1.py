rucksacks = []

duplicates = []

with open("./day3/input.txt","r") as input:
    for line in input:
        line = line.strip()
        length = len(line) // 2 
        rucksacks.append( [line[:length], line[length:]] )

for rucksack in rucksacks:
    for i in range(len(rucksack[0])):
        if rucksack[1].count(rucksack[0][i]) != 0:
            duplicates.append(rucksack[0][i])
            break

sum = 0

print(duplicates)

for char in duplicates:
    if char.islower():
        sum += ord(char) - ord( "a" ) + 1
    else:
        sum += ord(char) - ord("A") + 27

print(sum)