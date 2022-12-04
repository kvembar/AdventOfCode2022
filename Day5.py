#Day 5: Description goes here

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n") 
    #Gets rid of terminating newline(s) at the end of each line
    #Feel free to remove that if necessary for code.

    return line

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Inputs/Day5_input.txt","r") as f:
    for line in f:
        data.append(parse(line))

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")
    


################################################PART 2################################################
#print("\nPart 2:")



################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 