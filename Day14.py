#Day 14: Regolith Reservoir
#Had to start this problem late to due to a dinner tradition with a friend.
#This was actually a fun problem to try and mess around with! Surprisingly simple
#and efficient to do, even though Part 2 needed to think for a bit to execute.
#Not much else to say other than that. Finals at college are over!!

################################################FUNCTIONS################################################

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []

    for line in data:
        line = line.split(" -> ")
        
        line = [i.split(",") for i in line]

        for j in range(len(line)):
            line[j] = [int(x) for x in line[j]]

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
with open("Inputs/Day14_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#Normalize the data so that the numbers start at 0.

#Identify the minimum x to scale all x's by.
minx = 100000000000000000

for x in data:
    for y in x:
        if(y[0] < minx):
            minx = y[0]

#Scale the x coordinate (read: column coordinate) and identify maxes of x and y to generate table
maxy = -1
maxx = -1
for x in range(len(data)):
    for y in range(len(data[x])):
        data[x][y][0] -= minx

        if(data[x][y][0] > maxx):
            maxx = data[x][y][0]
        if(data[x][y][1] > maxy):
            maxy = data[x][y][1]

#Generate table from maxes and mins
table = [["." for i in range(maxx + 1)] for j in range(maxy + 1)]

#Generate walls from data
for x in data:
    previous = []

    for endpoint in x:
        #If we are at the start of a new set of walls x, previous will be empty. Set previous to start of wall and proceed
        if(previous == []):
            previous = endpoint
            continue

        #Using the data on the stretch of wall, we identify which axis it goes across and draw it on the table.
        #The x and y positions are a bit counterintuitive because I accidentally swapped my x and y from my identification earlier. Whoops.
        #Thankfully all that happens is that I get the transpose of the data, so a simple swap fixed it.
        if(previous[0] == endpoint[0]):
            start, end = sorted([previous[1],endpoint[1]])

            for i in range(start, end+1):
                table[i][previous[0]] = "#"
        elif(previous[1] == endpoint[1]):
            start, end = sorted([previous[0],endpoint[0]])

            for i in range(start, end+1):
                table[previous[1]][i] = "#"

        previous = endpoint

#Simulate Sand Falling

#Starting coordinate (using earlier scaling) for sand to fall
xcoord = 500 - minx
ycoord = 0

#continue until breaking condition is met.
while(True):
    #Breaking condition: If we ever get a sand grain that goes off the deep end,
    #where it goes lower than the maxy or the xcoord is negative, indicating that the particle
    #has no wall underneath it.
    if(ycoord >= maxy or xcoord < 0):
        break

    #Movement simulation, according to problem
    if(table[ycoord + 1][xcoord] == "."):
        ycoord += 1
    elif(table[ycoord + 1][xcoord - 1] == "."):
        ycoord += 1
        xcoord -= 1
    elif(table[ycoord + 1][xcoord + 1] == "."):
        ycoord += 1
        xcoord += 1
    elif("." not in table[ycoord + 1][xcoord - 1 : xcoord + 2]):
        #If there is no empty space in the lower neighbors (including diagonals), we mark a sand particle and reset position for a new sand particle.
        table[ycoord][xcoord] = "o"
        xcoord = 500 - minx
        ycoord = 0

#Counting o's in the graph
total = 0
for i in table:
    total += i.count("o")
print(total)
################################################PART 2################################################
print("\nPart 2:")

#This part 2 was challenging, but in a good way.

#Reread data. I will from now on, be making this a staple of the template to read the input twice.
with open("Inputs/Day14_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Implementation is nearly identical except in a few places, where I'll make special mention of it.

#Normalize data
minx = 100000000000000000

for x in data:
    for y in x:
        if(y[0] < minx):
            minx = y[0]

maxy = -1
maxx = -1
for x in range(len(data)):
    for y in range(len(data[x])):
        data[x][y][0] -= minx

        if(data[x][y][0] > maxx):
            maxx = data[x][y][0]
        if(data[x][y][1] > maxy):
            maxy = data[x][y][1]

#Generate table
table = [["." for i in range(maxx + 1)] for j in range(maxy + 1)]

#Generate walls
for x in data:
    previous = []

    for endpoint in x:
        if(previous == []):
            previous = endpoint
            continue

        
        if(previous[0] == endpoint[0]):
            start, end = sorted([previous[1],endpoint[1]])

            for i in range(start, end+1):
                table[i][previous[0]] = "#"

        elif(previous[1] == endpoint[1]):
            start, end = sorted([previous[0],endpoint[0]])

            for i in range(start, end+1):
                table[previous[1]][i] = "#"

        previous = endpoint

#Extend table for part 2, since we now have a floor and the room is way bigger.
table.append(["." for i in range(maxx + 1)])

#I had to pick for how long the x axis had to be extended by. I just picked the other max and used that, and it worked.
for row in range(len(table)):
    table[row] = ["." for i in range(maxy)] + table[row] + ["." for i in range(maxy)]

#Append the floor of the room
table.append(["#" for i in range(len(table[-1]))])

#Simulate Sand
xcoord = 500 - minx + maxy  #Now we need to add maxy to the scale since we extended the x axis by maxy on the left.
ycoord = 0
while(True):
    if(table[0][500 - minx + maxy] == "o"):
        break

    if(table[ycoord + 1][xcoord] == "."):
        ycoord += 1
    elif(table[ycoord + 1][xcoord - 1] == "."):
        ycoord += 1
        xcoord -= 1
    elif(table[ycoord + 1][xcoord + 1] == "."):
        ycoord += 1
        xcoord += 1
    elif("." not in table[ycoord + 1][xcoord - 1 : xcoord + 2] or ycoord == maxy + 1):
        table[ycoord][xcoord] = "o"
        xcoord = 500 - minx + maxy
        ycoord = 0

#Count the number of o's.
total = 0
for i in table:
    total += i.count("o")
print(total)

################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 