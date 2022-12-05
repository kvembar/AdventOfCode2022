#Day 5: Supply Stacks
#So, I have some words to say about this.
#First off: WHO THOUGHT THIS WAS AN ACCEPTABLE DAY 5 PROBLEM, YEA THE LOGIC IS EASY, BUT
#THE PARSING WOULD'VE BEEN SO AWFUL TO DO HAD I NOT CHOSE TO CHANGE THE DAY 5 INPUT
#SO THAT IT WOULD BE EASIER TO CODE.
#But second off: this problem made me realize that it may actually be easier to read in the whole file,
#split by newline, and parse the whole file rather than each line, so I'll be modifying the template accordingly.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    #Flag variable that delineates stacks from instructions
    instr_mode = False

    #arrays that hold each of the stacks of crates and the instructions for moving, simplified.
    stacks = []
    instr = []

    for l in range(len(line)):
        #Gets rid of terminating newline(s) at the end of each line
        line[l] = line[l].rstrip("\n").split(" ")
        
        #Switch modes at a newline
        if line[l] == [""]:
            instr_mode = True
            continue


        if(instr_mode == False):
            #Add stacks to array
            stacks.append(line[l])
        else:
            #Add instructions' numbers to array, which are always at these indexes.
            x = [int(line[l][1]), int(line[l][3]), int(line[l][5])]
            instr.append(x)

    return stacks, instr

################################################PARSING################################################

#Sending raw data to the parser, now modified to read in the whole file. Had to make this change on the fly
#NOTE: The input file had to be changed in order to make the code work, where the crates changed from being read top to bottom in columns to rows from left ro right.
#Refer to the input txt file in "Inputs" folder for clarification. Each row reads the crates from top to bottom in each stack. It was easy enough to hardcode/change, so I did.
with open("Inputs/Day5_input.txt","r") as f:
    d = f.read().split("\n")
    stacks, instr = parse(d)

#Checking the parsing (if necessary):
#print(stacks)
#print(instr)

################################################PART 1################################################
print("Part 1:")

#Once I hardcoded the stacks, it was easy enough to solve by following the instructions

for instruction in instr:
    #Disambiguating what the numbers mean for convenience and quicker coding
    amount = instruction[0]
    source = instruction[1]
    dest = instruction[2]

    #Moving amount crates from source to destination, one at a time. Made solving Part 2 easier.
    for x in range(amount):
        crate = stacks[source - 1][0]
        stacks[source - 1] = stacks[source - 1][1:]
        stacks[dest - 1] = [crate] + stacks[dest - 1]

#Print out each topmost crate in an easy to copy-paste fashion.
for s in stacks:
    print(s[0], end = "")
################################################PART 2################################################
print("\nPart 2:")

#Reread input, since we modified the vars themselves.
with open("Inputs/Day5_input.txt","r") as f:
    d = f.read().split("\n")
    stacks, instr = parse(d)

#Only a slight change here to move the crates together rather than one at a time.
for instruction in instr:
    amount = instruction[0]
    source = instruction[1]
    dest = instruction[2]

    crate = stacks[source - 1][:amount]
    stacks[source - 1] = stacks[source - 1][amount:]
    stacks[dest - 1] = crate + stacks[dest - 1]

#Print out each topmost crate in an easy to copy-paste fashion.
for s in stacks:
    print(s[0], end = "")
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 