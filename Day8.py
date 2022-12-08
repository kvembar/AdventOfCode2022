#Day 8: Treetop Tree House
#Pretty much lost all interest in the leaderboard now. Now, I'm in it for the challenge.
#Sam has overtaken me by such a margin that I cannot hope to recover, and Sumner will soon overtake me as well.
#It is sad, yes, but something I'll just have to deal with.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append([int(i) for i in line])

    return parsed

#Function used to create the transverse of the table so that I can traverse columns easier.
#Helpful little tool for later days.
def transverse(data):
    t = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            t[j][i] = data[i][j]
    
    return t
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day8_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])
#print(transverse(data))

################################################PART 1################################################
print("Part 1:")

seen = set() #Set is used to prevent double counting of trees

for i in range(len(data)):
    #If you understand this first inner for loop, you've understood the whole program.
    tallest = -1
    for j in range(len(data[i])):
        #Seeing if the tree at (i,j) is a tree that can be seen from the edge. If so, you add it.
        if(data[i][j] > tallest):
            seen.add((i,j))
            tallest = data[i][j]
        #There used to be a else:break statement here, but turns out you shouldn't break the second you see a tree that's hidden.
    
    #Same logic, but looking from the left
    tallest = -1
    for j in range(len(data[i])-1,-1,-1):
        if(data[i][j] > tallest):
            #print(i,j)
            seen.add((i,j))
            tallest = data[i][j]

#Turns rows into columns and vice versa
data = transverse(data)

for i in range(len(data)):
    #Looking from the top to the bottom
    tallest = -1
    for j in range(len(data[i])):
        if(data[i][j] > tallest):
            #print(i,j,data[i])
            seen.add((j,i))
            tallest = data[i][j]
    
    #Looking from the bottom to the top
    tallest = -1
    for j in range(len(data[i])-1,-1,-1):
        if(data[i][j] > tallest):
            #print(i,j)
            seen.add((j,i))
            tallest = data[i][j]

#Report the number of unique trees seen.
print(len(seen))
################################################PART 2################################################
print("\nPart 2:")
data = transverse(data) #Convert data back to normal

#This one was a pain to code for, since there's a weird edge case to handle. You'll see.

scores = dict()

for i in range(len(data)):
    for j in range(len(data[i])):
        
        #Each of these while loops looks in the 4 cardinal directions to see how many trees can be seen.
        #It keeps scanning in that direction as long as you don't encounter a tree taller than the one you're on or you go out of bounds.
        tallest = data[i][j]
        up = 1
        while(i - up >= 0):
            if(data[i-up][j] < tallest):
                up += 1
            else:
                break

        down = 1
        while(i + down < len(data)):
            if(data[i+down][j] < tallest):
                down += 1
            else:
                break
        
        left = 1
        while(j - left >= 0):
            if(data[i][j-left] < tallest):
                left += 1
            else:
                break

        right = 1
        while(j + right < len(data[i])):
            if(data[i][j+right] < tallest):
                right += 1
            else:
                break
        
        #Weird edge case: If the up/down/left/right counters go off the edge of the map, they add 1 too many,
        #So we subtract 1 if the counters went OOB.
        if(i - up < 0):
            up -= 1
        if(i + down >= len(data)):
            down -= 1
        if(j - left < 0):
            left -= 1
        if(j + right >= len(data[i])):
            right -= 1

        #Save scores
        scores[(i,j)] = left*up*down*right

#Report the highest value. In hindsight, could've used just a regular array, but I thought you needed to report the location and value in my haste.
print(sorted(scores.values(), reverse = True)[0])
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 