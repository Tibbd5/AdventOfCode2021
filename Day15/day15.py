file = open("input.txt", "r")
lines = file.readlines()

worldSizeY = len(lines)
worldSizeX = len(lines[0]) - 1

class Node:
    XPos = 0
    YPos = 0
    Index = 0
    ParentRisk = 0
    ParentIndex = -1
    RiskValue = -1
    bClosed = False

nodes = []

def GetIndexOf(InX, InY):
    return InY * worldSizeX + InX

# for y in range(worldSizeY):
#     nodes.append([])
#     for x in range(worldSizeX):
#         node = Node()
#         node.Index = GetIndexOf(x,y)
#         node.RiskValue = int(lines[y][x])
#         node.XPos = x
#         node.YPos = y
#         nodes[y].append(node)


def GetNodeOfPos(InX, InY):
    return nodes[InY][InX]

# Make the world 5x larger

for yMul in range(5):
    for y in range(worldSizeY):
        nodes.append([])
        for xMul in range(5):
            for x in range(worldSizeX):
                node = Node()
                baseRisk = int(lines[y][x])
                node.RiskValue = (baseRisk + xMul + yMul - 1) % 9 + 1
                node.XPos = x + xMul * worldSizeX
                node.YPos = y + yMul * worldSizeY
                node.Index = node.YPos * worldSizeX * 5 + node.XPos

                nodes[y + yMul * worldSizeY].append(node)

worldSizeY *= 5
worldSizeX *= 5
openNodeIndexes = [ 0 ] 

def GetNodeOf(InIndex):
    yPos = int(InIndex / worldSizeX)
    xPos = InIndex - yPos * worldSizeX
    return nodes[yPos][xPos]

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

def GetTotalRiskOfNode(InNode):
    return -(InNode.ParentRisk + InNode.RiskValue)

def GetTotalRiskOf(InIndex):
    return GetTotalRiskOfNode(GetNodeOf(InIndex))

def PrintNodePath(InNode):

    finalPathIndexes = []
    currentIndex = InNode.Index
    while True:
        finalPathIndexes.append(currentIndex)
        currentNode = GetNodeOf(currentIndex)
        if currentNode.ParentIndex != -1:
            currentIndex = currentNode.ParentIndex
        else:
            break
        
    print("----")
    print("Path")
    for y in range(worldSizeY):
        for x in range(worldSizeX):
            node = GetNodeOfPos(x,y)
            direction = ""
            if node.ParentIndex == -1:
                direction = "*"
            else:
                if abs(node.ParentIndex - node.Index) > worldSizeX - 1:
                    direction = "|"
                else:
                    direction = "-"

            # string = direction #+ " " + str(node.RiskValue) # + " " + str(node.ParentRisk + node.RiskValue)+ " " + str(node.Distance) + " " + str(int(GetTotalRiskOf(node.Index) + 1))
            string = str(node.RiskValue)#+ " " + str(node.Distance) + " " + str(int(GetTotalRiskOf(node.Index) + 1))

            if finalPathIndexes.__contains__(GetIndexOf(x,y)):
                print('\033[38;5;' + str(15 + node.RiskValue * 2) + "m" + str(string) + color.END, end="")
            else:
                print('\033[38;5;' + str(231 + node.RiskValue * 2) + "m" + str(string) + color.END, end="")
        print("")
    


def TryAddPosition(InX, InY, InParentNode):
    if InX < 0:
        return
    if InY < 0:
        return
    if InX >= worldSizeX:
        return
    if InY >= worldSizeY:
        return

    node = GetNodeOfPos(InX, InY)
    if node.Index == 0:
        return

    if not node.bClosed:
        openNodeIndexes.append(node.Index)

    if node.ParentIndex == -1:
        node.ParentRisk = InParentNode.ParentRisk + InParentNode.RiskValue
        node.ParentIndex = InParentNode.Index
    else:
        # We have not evaluated the node previusly, so add it to the 
        if (InParentNode.ParentRisk + InParentNode.RiskValue) <= node.ParentRisk :
            node.ParentRisk = InParentNode.ParentRisk + InParentNode.RiskValue
            node.ParentIndex = InParentNode.Index

    
stepCount = 0
while len(openNodeIndexes) > 0:
    ## Get the lowest risk node in the open list
    # Sort based on total risk, evaluate least first
    # openNodeIndexes.sort(key=GetTotalRiskOf)
    currentNodeIndex = openNodeIndexes.pop(0)
    currentNode = GetNodeOf(currentNodeIndex)

    # Make shure that we dont doubble scan
    if currentNode.bClosed:
        continue
    stepCount += 1

    currentNode.bClosed = True
    # add it to the closed list
    
    x = currentNode.XPos
    y = currentNode.YPos

    if stepCount % 1000 == 0:
    #     PrintNodePath(currentNode)
        print(str(stepCount))

    # If we have reached the end, break
    if currentNode.XPos == worldSizeX - 1:
        if currentNode.YPos == worldSizeY - 1:
            break

    # try all positions
    TryAddPosition(x + 1, y, currentNode)
    TryAddPosition(x - 1, y, currentNode)

    TryAddPosition(x, y + 1, currentNode)
    TryAddPosition(x, y - 1, currentNode)

# PrintNodePath(currentNode)

print(str(abs(currentNode.ParentRisk + currentNode.RiskValue) - nodes[0][0].RiskValue))
print("In " + str(stepCount) + " steps")