#Day 18: Description goes here

################################################FUNCTIONS################################################
from queue import Queue

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(tuple(int(i) for i in line.split(",")))

    return parsed


def bfs(cubes, start, goal, ext, internal):
    bqueue = Queue()
    bqueue.put(start)

    visited = set()

    while(not bqueue.empty()):
        process = bqueue.get()

        if(process in visited):
            continue

        visited.add(process)

        x,y,z = process

        neighbors = ((x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1))

        for n in neighbors:
            if(n not in cubes):
                bqueue.put(n)
            if(n == goal or n in ext):
                return visited
            if(n in internal):
                return False

    return False
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day18_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
print(data[:10])

################################################PART 1################################################
print("Part 1:")
cubes = set(data)

surface = 0

for cube in data:

    opened = 6

    x,y,z = cube

    if((x+1,y,z) in cubes):
        opened -= 1
    if((x,y+1,z) in cubes):
        opened -= 1
    if((x,y,z+1) in cubes):
        opened -= 1
    if((x-1,y,z) in cubes):
        opened -= 1
    if((x,y-1,z) in cubes):
        opened -= 1
    if((x,y,z-1) in cubes):
        opened -= 1
    
    surface += opened

print(surface)
################################################PART 2################################################
print("\nPart 2:")

max_x = max(cubes, key = lambda k: k[0])[0]
max_y = max(cubes, key = lambda k: k[1])[1]
max_z = max(cubes, key = lambda k: k[2])[2]

internal = set()
external = set()

goal = (0,0,0)

for x in range(max_x):
    for y in range(max_y):
        for z in range(max_z):
            if((x,y,z) not in cubes):
                #print(x,y,z)
                reachable = bfs(cubes, (x,y,z), goal, external, internal)
                if(type(reachable) is bool):
                    internal.add((x,y,z))
                elif(len(external) < len(reachable)):
                    for i in reachable:
                        external.add(i)

for i in internal:
    x,y,z = i
    if((x+1,y,z) in cubes):
        surface -= 1
    if((x,y+1,z) in cubes):
        surface -= 1
    if((x,y,z+1) in cubes):
        surface -= 1
    if((x-1,y,z) in cubes):
        surface -= 1
    if((x,y-1,z) in cubes):
        surface -= 1
    if((x,y,z-1) in cubes):
        surface -= 1

print(surface)
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 4062