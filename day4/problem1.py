overlap = 0

with open("./day4/input.txt","r") as input:
    for line in input:
        elves = line.split(",")

        a = [ int(x) for x in  elves[0].split("-")]
        b = [ int(x) for x in  elves[1].split("-")]


        if a[0] >= b[0] and a[1] <= b[1]:
            overlap += 1
        elif b[0] >= a[0] and b[1] <= a[1]:
            overlap  += 1


print(f"No. of total overlaps: {overlap}")
