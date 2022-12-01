#Day X: Description goes here

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
with open("Inputs/DayX_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

#Checking the parsing (if necessary):
#print(data)

################################################PART 1################################################
print("Part 1:")
    


################################################PART 2################################################
#print("\nPart 2:")



################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 