#Day 4: Camp Cleanup
#An interval intersection problem. Fairly standard fare.
#This time around, I tried to speed up a little bit, but do the test case before the full case
#And this measurably improved my time and rank. It's not *quite* up to par, but it did establish a rhythm that
#I can follow for the rest of the problems: Do the test case, don't bother with the lore until after you've
#solved the problem, then do the full case. This does bring up the case where I pass the test, but fail
#the larger case, but we'll cross that bridge when we get there.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(",")
    #Gets rid of terminating newline(s) at the end of each line and splits each pair

    return line

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Inputs/Day4_input.txt","r") as f:
    for line in f:
        data.append(parse(line))

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#Fairly simple subset test, but my feeble brain took a hot minute to figure out other stuff.

count = 0
for i in data:
    #Don't ask me why I named these variables like so, gotta go fast.
    top = i[0].split("-")
    bottom = i[1].split("-")

    #Checking if one set is contained in the other. If I used list comprehension to convert, I would've saved like 20-30 seconds.
    if(int(top[0]) <= int(bottom[0])) and (int(bottom[1]) <= int(top[1])):
        count += 1
    elif(int(bottom[0]) <= int(top[0])) and (int(top[1]) <= int(bottom[1])):
        count += 1

print(count)
################################################PART 2################################################
print("\nPart 2:")

count = 0

for i in data:
    top = i[0].split("-")
    bottom = i[1].split("-")

    #You see, this makes things a lot simpler!
    top = [int(i) for i in top]
    bottom = [int(i) for i in bottom]

    #Basically appending every range in here, allowing for duplicates
    r = []

    #Converting the ranges to lists of numbers and adding them to r
    for j in range(top[0],top[1] + 1):
        r.append(j)
    for j in range(bottom[0],bottom[1] + 1):
        r.append(j)
    
    #Checking for duplicates, which indicates a copy of a number, implying an intersection.
    flag = True
    for j in r:
        if r.count(j) > 1:
            flag = False
            break
    
    if(not flag):
        count += 1

print(count)


################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 