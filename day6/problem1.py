line = open("./day6/input.txt","r").readline()

size = 14

for i in range(len(line) - size):
    window = line[i:i+size]
    duplicates = 0
    for char in window:
        duplicates += 1 if window.count(char) > 1 else 0
    if duplicates == 0:
        print( i + size )
        break