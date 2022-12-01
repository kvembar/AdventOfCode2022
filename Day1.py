#Day 1: Calorie Counting
#And so AoC begins for 2022! This one was a Speedy-Gonzalez problem. 
#Like Sonic, I gotta go fast, and I ended up with a Rank of 627 for this problem on Part 2
#But someone in the chat ended up ranking 42! RANK 42! He's absolutely crazy.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n") 
    #Gets rid of terminating newline(s) at the end of each line

    return line

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Inputs/Day1_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")
#This one was easy. Real easy to complete once I realized just how fast I had to be.

#m is the list of sums for each elf
m = []

#The variable keeping track of the sum for each
running_sum = 0

for i in data:
    #Delimiter checking, adding if we encounter a number, appending and resetting the sum to 0 if we encounter the delimiter
    if(i != ""):
        running_sum += int(i)
    else:
        m.append(running_sum)
        running_sum = 0

#Part 1 simply asks that you print the maximum of m, the elf with the most calories
print(max(m))
################################################PART 2################################################
print("\nPart 2:")
#This one was even easier.

#Sort and sum. That's it.
s = sorted(m, reverse=True)
print(sum(s[:3]))

################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 