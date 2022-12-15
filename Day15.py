#Day 15: Beacon Exclusion Zone
#Welp, today was an optimization problem. And I *hate* optimization problems
#Mostly because I'm too stupid to figure them out immediately in a competitive context
#I had to sleep on part 2, since I couldn't get it the night before, but I managed to do it!

################################################FUNCTIONS################################################

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []

    for line in data:
        line = line.split(" ")
        #Append line to returned data, parsed to a usable format.

        sensor_x = int(line[2].strip("=,x"))
        sensor_y = int(line[3].strip("=:y"))

        beacon_x = int(line[-2].strip("=,x"))
        beacon_y = int(line[-1].strip("=,y"))

        parsed.append([[sensor_x, sensor_y],[beacon_x, beacon_y]])

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

#Simple manhattan helper function to calculate all covered areas in a particular row.
def manhattan_helper(x, y, d):
    global roi
    
    the_list = []

    for i in range(-d,d+1):
        j = roi - y
        if(abs(j) + abs(i) <= d):
            the_list.append((x+i,y+j))
    
    return the_list
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day15_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#ns = negative space (where a beacon isn't)
ns = set()

#list of beacons to prevent false identification based purely on manhattan distance
beacons = set()

#Row of interest, for quick switching between sample and real test cases
roi = 2000000

for group in data:
    #Extract sensor and beacon from group
    sensor = group[0]
    beacon = group[1]

    beacons.add(tuple(beacon))

    #Calculate manhattan distance between the two
    manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    #Find all coordinates that have that manhattan distance@ROI and add to ns
    result = manhattan_helper(sensor[0],sensor[1],manhattan)

    if(type(result) is tuple):
        ns.add(result)
    else:
        for i in result:
            ns.add(i)


#Extract all values in ns that have the same row as our row of interest and that are not beacons already.
total = 0
for i in sorted(ns):
    if(i[1] == roi and i not in beacons):
        total += 1
print(total)
################################################PART 2################################################
print("\nPart 2:")
#Sending raw data to the parser to handle any in-place augmentation of data that needs to be reversed.
with open("Inputs/Day15_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#This part I had to sleep on to get the 'interval' idea that I needed to compute this.

#Bound for x and y in search area
bound = 4000000

for row in range(0,bound + 1):
    #If you wish to run this code, it will take about 30-60 seconds. Uncomment this for a 'progress bar' of sorts.
    '''if(row%10000 == 0):
        print(row)'''
    intervals = []

    for group in data:
        #Extract sensor and beacon information
        sensor, beacon = group

        #Calculate manhattan distance
        manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        #Generate interval covered in row (dtr = distance to row)
        dtr = abs(sensor[1] - row)

        radius = manhattan - dtr
        
        #If radius > 0, then the sensor will reach the row, add the interval it covers to list of intervals
        if(radius > 0):
            interval_covered = [max(0,sensor[0]-radius), min(bound,sensor[0]+radius)]
            intervals.append(interval_covered)
    
    #Proceed to merge all intervals together in merged, and have a flag variable for when we detect a hole.
    merged = min(intervals)
    caught = False

    #We sort the intervals for simplicity in merging and checking.
    #If the merged interval is disjoint from any particular interval, we've found our hole.
    #If it isn't, then merge them together.
    for i in sorted(intervals):
        if(max(merged) < min(i) - 1):
            missed = (max(merged) + min(i)) // 2
            print(f"Missing something in row {row}: {missed}")
            print(row + missed * bound)
            caught = True
            break
        else:
            merged = [min(merged + i), max(merged + i)]
    
    #Stop computing if we find our magic interval.
    if(caught):
        break

#Correct answer is 13,267,474,686,239. Yeah, a pretty big number alright.
#Turns out in my input, in row 2686239, there exists ONE hole in the data at column 3316868.
#These elves that I'm saving better have coupons for me for trying to save their asses.

################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 10744959316868 (too low)