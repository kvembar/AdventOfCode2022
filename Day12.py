#Day 12: Hill Climbing Algorithm
#Ladies and gentlemen, we have succeeded! I have managed to score my lowest rank on Part 2 in the past week
#And I scored 5th on the leaderboard baby! We're back in business... for now. Will it last? Only time will tell.
#I am proud of my solution, which is the first day where I made a mostly/purely functional solution. Thought I would need
#recursion, but I did not end up doing it lol.

################################################FUNCTIONS################################################
from queue import Queue
from queue import PriorityQueue

#Parse function used during input
def parse(data):
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(list(line))

    return parsed

#Utility: Function used to create the transverse of a table.
def transverse(data):
    t = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            t[j][i] = data[i][j]
    
    return t

#Utility: Get neighbors of coordinates of grid cell, as well as their directions (sides).
#Will be helpful for later days. I am adding this to the template.
def get_neighbors(data, i, j):
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

#The function used for part 1's implementation. This won't be a utility function, since
#graphs can come in a million different forms, and coding it from scratch is the meta.
def bfs_grid_part_1(data, start, end):

    #BFS Queue implementation always starts with a queue and your starting vertex, which stores the starting coordinates and a distance of 0.
    gqueue = Queue()
    gqueue.put((start, 0))

    #Visited set to prevent cycles.
    visited = set()

    while(not gqueue.empty()):
        obj = gqueue.get()

        #Unpacking of object
        coordinates = obj[0]
        dist = obj[1]

        #Visited vertex check
        if(coordinates not in visited):
            visited.add(coordinates)
        else:
            continue

        #Height variable stores, you guessed it, height as an ASCII code.
        height = ord(data[coordinates[0]][coordinates[1]])

        #We get our neighbors from our utility function.
        neighbors, sides = get_neighbors(data, coordinates[0], coordinates[1])

        #Check if we've reached the end
        if(coordinates == end):
            return dist

        #For each of the neighbors, check if we can traverse to that neighbor (with a special case for our starting node)
        #And using the sides[i] variable, note which neighbor it is that we need to add, then add the neighbor and add 1 to the distance to get there.
        for i in range(len(neighbors)):
            if(sides[i] == "L" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                gqueue.put(((coordinates[0],coordinates[1] - 1),dist + 1))
            elif(sides[i] == "R" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                gqueue.put(((coordinates[0],coordinates[1] + 1),dist + 1))
            elif(sides[i] == "U" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                gqueue.put(((coordinates[0] - 1,coordinates[1]),dist + 1))
            elif(sides[i] == "D" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                gqueue.put(((coordinates[0] + 1,coordinates[1]),dist + 1))

    #No path found, so we return None, indicates error.
    return None

#I needed an augmented BFS search for part 2, thus this definition. Only a few things change, so I'll highlight those.
#I am very proud of this solution, since I get to use big-boy Algorithms and Data Structure terms.
def bfs_grid_part_2(data, start, end):

    #Since there are multiple possible starting points, we need to find the most efficient one out of all of them,
    #which means we have to extract the smallest distance node over and over again. The best way to do that?
    #A priority queue, which is just a queue that guarantees that the value coming out is the minimum in all of the queue.
    gqueue = PriorityQueue()

    #Here, I add to queue with a tuple containing distance THEN coordinate so that the Priority Queue can work its magic.
    gqueue.put((0, start))

    visited = set()

    while(not gqueue.empty()):
        obj = gqueue.get()

        coordinates = obj[1]
        dist = obj[0]

        if(coordinates not in visited):
            visited.add(coordinates)
        else:
            continue

        height = ord(data[coordinates[0]][coordinates[1]])
        neighbors, sides = get_neighbors(data, coordinates[0], coordinates[1])

        if(coordinates == end):
            return dist

        #Here, distance only gets added by 1 if the height is not 'a,' ASCII Code 97. Otherwise, we add it with 0 distance added,
        #since we can start at any 'a' height connected to S.
        for i in range(len(neighbors)):
            if(sides[i] == "L" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                if(height != 97):
                    gqueue.put((dist + 1, (coordinates[0],coordinates[1] - 1)))
                else:
                    gqueue.put((dist,(coordinates[0],coordinates[1] - 1)))
            elif(sides[i] == "R" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                if(height != 97):
                    gqueue.put((dist + 1,(coordinates[0],coordinates[1] + 1)))
                else:
                    gqueue.put((dist,(coordinates[0],coordinates[1] + 1)))
            elif(sides[i] == "U" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                if(height != 97):
                    gqueue.put((dist + 1,(coordinates[0] - 1,coordinates[1])))
                else:
                    gqueue.put((dist,(coordinates[0] - 1,coordinates[1])))
            elif(sides[i] == "D" and (height == 83 or ord(neighbors[i]) <= height + 1)):
                if(height != 97):
                    gqueue.put((dist + 1,(coordinates[0] + 1,coordinates[1])))
                else:
                    gqueue.put((dist,(coordinates[0] + 1,coordinates[1])))

    return None
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day12_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#Extracting the start and end coordinates for bfs_grid_part_1
for i in range(len(data)):
    for j in range(len(data[i])):
        if(data[i][j] == "S"):
            start = (i,j)
        elif(data[i][j] == "E"):
            end = (i,j)
            #Setting end to "z" and storing end variable allows for height difference to be detected.
            data[i][j] = "z"

#Run part 1. See implementation above
print(bfs_grid_part_1(data, start, end))
################################################PART 2################################################
print("\nPart 2:")

#Just run part 2, nothing too crazy there. See implementation above and part 1 for more details.
#Fun fact, my solution to part 1 was 481, and my solution to part 2? 480. Just a one unit improvement lol.
print(bfs_grid_part_2(data, start, end))
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 