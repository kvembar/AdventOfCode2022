#Day 7: Description goes here

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
with open("Inputs/Day7_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")
    


################################################PART 2################################################
#print("\nPart 2:")



################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 