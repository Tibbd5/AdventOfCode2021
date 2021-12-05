file = open("Input.txt", "r")
lines = file.readlines()

#01 -> 23, repeating
cleanPoints = []
#Parse into inegers
for index, value in enumerate(lines):
    points = value.split(" -> ")
    lhs = points[0].split(",")
    cleanPoints.append(int(lhs[0]))
    cleanPoints.append(int(lhs[1]))

    rhs = points[1].split(",")
    cleanPoints.append(int(rhs[0]))
    cleanPoints.append(int(rhs[1]))

world = []
worldSize = 1000
#Initialize the world
for positionX in range(worldSize):
    for positionY in range(worldSize):
        world.append(0)

#Iterate over points, generate vector, update world on those points
for pointStartIndex in range(int(len(cleanPoints) / 4)):
    x1 = cleanPoints[pointStartIndex*4]
    y1 = cleanPoints[pointStartIndex*4 + 1]
    x2 = cleanPoints[pointStartIndex*4 + 2]
    y2 = cleanPoints[pointStartIndex*4 + 3]

## Direction & Speed axies
    xLen = abs(x2 - x1)
    yLen = abs(y2 - y1)
    len = 0
    ySpeed = (y2 - y1)
    xSpeed = (x2 - x1)

    if (xLen > yLen):
        len = xLen
        xSpeed /= xLen
        ySpeed /= xLen
    else:
        len = yLen
        xSpeed /= yLen
        ySpeed /= yLen

    currentX = x1
    currentY = y1
    for moveIndex in range(len + 1):
        flooredValueX = int(currentX)
        flooredValueY = int(currentY)
        world[flooredValueX * worldSize + flooredValueY] += 1

        currentX += xSpeed
        currentY += ySpeed

        
## Calculate intersections
count = 0
for positionX in range(worldSize):
    for positionY in range(worldSize):
        value = world[positionY * worldSize + positionX]
        if value > 1:
            count += 1
        
    #     if value > 0:
    #         print(str(value), end="")
    #     else:
    #         print(".", end="")
    # print("")

print(str(count))

    