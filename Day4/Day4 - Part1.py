
bingoFile = open("Input.txt", "r")
bingoInput = bingoFile.read().split(",")

boardFile = open("Boards.txt", "r")
boardInput = boardFile.readlines()

print("Input:")
print(bingoInput)
# print(boardInput)

#Remove lines only consisting of \n 
for rowIndex in reversed(range(len(boardInput))):
    if boardInput[rowIndex] == "\n":
        boardInput.remove(boardInput[rowIndex])

# Split into size of boardSize*boardSize
boards = [[]]
boardSize = 5
rows = len(boardInput)
for rowIndex in range(int(rows / boardSize)):
    boards.append([])
    for inputRow in range(boardSize):
        lineString = boardInput[rowIndex * boardSize + inputRow]
        split = lineString.split()
        if len(split) <= 0:
            break

        for valueIndex in range(boardSize):
            boards[rowIndex].append(int(split[valueIndex]))

# last is empty
boards.remove(boards[len(boards) - 1])

def HorizontalFull(board, values):
    for inputRowX in range(boardSize):
        setCount = 0
        for inputRowY in range(boardSize):
            value = board[inputRowX * boardSize + inputRowY]
            if value in values:
                setCount += 1
                print(str(value).zfill(2), end=" ")
            else:
                print("--", end=" ")
                

        if setCount >= boardSize:
            return True
        print("")
        
    return False

def VerticalFull(board, values):
    for inputRowY in range(boardSize):
        setCount = 0
        for inputRowX in range(boardSize):
            value = board[inputRowY + inputRowX * boardSize]
            if value in values:
                setCount += 1
                print(str(value).zfill(2), end=" ")
            else:
                print("--", end=" ")

        if setCount == boardSize:
            return True
        print("")

    return False

winner = -1
scannedValues = []
for index, value in enumerate(bingoInput):
    scannedValues.append(int(value))

    for boardIndex in range(len(boards)):
        print("H:")
        if(HorizontalFull(boards[boardIndex], scannedValues)):
            winner = boardIndex
            break
        print("V:")
        if(VerticalFull(boards[boardIndex], scannedValues)):
            winner = boardIndex
            break

    if winner != -1:
        break

# Array starts @ 0 so +1
print("Board " + str(winner) + " won after: " + str(len(scannedValues)))

combinedValues = 0
for inputRowY in range(boardSize):
    for inputRowX in range(boardSize):
        value = boards[winner][inputRowY * boardSize + inputRowX]
        isNotIn = value in scannedValues
        if not isNotIn:
            combinedValues += value



combinedValues *= scannedValues[len(scannedValues) - 1]
print("Value: " + str(combinedValues))
