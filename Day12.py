#Day 12: Description goes here

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    parsed = []

    for line in data:
        #Append line to returned data, parsed to a usable format.
        parsed.append(line)

    return parsed

#Utility: Function used to create the transverse of a table.
def transverse(data):
    t = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            t[j][i] = data[i][j]
    
    return t
################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day12_input.txt","r") as f:
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