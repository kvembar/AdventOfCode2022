#Day 3: Rucksack Reorganization
#Today, I have decided to change my approach in light of yesterday's disaster.
#I decided to... actually *read* the problem, and do the test cases before I did my actual input.
#This was simultaneously a good and bad decision, as I got both first try, but performance suffered a bit.
#I went up the leaderboard today! I'm now in 4th place! But I'll have to speed up, which is hard to do when
#you have ONE MONITOR, but I'll have to make do for now until school goes back in session for finals.

################################################FUNCTIONS################################################

#Parse function used during input
#Side Note: If I made this parse split for part 1, it would've been disastrous for part 2
#Take notes kids, only augment this for special line-by-line purposes.
def parse(line):
    line = line.rstrip("\n") 
    #Gets rid of terminating newline(s) at the end of each line

    return line

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Inputs/Day3_input.txt","r") as f:
    for line in f:
        data.append(parse(line))

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")
#This one was fairly simple to implement, but required a bit of thinking power
#to make a proper game plan.

#This array will hold the common types of items found in each rucksack
common = []

for i in data:
    #First and second compartments of each rucksack
    fst = i[:(len(i)//2)]
    snd = i[len(i)//2:]
    
    #One-liner for getting the list of unique items in the entire pack
    unique = list(set([i for i in fst + snd]))
    
    #If the unique item is in both, we have found the bad item and append it to common, break to move on to the next sack
    for u in unique:
        if (u in fst) and (u in snd):
            common.append(u)
            break
    
#Conversion of item ID to numerical value using ASCII conversion
#Didn't have to look the ASCII conversion tables on this one, thanks brain for remembering that!
for i in range(len(common)):
    if(common[i].islower()):
        common[i] = ord(common[i]) - 96
    else:
        common[i] = ord(common[i]) - 64 + 26

print(sum(common))
################################################PART 2################################################
print("\nPart 2:")
#This solution was nearly identical, but I had to account for grouping by all three lol.

grouped = []
temp = []

#Grouping the items by three using a counter and a temp to compartmentalize each group.
for i in range(len(data)):
    if(i % 3 == 0 and i != 0):
        grouped.append(temp)
        temp = [data[i]]
    else:
        temp.append(data[i])
grouped.append(temp)

#Same process as Part 1, but this time we check all three rucksacks in a group for the unique values
common = []

for i in grouped:

    combined = i[0] + i[1] + i[2]
    unique = list(set([i for i in combined]))

    for u in unique:
        if (u in i[0]) and (u in i[1]) and (u in i[2]):
            common.append(u)
            break

#Same conversion as before.
for i in range(len(common)):
    if(common[i].islower()):
        common[i] = ord(common[i]) - 96
    else:
        common[i] = ord(common[i]) - 64 + 26

print(sum(common))
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 