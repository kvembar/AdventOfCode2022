#Day 13: Description goes here

################################################FUNCTIONS################################################

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(line)

    return parsed

def transverse(data):
    '''
    Returns the transverse of a grid/table.
    '''
    t = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            t[j][i] = data[i][j]
    
    return t

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
with open("Inputs/Day13_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")
    


################################################PART 2################################################
#print("\nPart 2:")



################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 