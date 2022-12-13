#Day 13: Distress Signal

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
        #Append line to returned data, parsed to a usable format.
        if(line != ""):
            pair.append(ast.literal_eval(line))
        else:
            #Append line to returned data, parsed to a usable format.
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

def check_pair(pair):
    left = pair[0]
    right = pair[1]

    while(True):
        if(left == [] and right == []):
            return "?"
        if(left == []):
            return True
        if(right == []):
            return False
        
        if(type(left) is int and type(right) is int):
            if(left < right):
                return True
            elif(left == right):
                return "?"
            else:
                return False
        
        if(type(left) is int):
            left = [left]
        if(type(right) is int):
            right = [right]
        
        R = check_pair([left.pop(0), right.pop(0)])

        if(type(R) is bool):
            return R

def quicksort(l, compare):
    if(len(l) in (0,1)):
        return l

    pivot = l[len(l)//2]
    left = []
    right = []

    l.remove(pivot)

    for i in l:
        pc = deepcopy(pivot)
        copy = deepcopy(i)
        #print(i)
        if(compare([pc, copy]) == True):
            left.append(i)
        else:
            right.append(i)
        #cprint(i)
    
    #print(left, pivot, right)
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

total = 0
correct = []

for pair in range(len(data)):
    r = check_pair(data[pair])
    #print(r,pair+1,"\n")
    if(r):
        correct.append(pair)
        total += pair + 1

print(total)
################################################PART 2################################################
print("\nPart 2:")

with open("Inputs/Day13_input.txt","r") as f:
    raw = f.read().split("\n")
    data = parse(raw)

correct_data = []

for i in range(len(data)):
    correct_data.append(data[i][0])
    correct_data.append(data[i][1])
correct_data.append([[2]])
correct_data.append([[6]])

result = quicksort(correct_data, check_pair)
result.reverse()
print((result.index([[2]]) + 1) * (result.index([[6]]) + 1))
################################################FAILED ANSWERS:################################################
#PART 1: 6622, 6506
#PART 2: 19320