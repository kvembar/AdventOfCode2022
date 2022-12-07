#Day 7: No Space Left on Device
#I. hate. everything.
#"Hey, let's make directory names repeat and not tell Keshav about it. Yeah, that'll really annoy him."
#Rank is awful and slipped down the mines leaderboard as a result. Guess I'm a big dum dum.
#Lesson here is don't assume someone names directories distinctly. I suppose that's not really much of a help in later AoC puzzles.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format thorugh splitting.
        parsed.append(line.split(" "))

    return parsed

################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day7_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("\nPart 1:")

total = 0
directories = dict()

curr_dir_path = [] #Storing the whole directory path for key generation

for command in data:
    #A change of directory indicates a new directory, add it to the current path and add it to the hashmap of directories
    if(command[1] == "cd" and command[2] != ".."):
        curr_dir_path.append(command[2])
        directories[" ".join(curr_dir_path)] = 0
    #.. moves up a directory, so we augment the path as a result.
    elif(command[1] == "cd" and command[2] == ".."):
        curr_dir_path.pop()

curr_dirs = []
for command in data:
    #Similar logic as above to keep track of the directory/directories we are in.
    if(command[1] == "cd" and command[2] != ".."):
        curr_dirs.append(command[2])
    elif(command[1] == "cd" and command[2] == ".."):
        curr_dirs.pop()
    elif(command[0].isdigit()):
        for i in range(len(curr_dirs)):
            #We add our file size to every directory coming up to the top, since a file in a/b/file is added to directory a/b and a.
            true_curr_dir = " ".join(curr_dirs[:i+1])
            directories[true_curr_dir] += int(command[0])

#Filter adding
for v in directories.values():
    if(v <= 100000):
        total += v

print(total)
################################################PART 2################################################
print("\nPart 2:")

#Straightforward, calculate free space, then find the minimum value satisfying certain requirements.
total = directories["/"]
amount = 70000000
free_space = amount - total

smallest = ""
val = 3000000000000000

print(total)
for d in directories.keys():
    #If free_space + the space in the directory gives us the value we need, and its is smaller than any val we might've found, set the minimum to such.
    if(free_space + directories[d] >= 30000000 and directories[d] < val):
        smallest = d
        val = directories[d]

print(smallest, val)
################################################FAILED ANSWERS:################################################
#PART 1: 899654
#PART 2: 12534602