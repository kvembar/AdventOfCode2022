#Day 11: Monkey in the Middle
#I have a confession to make for this one: I kinda cheated for part 2, I got a hint from the discord chat
#And implemented a solution from there. Going forward, I plan not to do that. I'll struggle for as long as 
#I can before I break. In other news, this was actually a fun problem to solve, if a little intimidating at
#first though.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(data):
    parsed = []
    #The array that will contain each monkey.
    new_monkey = []

    for line in data:
        line = line.strip(" ")

        #An empty line delineates monkeys, so we use it as an indicator to add to parsed.
        if(line == ""):
            #Append line to returned data, parsed to a usable format.
            parsed.append(new_monkey)
            new_monkey = []
            continue
        #Otherwise, we split the line for the upcoming massiv if-elif statement.
        else:
            line = line.split(" ")
        
        #Each of these ifs looks for a certain word in the line that indicates what data we're working with and constructs it accordingly.
        if(line[0] == "Monkey"):
            continue
        elif(line[0] == "Starting"):
            new_monkey.append([int(i.strip(",")) for i in line[2:]])
        elif(line[0] == "Operation:"):
            new_monkey.append(line[4:])
        elif(line[0] == "Test:"):
            new_monkey.append(int(line[-1]))
        elif(line[1] in ("true:","false:")):
            new_monkey.append(int(line[-1]))

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
with open("Inputs/Day11_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

inspected = [0 for i in data]  

#Simulate 20 rounds
for r in range(20):
    
    for monkey in data:

        #For each monkey, we analyze all of the items it has and move them accordingly.
        while(monkey[0] != []):
            #Pop the first item and add one to the monkey's inspection number
            item = monkey[0].pop(0)
            inspected[data.index(monkey)] += 1

            #Identify the operation. Yes, I could've used lambdas or eval, but I was too lazy to remind
            #myself how those worked.
            op = monkey[1][0]

            #Identify the second operand, replacing 'old' with the first operand if it is there.
            if(monkey[1][1] == "old"):
                second = item
            else:
                second = int(monkey[1][1])

            #Implementation of operand
            if(op == "*"):
                worry = item * second
            elif(op == "+"):
                worry = item + second
            elif(op == "-"):
                worry = item + second
            
            #Worry decreases according to this.
            worry //= 3

            #Identify if the monkey is bored via the divisibility test
            if(worry % monkey[2] != 0):
                bored = True
            else:
                bored = False

            #Add item to monkey's list according to true-false indicated in the file.
            #monkey[-1] contains the monkey that will recieve the item if the divisibility test passes, 
            #and monkey[-2] contains the monkey that will recieve it if the test fails.
            if(bored):
                data[monkey[-1]][0].append(worry)
            else:
                data[monkey[-2]][0].append(worry)
            
inspected = sorted(inspected, reverse= True)
print(inspected[0] * inspected[1])
################################################PART 2################################################
print("\nPart 2:")

#Here, only a few things changed, so I'll point those changes out directly.

#Reread input since we modified data directly.
with open("Inputs/Day11_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

inspected = [0 for i in data]    

#All the divisibility information is retained if you multiply the divisibilities (which are always prime)
#to each other. This allows our worry calculation to be reigned in and allows for 10000 loops to be simulated.

magic = 1
for monkey in data:
    magic *= monkey[2]

#Simulate 10000 loops
for r in range(10000):
    for monkey in data:

        while(monkey[0] != []):
            item = monkey[0].pop(0)
            inspected[data.index(monkey)] += 1
            op = monkey[1][0]

            if(monkey[1][1] == "old"):
                second = item
            else:
                second = int(monkey[1][1])

            if(op == "*"):
                worry = item * second
            elif(op == "+"):
                worry = item + second
            elif(op == "-"):
                worry = item + second
            
            #Thanks to @puggle for suggesting this route, I never would have thought to do this had I not cheated.
            #I plan not to going forward.
            worry %= magic

            if(worry % monkey[2] != 0):
                bored = True
            else:
                bored = False

            if(bored):
                data[monkey[-1]][0].append(worry)
            else:
                data[monkey[-2]][0].append(worry)
            
inspected = sorted(inspected, reverse= True)
print(inspected[0] * inspected[1])
################################################FAILED ANSWERS:################################################
#PART 1: 
#PART 2: 11302124160 (Too low)