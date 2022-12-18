#Day X: Description goes here

################################################FUNCTIONS################################################
from copy import deepcopy

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(line)

    return parsed[0]

def visualize(stack):
    #For visualization and debugging purposes only
    vizy = max(stack, key = lambda k:k[0])[0]
    vizx = max(stack, key = lambda k:k[1])[1]
    grid = [["." for i in range(vizx + 1)] for j in range(vizy + 1)]
    for i in stack:
        grid[i[0]][i[1]] = "#"
    for i in reversed(grid):
        print("".join(i))

def get_neighbors(data, i, j):
    '''
    Get the neighbors of a grid cell.
    data: the grid itself.
    i: the x coordinate (row index) of the grid
    j: the y coordinate (col index) of the grid
    '''
    n = []
    sides = []
    if(i > 0):
        n.append(data[i-1][j])
        sides.append("U")
    if(i < len(data)-1):
        n.append(data[i+1][j])
        sides.append("D")
    if(j > 0):
        n.append(data[i][j-1])
        sides.append("L")
    if(j < len(data[i]) - 1):
        n.append(data[i][j+1])
        sides.append("R")
    return n, sides
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day17_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])
################################################PART 1################################################
print("Part 1:")
    
rocks = []
# x###
rocks.append(([0,0],[0,1],[0,2],[0,3]))

# .#.
# ###
# x#.

rocks.append([[0,1],[1,0],[1,1],[1,2],[2,1]])

# ..#
# ..#
# x##
rocks.append([[0,0],[0,1],[0,2],[1,2],[2,2]])

# #
# #
# #
# x
rocks.append([[0,0],[1,0],[2,0],[3,0]])

# ##
# x#
rocks.append([[0,0],[1,0],[0,1],[1,1]])

highest = 0
stack = set()
instruction = 0

for r in range(2022):
    start = deepcopy(rocks[r%5])

    for x in range(len(start)):
        start[x][0] += (highest + 3)
        start[x][1] += 2
    
    #print("New block",start)
    
    stop = False

    while(True):
        #Shift by wind
        noshift = False
        if(data[instruction] == "<" and min(start, key = lambda k: k[1])[1] != 0):
            for bit in start:
                if((bit[0],bit[1] - 1) in stack):
                    noshift = True
                    break
            
            if(not noshift):
                for x in range(len(start)):
                    start[x][1] -= 1 

        elif(data[instruction] == ">" and max(start, key = lambda k: k[1])[1] != 6):
            for bit in start:
                if((bit[0],bit[1] + 1) in stack):
                    noshift = True
                    break

            if(not noshift):
                for x in range(len(start)):
                    start[x][1] += 1
        
        #print(f"Shifted by {data[instruction]}: {start}")
        instruction = (instruction + 1) % len(data)

        #Check for collision
        for bit in start:
            if((bit[0] - 1, bit[1]) in stack or bit[0] == 0):
                stop = True
                break
        
        #Execute proper step
        if(stop):
            break
        else:
            for x in range(len(start)):
                start[x][0] -= 1

    for x in start:
        stack.add(tuple(x))
    
    #print("Stack now:")
    #visualize(stack)
    #print("")

    highest = max(stack, key = lambda k:k[0])[0] + 1

print(highest)
################################################PART 2################################################
print("\nPart 2:")
#Sending raw data to the parser to handle any in-place augmentation of data that needs to be reversed.
with open("Inputs/Day17_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

highest = [1 for i in range(7)]
instruction = 0
#insight = []

for r in range(2022):
    #insight.append(highest[:])

    start = deepcopy(rocks[r%5])

    for x in range(len(start)):
        start[x][0] += (max(highest) + 3)
        start[x][1] += 2
    
    #print("New block",start)
    
    stop = False

    while(True):
        #Shift by wind
        noshift = False
        if(data[instruction] == "<" and min(start, key = lambda k: k[1])[1] != 0):
            for bit in start:
                if(bit[0] < highest[bit[1] - 1]):
                    noshift = True
                    break
            
            if(not noshift):
                for x in range(len(start)):
                    start[x][1] -= 1 

        elif(data[instruction] == ">" and max(start, key = lambda k: k[1])[1] != 6):
            for bit in start:
                if(bit[0] < highest[bit[1] + 1]):
                    noshift = True
                    break

            if(not noshift):
                for x in range(len(start)):
                    start[x][1] += 1

        #print(f"Shifted by {data[instruction]}: {start}")
        
        instruction = (instruction + 1) % len(data)

        #Check for collision
        for bit in start:
            if(bit[0] - 1 < highest[bit[1]]):
                stop = True
                break
        
        if(stop):
            #print(start)
            break
        else:
            for x in range(len(start)):
                start[x][0] -= 1
            #print("Dropped",start)
        
    for x in start:
        highest[x[1]] = x[0] + 1

print(highest)
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 