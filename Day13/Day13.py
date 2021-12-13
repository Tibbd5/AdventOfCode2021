from os import read
from typing import NoReturn


file = open("input.txt", "r")
lines = file.readlines()

worldSizeX = 0
worldSizeY = 0

pointLines = []
instructions = []

for lineIndex, line in enumerate(lines):
    if line.__contains__("fold"):
        instructions.append(line)
        continue

    if line == "\n":
        continue

    pointLines.append(line)

# find the world size, and create the world grid
for pointIndex, pointLine in enumerate(pointLines):
    points = pointLine.split(",")
    x = int(points[0])
    y = int(points[1])

    if worldSizeX <= x:
        worldSizeX = x + 1
    if worldSizeY <= y:
        worldSizeY = y + 1

world = []
for y in range(worldSizeY):
    world.append([])
    for x in range(worldSizeX):
        world[len(world) - 1].append(0)


def SetWorldValue(InX, InY, InValue):
    if InValue > world[InY][InX]:
        world[InY][InX] = InValue 

def GetWorldValue(InX, InY):
    return world[InY][InX]

# Set the world data
for pointIndex, pointLine in enumerate(pointLines):
    points = pointLine.split(",")
    x = int(points[0])
    y = int(points[1])
    SetWorldValue(int(x), int(y), 1)
    
def PrintWorld():
    print("----------------------")
    for y in range(worldSizeY):
        for x in range(worldSizeX):
            val = GetWorldValue(x,y)
            if val == 0:
                print(str("."), end="")
            else:
                print(str("#"), end="")
        print("")
    print("----------------------")
    

# PrintWorld()
outFile = open("outTest.txt", "w")

for instructionIndex, instructionLine in enumerate(instructions):
    # instructionLine ex: 
    # fold along y=7
    # fold along x=5

    data = instructionLine.split(" ")
    splitData = data[2].split("=")
    axies = splitData[0]
    amount = int(splitData[1])
    print(instructionLine, end="")

    size = 0
    if axies == "y":
        size = worldSizeX
    else:
        size = worldSizeY

    for pos in range(int(size)):
        for index in range(amount ):
                realIndex = (index + 1)
                writePos = amount - realIndex
                readPos = amount + realIndex
                if axies == "y":
                    if readPos < worldSizeY:
                        SetWorldValue(pos, writePos, GetWorldValue(pos, readPos))
                else:
                    if readPos < worldSizeX:
                        SetWorldValue(writePos, pos, GetWorldValue(readPos, pos))
    if axies == "y":
        worldSizeY =  int(worldSizeY / 2)
    else:
        worldSizeX = int(worldSizeX / 2)

    # part 1
    # count = 0
    outFile.seek(0)
    for y in range(int(worldSizeY)):
        for x in range(int(worldSizeX)):
            outFile.write(str(GetWorldValue(x,y)))
        outFile.write("\n")
    outFile.write("\n")
    
    outFile.flush()

    # print(str(count))
    # break
print("")
print(str(worldSizeX))
print(str(worldSizeY))

PrintWorld()