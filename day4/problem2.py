overlap = 0

with open("./day4/input.txt","r") as input:
    for line in input:
        elves = line.split(",")

        a = [ int(x) for x in  elves[0].split("-")]
        b = [ int(x) for x in  elves[1].split("-")]


        if a[0] <= b[1] and b[0] <= a[1]:
            overlap += 1


print(f"No. of total overlaps: {overlap}")
