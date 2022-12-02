#Day 2: Rock Paper Scissors
#Holy guacamole, this one was a disasterpiece. Had a delta of 11 minutes on this one
#The problem itself wasn't difficult, but my rushing made it more difficult.
#Lesson of today? Don't rush, take a deep breath, panicking will only lengthen your time.
#One slow correct answer is faster than 100 fast incorrect answers, and beware the siren of copy-pasting
#If you do engage with copy-pasting, keep a close eye on every line. Wasted attempts come from lines you were supposed to delete.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(" ") 
    #Gets rid of terminating newline(s) at the end of each line

    return line

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Inputs/Day2_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

#Checking the parsing (if necessary):
#print(data[-1])

################################################PART 1################################################
print("Part 1:")
#Took a hot second to get this one, but managed to clear it in 7 minutes
#Had a couple of failed inputs because I thought it was me-them, and not them-me.

score = 0

for i in data:
    #Score based off of what I got.
    score += ord(i[1]) - 87
    #Tie conditions
    if (i in [['A','X'],['B','Y'],['C','Z']]):
        score += 3
    #Win conditions
    elif (i in [['A','Y'],['B','Z'],['C','X']]):
        score += 6
    #Losing conditions
    else:
        score += 0

print(score)
################################################PART 2################################################
print("\nPart 2:")

score = 0

for i in data:
    #Tie conditions, where we simply convert the opponent's throw into a numerical representation of the input.
    if(i[1] == 'Y'):
        score += ord(i[0]) - 64 + 3

    #Losing conditions. Had to hard code these ones, since my brain was a bit fried. Kelly's mod 3 solution would've helped here tbh
    elif(i[1] == 'X'):
        if(i[0] == 'A'):
            score += 3
        elif(i[0] == 'B'):
            score += 1
        elif(i[0] == 'C'):
            score += 2
    
    #Winning conditions
    else:
        if(i[0] == 'A'):
            score += 8
        elif(i[0] == 'B'):
            score += 9
        elif(i[0] == 'C'):
            score += 7

print(score)

################################################FAILED ANSWERS:################################################
#PART 1: 13714, 12196
#PART 2: 18437, 18477