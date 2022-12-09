#Day 9: Rope Bridge
#This day, AoC isn't pullng any punches. Holy mother of god, was Part 2 a test of patience
#and persistence. I ended up with a 1 HOUR Delta, but I don't care. Getting part 2 to work is like
#pulling teeth from a strongman that's actively resisting you. But, I managed to do it, and it's all
#thanks to one function. One simple, singular function for Part 2 that not only cleaned up my code 
#but gave me the right answer too.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(line.split(" "))

    return parsed

#This function detects if a given set of coordinates neighbors another set of coordinates,
#including diagonal neighbors. Tricky to use for utility purposes, won't include in the template,
#but good to keep in mind.
def in_range(head, tail):
    if(tail[0] in [i + head[0] for i in range(-1,2)]):
        if(tail[1] in [i + head[1] for i in range(-1,2)]):
            return True
    return False

def difference(head, tail):
    return [head[0] - tail[0], head[1] - tail[1]]

#This function, the update function, saved my hide from another hour of madness.
#The ironic part? It's only 9 lines long. A simple function that updates the position of the head and tail,
#assuming that they do not neighbor each other, even diagonally.
def update(head, tail):
    #Move row if mismatched
    if(head[0] > tail[0]):
        tail[0] += 1
    elif(head[0] < tail[0]):
        tail[0] -= 1
    
    #Move column if mismatched.
    if(head[1] < tail[1]):
        tail[1] -= 1
    elif(head[1] > tail[1]):
        tail[1] += 1
    
    return tail
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day9_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#Part 1 is easy enough. I even got a 1301 Rank out of it, which is one of my better ranks for
#my part 1's.

head = [0,0]
tail = [0,0]

traversed = []


for inst in data:
    #Extract direction and amount to move.
    direction = inst[0]
    amount = int(inst[1])

    #Each of these for loops handles one direction, and they work nearly identically to each other,
    #so for brevity, I'll only go into detail on the right movement here and in part 2.
    if(direction == "R"):
        #We move one length at a time, so that the tail can be handled properly.
        for i in range(amount):
            #Move once in the direction, then if the tail is not within range of the head, move the tail to 
            #be immediately behind the head. This logic DOES NOT carry through to Part 2, which is what made it annoying and long to solve.
            head[1] += 1
            if(not in_range(head, tail)):
                tail = [head[0],head[1] - 1]
            traversed.append(tail)
    
    #Left movement
    if(direction == "L"):
        for i in range(amount):
            head[1] -= 1
            if(not in_range(head, tail)):
                tail = [head[0],head[1] + 1]
            traversed.append(tail)
    
    #Upward movement
    if(direction == "U"):
        for i in range(amount):
            head[0] -= 1
            if(not in_range(head, tail)):
                tail = [head[0] + 1,head[1]]
            traversed.append(tail)
    
    #Downward movement.
    if(direction == "D"):
        for i in range(amount):
            head[0] += 1
            if(not in_range(head, tail)):
                tail = [head[0] - 1,head[1]]
            traversed.append(tail)

#Turn into a set to remove duplicates quickly and report length.
x = set([tuple(i) for i in traversed])
print(len(x))
################################################PART 2################################################
print("\nPart 2:")

#Oh boy, this one. This one was the difficult part, but I've stressed that enough here.
#Let's take a deep dive.

#Instead of a head and a tail, you have a sequence of coordinates for each part
#of the rope, which I thought looked like a snake from the game 'Snake,' thus the name
snake = [[0,0] for i in range(10)]
visited = set()

for inst in data:
    direction = inst[0]
    amount = int(inst[1])


    if(direction == "R"):
        for i in range(amount):
            #Move the head of the snake (the first array in the mega-array)
            snake[0][1] += 1

            #For each segment, if the segment is not in range of the next, you simply update it.
            #In hindsight, this was the obvious and cleanest way to do it, but I overcomplicated it and it led to problems.

            #I at first tried to implement the previous logic, but that failed, since you had multiple segments, and slapping
            #that logic on every 2-segment stretch did not account for all ranges of movement where some segments would move and anothers wouldn't
            #depending on the arrangment. I tried a clever approach, but it made an assumption that gave the wrong answer. Then the idea of the update
            #function stumbled on me, but I was hesitant, and stretched it out for way longer before just doing the update function.
            #It worked on the second try, after fixing a small typo. I guess the lesson here is don't be afraid to code functions
            for segment in range(len(snake) - 1):
                if(not in_range(snake[segment],snake[segment+1])):
                    snake[segment+1] = update(snake[segment],snake[segment+1])
            
            visited.add(tuple(snake[-1]))
        
    if(direction == "L"):
        for i in range(amount):
            snake[0][1] -= 1

            for segment in range(len(snake) - 1):
                if(not in_range(snake[segment],snake[segment+1])):
                    snake[segment+1] = update(snake[segment],snake[segment+1])
            
            visited.add(tuple(snake[-1]))
    
    if(direction == "U"):
        for i in range(amount):
            snake[0][0] -= 1

            for segment in range(len(snake) - 1):
                if(not in_range(snake[segment],snake[segment+1])):
                    snake[segment+1] = update(snake[segment],snake[segment+1])
            
            visited.add(tuple(snake[-1]))
    
    if(direction == "D"):
        for i in range(amount):
            snake[0][0] += 1

            for segment in range(len(snake) - 1):
                if(not in_range(snake[segment],snake[segment+1])):
                    snake[segment+1] = update(snake[segment],snake[segment+1])
            
            visited.add(tuple(snake[-1]))

#Since visited was immediately turned into a set, just ask for its length.
print(len(visited))
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 