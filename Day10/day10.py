inputFile = open("input.txt", "r")
inputLines = inputFile.readlines()

chunkOpeners = ["(", "[", "{", "<"]
chunkClosers = [")", "]", "}", ">"]

def ExistsIn(InValue, InArray):
    for index, value in enumerate(InArray):
        if value == InValue:
            return True
    return False

def GetEquivlant(InCloser):
    if InCloser == '}':
        return '{'

    if InCloser == '>':
        return '<'

    if InCloser == ']':
        return '['

    if InCloser == ')':
        return '('

    return ' '

chunkStack = []
def IsCurrupt(InLine):

    valid = True
    for index, char in enumerate(InLine):
        if ExistsIn(char, chunkOpeners):
            chunkStack.append(char)
            continue

        if ExistsIn(char, chunkClosers):
            if chunkStack[len(chunkStack) - 1] != GetEquivlant(char):
                print("Currupt " + char + " @ " + str(index))
                valid = False
                # return False
            else:
                chunkStack.pop()
    # Part 1, ignore all non currupted

    return valid

scores = []
for index, line in enumerate(inputLines):
    print("index: " + str(index))
    chunkStack = []
    isValid = IsCurrupt(line) 
    if not isValid:
        continue

    print(str(chunkStack))

    count = 0
    for closerIndex, closerValue in enumerate(reversed(chunkStack)):
        count *= 5
        if closerValue == '{':
            count += 3

        if closerValue == '<':
            count += 4

        if closerValue == '[':
            count += 2

        if closerValue == '(':
            count += 1
        # print(str(count))

    scores.append(count)

scores.sort()
print(str(scores[int(len(scores) / 2)]))