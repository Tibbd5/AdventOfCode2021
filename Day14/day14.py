file = open("input.txt", "r")
lines = file.readlines()

startingTemplate = ""

class Instruction:
    Letters = ""
    Insert = ""

instructions = []

def GetIndexOf(InPair):
    count = 0
    for i, char in enumerate(InPair):
        count += (ord(char) - ord('A')) * pow(26, i + 1)
    return count  

for index, line in enumerate(lines):
    if len(line) < 2:
        continue

    if index == 0:
        startingTemplate = line.removesuffix("\n")
        continue


    inst = Instruction()
    inst.Letters = line.split(" ")[0]
    inst.Insert = line.split(" ")[2].removesuffix("\n")

    instructions.append(inst)

#Generate list of posible pairs
combinationToLetter = {}
combinations = {}
for i, instruction in enumerate(instructions):
    a = "".join([instruction.Letters[0], instruction.Insert])
    b = "".join([instruction.Insert, instruction.Letters[1]])

    combinations[GetIndexOf( instruction.Letters )] = [GetIndexOf(a), GetIndexOf(b)]

    combinationToLetter[GetIndexOf( instruction.Letters )] = instruction.Letters
    combinationToLetter[GetIndexOf( a )] = a
    combinationToLetter[GetIndexOf( b )] = b


templateIndexes = {}
for index, combination in enumerate(combinations):
    templateIndexes[combination] = 0

#Convert template to generic integer
for charIndex in range(int(len(startingTemplate) - 1)):
    pair = "".join([startingTemplate[charIndex ], startingTemplate[charIndex + 1]]) 
    templateIndexes[GetIndexOf(pair)] += 1

for day in range(40):
    newValues = {}
    for index, combination in enumerate(combinations):
        newValues[combination] = 0

    for index, val in enumerate(templateIndexes):
        for i, resultingValues in enumerate(combinations[val]):
            newValues[resultingValues] += templateIndexes[val]

    templateIndexes = newValues
    print(str(day))


characterOccurence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for index, debVal in enumerate(templateIndexes):
    occuranceCount = templateIndexes[debVal]
    
    characterOccurence[ord(combinationToLetter[debVal][0]) - ord('A')] += occuranceCount
    # if debI == len(newValues) - 1:
    #     characterOccurence[ord(combinationToLetter[debVal][1]) - ord('A')] += occuranceCount
smallest = 99999999999989
biggest = 0
for index, val in enumerate(characterOccurence):
    if val > 0:
        if val < smallest:
            smallest = val

    if val > biggest:
        biggest = val


print(str(biggest - smallest))