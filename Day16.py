#Day 16: Proboscidea Volcanium

################################################FUNCTIONS################################################
from queue import Queue
import time

class Node:
    def __init__(self, f, name):
        self.flow = f
        self.name = name
    
    def set_neighbors(self, n):
        self.neighbors = n

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []

    for line in data:
        line = line.split(" ")
        #Append line to returned data, parsed to a usable format.

        valve = line[1]
        rate = int(line[4].strip("rate=;"))

        exit_start = line.index("to")

        exits = line[exit_start+2:]

        exits_parsed = [i.strip(",") for i in exits]

        x = [valve, rate] + exits_parsed

        parsed.append(x)

    return parsed
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day16_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

valves = dict()

for valve in data:
    #print(valve)
    name, flow = valve[0:2]
    
    new = Node(flow, name)
    new.set_neighbors(valve[2:])

    valves[name] = new

'''bqueue = Queue()
#Name, rate, Accumulated pressure released, minute elapsed, valves opened
bqueue.put(('AA',0,0,0,[]))
transposition = set()

maximum = 0

quantile = 0.75

start = time.time()
while(True):
    info = bqueue.get()

    name, rate, acc, minute, opened = info

    if(acc > maximum):
        print(info)
        maximum = acc

    if(valves[name].flow > 0 and name not in opened):
        bqueue.put((name, rate + valves[name].flow, acc + rate, minute + 1, opened + [name]))
    
    if(acc >= maximum * quantile and (info[:-1], tuple(info[-1])) not in transposition):
        transposition.add((info[:-1], tuple(info[-1])))
        
        neighbors = valves[name].neighbors
        for n in neighbors:
            bqueue.put((n, rate, acc + rate, minute + 1, opened))

    if(minute > 30):
        break
end = time.time()

print(maximum)
print(f"Time taken: {end-start}:.2f")'''
################################################PART 2################################################
print("\nPart 2:")

bqueue = Queue()
#State of the puzzle, rate, Accumulated pressure released, minute elapsed, valves opened
bqueue.put((('AA','AA'),0,0,0,[]))
transposition = set()

maximum = 0
quantile = 0.2

while(True):
    info = bqueue.get()

    while((tuple(sorted(info[0])), info[1:-1], tuple(sorted(info[-1]))) in transposition):
        info = bqueue.get()

    name, rate, acc, minute, opened = info

    me, el = name

    if(acc > maximum):
        print("New max:",info)
        maximum = acc

    #Case 1: I open valve if I can, elephant moves.
    if(valves[me].flow > 0 and valves[el].flow == 0 and me not in opened):
        #print("Case 1")

        if(acc >= maximum * quantile):

            for i in valves[el].neighbors:
                state = ((me, i), rate + valves[me].flow, acc + rate, minute + 1, opened + [me])
                bqueue.put(state)
    
    #Case 2: Elephant opens valve if they can, I move.
    if(valves[me].flow == 0 and valves[el].flow > 0 and el not in opened):
        #print("Case 2")

        if(acc >= maximum * quantile):

            for i in valves[me].neighbors:
                state = ((i, el), rate + valves[el].flow, acc + rate, minute + 1, opened + [el])
                bqueue.put(state)
    
    #Case 3: We both open valves if possible, given we are in distinct rooms.
    if(valves[me].flow > 0 and valves[el].flow > 0 and me != el):
        #print("Case 3")
        #print(info)
        if(me not in opened and el not in opened):
            state = (name, rate + valves[me].flow + valves[el].flow, acc + rate, minute + 1, opened + [me, el])
            bqueue.put(state)
        elif(me not in opened):
            state = (name, rate + valves[me].flow, acc + rate, minute + 1, opened + [me])
            bqueue.put(state)
        elif(el not in opened):
            state = (name, rate + valves[el].flow, acc + rate, minute + 1, opened + [el])
            bqueue.put(state)
        #print(state)
    #Case 3.5: If we are both in the same room and a valve can be opened, send the elephant out while I open the valve
    elif(valves[me].flow > 0 and valves[el].flow > 0 and me == el and me not in opened):

        if(acc >= maximum * quantile):

            for i in valves[el].neighbors:
                state = ((me, i), rate + valves[me].flow, acc + rate, minute + 1, opened + [me])
                bqueue.put(state)

    #Case 4: We both move to new locations/do nothing, which can always be done.
    if(acc >= maximum * quantile):

        m_neighbors = valves[me].neighbors
        e_neighbors = valves[el].neighbors

        for i in m_neighbors + [me]:
            for j in e_neighbors + [el]:
                state = ((i,j), rate, acc + rate, minute + 1, opened)
                #print((i,j))
                bqueue.put(state)
    
    state = (tuple(sorted(info[0])), info[1:-1], tuple(sorted(info[-1])))
    transposition.add(state)

    if(minute > 26 or bqueue.empty()):
        break

print(maximum)
if(maximum != 1707):
    print("You are a clown, try again bucko")
################################################FAILED ANSWERS:################################################
#PART 1: 1642 (too high. I mean, yeah 1642 > 1641. You're not wrong.)
#PART 2: 2014 (too low), 2017 (too low), 2020 (too low), 2100