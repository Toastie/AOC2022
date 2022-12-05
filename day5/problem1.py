import re

no = 9

stacks = [[] for i in range(no)]
moves = []
with open("./day5/input.txt","r") as input:
    for line in input:
        


        if len(line.strip()) != 0 and line.strip().split()[0] != "move":
            # Build the Stacks
            #for i in range(1,12,4):
            for i in range(1,35,4):
                if re.match("[A-Z]",line[i]) != None:
                    stacks[i//4].insert(0, line[i] )
        elif len(line.strip()) == 0:
            continue
        else:
            line = line.replace("move ","").replace("from ","").replace("to ","").split()
            moves.append([ int(line[x]) for x in range(3)])

for move in moves:
    for i in range(move[0]):
        stacks[move[2] - 1].append( stacks[move[1] - 1].pop() )

print("".join( str(stacks[x][-1:][0]) for x in range(no) ) )        
