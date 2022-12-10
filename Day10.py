#Day 10: Cathode-Ray Tube
#Double digits baby. This time, I didn't have an hour delta, I had a 40 minute delta!
#Hey, that's improvement man. Plus, this problem was fun. But, remember kids: If you don't read instructions,
#you too will fail to make a quick solution. Be fast, but be fast AND read instructions if you want to win.
#It was difficult, but a fun problem nonetheless!

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    #Major deviation: In this input, I have forgone the array, at least initially, and decided
    #to append the instructions as one giant string
    parsed = ""

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed += line + " "

    #Then we return the split array.
    return parsed.split(" ")

#Utility: Function used to create the transverse of a table.
def transverse(data):
    t = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            t[j][i] = data[i][j]
    
    return t
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day10_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#Our parsed data has each word as an element. This whole program operates off of a particular insight
#with the data: addx and noop have as many words as cycles necessary to accomplish it. Think about that.

#A variable for the x register, a bool whether or not we've encountered an addx, and the necessary values to sum
xreg = 1
add_mode = False
needed = []

for cyc in range(len(data)):
    #If we are in a cycle of interest, we append the signal strength of it
    if(cyc + 1 in (20,60,100,140,180,220)):
        needed.append(xreg * (cyc + 1))

    #If the instruction is an addx, set add_mode to true, we're gonna encounter a number afterwards
    #If add_mode is true, add the number and set add mode back to false.
    if(data[cyc] == 'addx'):
        add_mode = True
    elif(add_mode):
        xreg += int(data[cyc])
        add_mode = False

print(sum(needed))
################################################PART 2################################################
print("\nPart 2:")

#There were so many Off-by-one errors in this code it wasn't even funny.
#Half of the time spent solving part 2 was just looking at the confusing problem statement and going 'what the heck is this'
#And the other half was spent solving off-by-one errors that occured when different things needed to be indexed by 1 vs by 0.

#The same vars as before, but now with vals to simulate the screen.
xreg = 1
add_mode = False
vals = [[" " for i in range(40)] for j in range(6)]

for cyc in range(len(data)):
    #Our current row can be calculated from the cycle by dividing it by 40.
    curr_row = (cyc)//40
    
    #Mark the pixel as lit if it's within the range of our sprite. This was a pain to tune properly.
    if(cyc in [40*curr_row + xreg + i for i in range(-1,2)]):
        vals[cyc//40][cyc%40] = "#"

    #Same xreg simulator as before.
    if(data[cyc] == 'addx'):
        add_mode = True
    elif(add_mode):
        xreg += int(data[cyc])
        add_mode = False

#Printing the result as a set of strings
for i in vals:
    print("".join(i))
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: RBPARAGP, RBPARAGR