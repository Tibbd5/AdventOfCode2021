file = open("input.txt", "r")
rawLines = file.readlines()

worldSizeX = len(rawLines[0]) - 1 # remove \n
worldSizeY = len(rawLines)

values = []

for yPos in range(worldSizeY):
    values.append([])
    for xPos in range(worldSizeX):
        values[len(values) - 1].append(int(rawLines[yPos][xPos]))

# Functions start
def GetIndexOf(InX, InY):
    return worldSizeY * InY + InX

def GetYOfIndex(InIndex):
    return int(InIndex / worldSizeY)

def GetXOfIndex(InIndex):
    return InIndex - GetYOfIndex(InIndex) * worldSizeY

def GetValueOf(InX, InY):
    return values[InY][InX]

def SetValueOf(InX, InY, InValue):
    values[InY][InX] = InValue

def GetValueOfIndex(InIndex):
    y = GetYOfIndex(InIndex)
    x = GetXOfIndex(InIndex)
    return GetValueOf(x,y)

def SetValueOfIndex(InIndex, InValue):
    y = GetYOfIndex(InIndex)
    x = GetXOfIndex(InIndex)
    return SetValueOf(x,y, InValue)

def TryIncrementValueOfIndex(InX, InY):
    if InX < 0:
        return 0
    if InX >= worldSizeX:
        return 0

    if InY < 0:
        return 0
    if InY >= worldSizeY:
        return 0

    value = GetValueOf(InX, InY) + 1
    SetValueOf(InX, InY, value)
    return value

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def ExistsIn(InVal, InAray):
    for index, value in enumerate(InAray):
        if InVal == value:
            return True

    return False

def PrintValues(InFlases):
    for yPos in range(worldSizeY):
        for xPos in range(worldSizeX):
            value = GetValueOf(xPos, yPos)
            if value >= 10:
                value = 9
            if not ExistsIn(GetIndexOf(xPos, yPos), InFlases):
                print(str(value).zfill(1), end="")
            else:
                print(color.BOLD + str(value).zfill(1) + color.END, end="")

        print()
# Functions end

flashCount = 0
# Simulate 100 days
for simulationDay in range(9999):
    # 1. Find all steps that will flash
    indexesToFlash = []
    for yPos in range(worldSizeY):
        for xPos in range(worldSizeX):
            posValue = GetValueOf(xPos, yPos) + 1
            SetValueOf(xPos, yPos, posValue)
            # We want all values that are 8 to start with
            if posValue > 9:
                indexesToFlash.append(GetIndexOf(xPos, yPos))


    # 2. Once we know the base indecies, we will add all of the values to the adjaisent, & look for if we added to much to it
    totalScanned = []
    additionalIndecies = indexesToFlash.copy()
    while len(additionalIndecies) > 0:

        index = additionalIndecies[0]
        additionalIndecies.pop(0)
        if ExistsIn(index, totalScanned):
            continue

        totalScanned.append(index)

        x = GetXOfIndex(index)
        y = GetYOfIndex(index)

        if x < 0:
            continue
        if x >= worldSizeX:
            continue
        if y < 0: 
            continue
        if y >= worldSizeY:
            continue

# Diagonals
        # Up left
        if TryIncrementValueOfIndex(x - 1, y + 1) > 9:
            additionalIndecies.append(GetIndexOf(x - 1,y + 1))

        # Up right
        if TryIncrementValueOfIndex(x + 1, y + 1) > 9:
            additionalIndecies.append(GetIndexOf(x + 1,y + 1))

        # Down left
        if TryIncrementValueOfIndex(x - 1, y - 1) > 9:
            additionalIndecies.append(GetIndexOf(x - 1,y - 1))

        # Down right
        if TryIncrementValueOfIndex(x + 1, y - 1) > 9:
            additionalIndecies.append(GetIndexOf(x + 1,y - 1))

# Straights
        # Up 
        if TryIncrementValueOfIndex(x , y + 1) > 9:
            additionalIndecies.append(GetIndexOf(x,y + 1))

        # Down 
        if TryIncrementValueOfIndex(x , y - 1) > 9:
            additionalIndecies.append(GetIndexOf(x,y - 1))

        # Left
        if TryIncrementValueOfIndex(x - 1, y) > 9:
            additionalIndecies.append(GetIndexOf(x - 1,y))

        # Right
        if TryIncrementValueOfIndex(x + 1, y) > 9:
            additionalIndecies.append(GetIndexOf(x + 1,y))


    for i,val in enumerate(indexesToFlash):
        if not ExistsIn(val, totalScanned):
            totalScanned.append(val)

    # With All values found, reset them to 0
    for i, index in enumerate(totalScanned):
        SetValueOfIndex(index, 0)

    allFlashes = True
    for yPos in range(worldSizeY):
        if not allFlashes:
            break
        
        for xPos in range(worldSizeX):
            posValue = GetValueOf(xPos, yPos)
            if posValue != 0:
                allFlashes = False
                break

    if allFlashes:
        PrintValues(totalScanned)
        print("All flashed on day: " + str(simulationDay + 1))
        break

    flashes = len(totalScanned)
    flashCount += flashes
    print("Flashes of day(+1): " + str(simulationDay + 1) + " Was: " + str(flashes))

print("Total: " + str(flashCount))