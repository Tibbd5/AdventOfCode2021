from os import terminal_size


inputFile = open("input.txt", "r")
inputLines = inputFile.readlines()

worldSizeY = len(inputLines)
worldSizeX = len(inputLines[0]) - 1 # -1 due to \n

# Y X
grid = []
for lineI, line in enumerate(inputLines):
    grid.append(int(line))

def GetIndexOf(InX, InY):
    return InY * worldSizeY + InX

def GetYFromIndex(InIndex):
    return int(InIndex / worldSizeY)

def GetXFromIndex(InIndex):
    return InIndex - GetYFromIndex(InIndex) * worldSizeY

def GetValueAt(InX, InY):
    if InX < 0:
        return 10
    if InX >= worldSizeX:
        return 10
    if InY < 0:
        return 10
    if InY >= worldSizeY:
        return 10

    return int(str(grid[InY])[InX])

def LowerThanOthers(InX, InY):
    center = GetValueAt(InX, InY)
    above = GetValueAt(InX, InY - 1)
    if above <= center:
        return False
    below = GetValueAt(InX, InY + 1)
    if below <= center:
        return False
    left = GetValueAt(InX - 1, InY)
    if left <= center:
        return False
    right = GetValueAt(InX + 1, InY)
    if right <= center:
        return False

    return True

isIndexScanned = []
for x in range(worldSizeX):
    for y in range(worldSizeY):
        isIndexScanned.append(0)

def HasScanned(InIndex):
    return isIndexScanned[InIndex]

def BreadthFirstScan(InX, InY):
    positionIndex = GetIndexOf(InX, InY)
    center = GetValueAt(InX, InY)

    if HasScanned(positionIndex):
        return 0
    if center >= 9:
        return 0

    indexesToScan = []
    indexesToScan.append(positionIndex)
    scanCount = 0

    while len(indexesToScan) != 0:
        currentIndex = indexesToScan[0]
        indexesToScan.remove(currentIndex)

        if HasScanned(currentIndex):
            continue

        isIndexScanned[currentIndex] = 1

        scanCount += 1

        xPos = GetXFromIndex(currentIndex)
        yPos = GetYFromIndex(currentIndex)

        above = GetValueAt(xPos, yPos - 1)
        if above < 9:
            indexesToScan.append(GetIndexOf(xPos, yPos - 1))

        below = GetValueAt(xPos, yPos + 1)
        if below < 9:
            indexesToScan.append(GetIndexOf(xPos, yPos + 1))

        left = GetValueAt(xPos - 1, yPos)
        if left < 9:
            indexesToScan.append(GetIndexOf(xPos - 1, yPos))

        right = GetValueAt(xPos + 1, yPos)
        if right < 9:
            indexesToScan.append(GetIndexOf(xPos + 1, yPos))

    if scanCount > 1:
        print("Size: " + str(scanCount))
    return scanCount

sum = 0
basinSizes = []
for indexY in range(len(grid)):
    for indexX in range(len(str(grid[indexY]))):
        size = BreadthFirstScan(indexX, indexY)
        if size > 1:
            basinSizes.append(size)

basinSizes.sort()


print("totoal: " + str(sum))