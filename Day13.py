#Day 13: Distress Signal
#This one was really ugly, took me ages to get right, and I made it way harder for myself
#than need be because I felt the need to show off my knowledge of higher-order functions and small-step semantics.
#What resulted was me looking like a clown, but learning a lot in the process.

#Our first imports from external libraries! I'll go over what these were used for when they crop up.
import ast
from copy import deepcopy
################################################FUNCTIONS################################################

def parse(data):
    '''
    Parse function used during input on data.
    '''
    parsed = []
    pair = []

    for line in data:
        #Fun fact, I cost myself a few minutes by appending when a delimiter appears. I made the same mistake
        #of not adding the last array, which (turns out) is sorted correctly, so it impacts the answers in both parts.
        if(line != ""):
            #Lord almighty, thank you for this function that exists. I don't know if I would've survived
            #having to write a list parsing function AGAIN. (See my unfinished attempt for Day 18 in 2021)
            #It is cheating a lil bit, but cmon, it's just the input.
            pair.append(ast.literal_eval(line))
        else:
            #Append line to returned data, parsed to a usable format, and reset pair to empty pair.
            parsed.append(pair)
            pair = []

    return parsed

def transverse(data):
    '''
    Returns the transverse of a grid/table.
    '''
    t = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            t[j][i] = data[i][j]
    
    return t

def get_neighbors(data, i, j):
    '''
    Get the neighbors of a grid cell.
    data: the grid itself.
    i: the x coordinate (row index) of the grid
    j: the y coordinate (col index) of the grid
    '''
    n = []
    sides = []
    if(i > 0):
        n.append(data[i-1][j])
        sides.append("U")
    if(i < len(data)-1):
        n.append(data[i+1][j])
        sides.append("D")
    if(j > 0):
        n.append(data[i][j-1])
        sides.append("L")
    if(j < len(data[i]) - 1):
        n.append(data[i][j+1])
        sides.append("R")
    return n, sides

#This is the magic function that uses concepts akin to small-step semantics in PL to solve
#the problem. Honestly made it way harder for myself, even though it makes sense to do that.
#Also messed up my implementation of other parts, and they were way easier ways to do it.
def check_pair(pair):
    #Extract each list in the pair.
    left = pair[0]
    right = pair[1]

    while(True):
        #Base Case 1: 1+ empty lists and their truth values, with both lists being empty representing a inconclusive "?"
        if(left == [] and right == []):
            return "?"
        if(left == []):
            return True
        if(right == []):
            return False
        
        #Base Case 2: Both left and right are ints. Straightforward implementation, with equality representing inconclusive result.
        if(type(left) is int and type(right) is int):
            if(left < right):
                return True
            elif(left == right):
                return "?"
            else:
                return False
        
        #Conversion of one/both arguments to lists, since they might be integers
        if(type(left) is int):
            left = [left]
        if(type(right) is int):
            right = [right]
        
        #Reduction of the list into a check pair between the first element in both arrays.
        #Like small step semantics, we only evaluate if BOTH arguments are primitive ints, if even one of them's a list,
        #We must reduce them further. The pop(0) makes sure to evaluate the rest of the lists. This... was a terrible mistake
        #that led to issues in part 2.
        R = check_pair([left.pop(0), right.pop(0)])

        #If the result wasn't inconclusive, we carry the return up the stack of function calls.
        if(type(R) is bool):
            return R
        
        #If this wasn't the case, we move on to the next elements and repeat the process.

#A quicksort implementation where I decided to be cheeky and try out something new: a higher-order function.
#Do not recommend. At least for this problem. It was unnecessary and led to some problems.
def quicksort(l, compare):
    #Base case of quicksort
    if(len(l) in (0,1)):
        return l

    pivot = l[len(l)//2]
    left = []
    right = []

    #Remove the pivot, as we don't want copies of the pivot in the resulting array.
    l.remove(pivot)

    for i in l:
        #This is where the deepcopy library gets to be used. Turns out simple list slicing only copies one layer deep,
        #and since my check_pair modifies in place, even a shallow copy got utterly destroyed, thus the need to use
        #a copy function that copies deeper than one layer and into lists of lists.
        pc = deepcopy(pivot)
        copy = deepcopy(i)
        
        #We append the unaltered copy to left if it's bigger, resulting in a reversed sort
        if(compare([pc, copy]) == True):
            left.append(i)
        else:
            right.append(i)
        
    
    #Recursive step of quicksort.
    return quicksort(left, compare) + [pivot] + quicksort(right, compare)

################################################PARSING################################################

#Sending raw data to the parser
with open("Inputs/Day13_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Checking the parsing (if necessary):
#print(data[:10])

################################################PART 1################################################
print("Part 1:")

#Total sum of all correctly ordered pairs
total = 0

#Straightforward implementation of problem statement
for pair in range(len(data)):
    r = check_pair(data[pair])
    if(r):
        total += pair + 1

print(total)
################################################PART 2################################################
print("\nPart 2:")

#This part was ROUGH. If you want to see why it's rough, see comments on my quicksort implementation.

#Reread input, since calling the check_pair function augments the data in place.
with open("Inputs/Day13_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

#Gather all pairs to be sorted. The name of the array is confusingly chosen because
#of a misunderstanding of the prompt.
correct_data = []
for i in range(len(data)):
    correct_data.append(data[i][0])
    correct_data.append(data[i][1])
correct_data.append([[2]])
correct_data.append([[6]])

#Get result and reverse it to put them in order from smallest to largest.
result = quicksort(correct_data, check_pair)
result.reverse()

#Calculate problem statment.
print((result.index([[2]]) + 1) * (result.index([[6]]) + 1))
################################################FAILED ANSWERS:################################################
#PART 1: 6622, 6506
#PART 2: 19320