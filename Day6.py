#Day 6: Tuning Trouble
#This one was SIGNIFICANTLY EASIER than the previous two days.
#Got a performance of 947*/913** on this one, with a delta of a measly 54 seconds.
#I was outperformed by a lot of people in the mines leaderboard, but IDC, I feel
#powerful AF. Seems weekend problems are the problems we have to watch out for.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(line)

    return parsed

################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day6_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#The data is an array of length one, containing the input, so this was to just extract it.
data = data[0]

#Look at every subset of data, and if the subset has the same contents of the set (no copies allowed),
#then each member is unique. Print the index of the last char and break.
for i in range(len(data) - 4):
    subset = list(data[i:i+4])
    if(sorted(subset) == sorted(list(set(subset)))):
        print(i + 4)
        break

################################################PART 2################################################
print("\nPart 2:")

#Same as above, but with 14 chars instead of 4. 
for i in range(len(data) - 14):
    subset = list(data[i:i+14])
    if(sorted(subset) == sorted(list(set(subset)))):
        print(i + 14)
        break

#In retrospect, I could've just done len(set(subset)) == 4 or 14, but gotta go fast, you know how it is.
#In the future, I'll have to keep an eye out for simpler solutions, but that'll come with experience.
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 