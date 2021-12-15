file = open("input.txt", "r")
lines = file.readlines()

worldSizeY = len(lines)
worldSizeX = len(lines[0]) - 1

def GetIndexOf(InX, InY):
    return InY * worldSizeX + InX

nodes = []

def GetNodeOfPos(InX, InY):
    return nodes[InY][InX]

def GetNodeOf(InIndex):
    yPos = int(InIndex / worldSizeX)
    xPos = InIndex - yPos * worldSizeX
    return nodes[yPos][xPos]

class Node:
    XPos = 0
    YPos = 0
    Index = 0
    ParentRisk = 0
    ParentIndex = -1
    Distance = 1
    RiskValue = -1

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
    endDiffX = worldSizeX - node.XPos
    endDiffY = worldSizeY - node.YPos
    diff = endDiffX*endDiffX + endDiffY*endDiffY
    return -(InNode.ParentRisk + InNode.RiskValue)
    # return -(node.TotalRisk * 2 + node.Distance + diff / (worldSizeX * worldSizeX))

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

            string = direction #+ " " + str(node.RiskValue) # + " " + str(node.ParentRisk + node.RiskValue)+ " " + str(node.Distance) + " " + str(int(GetTotalRiskOf(node.Index) + 1))
            # if finalPathIndexes.__contains__(GetIndexOf(x,y)):
            print('\033[38;5;' + str(233 + node.RiskValue) + "m" + str(string) + color.END, end="")
            # else:
            #     print('\033[38;5;' + str(233 + node.RiskValue) + "m" + str(node.RiskValue) + color.END, end="")
        print("")
    
for y in range(worldSizeY):
    nodes.append([])
    for x in range(worldSizeX):
        node = Node()
        node.Index = GetIndexOf(x,y)
        node.RiskValue = int(lines[y][x])
        node.XPos = x
        node.YPos = y
        nodes[y].append(node)

openNodeIndexes = [ 0 ] 
closedIndexes = []

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

    if not closedIndexes.__contains__(GetIndexOf(InX, InY)):
        openNodeIndexes.append(node.Index)

    totalParentRisk = abs(GetTotalRiskOfNode(InParentNode))

    if node.ParentIndex == -1:
        node.ParentRisk = totalParentRisk
        node.ParentIndex = InParentNode.Index
        node.Distance = InParentNode.Distance + 1
        # print("Set value of " + str(node.XPos) + " " + str(node.YPos))
    else:
        # We have not evaluated the node previusly, so add it to the 
        if (totalParentRisk + node.RiskValue) < GetTotalRiskOfNode(node):
            node.ParentRisk = totalParentRisk
            node.ParentIndex = InParentNode.Index
            node.Distance = InParentNode.Distance + 1


    

while len(openNodeIndexes) > 0:
    # Sort based on total risk, evaluate least first
    openNodeIndexes.sort(key=GetTotalRiskOf)
    # for i ,index in enumerate(openNodeIndexes):
    #     print("SortedValues " + str(GetTotalRiskOf(index)))
## TODO: Validate that this is sorts right direction
    currentNodeIndex = openNodeIndexes.pop()
    if closedIndexes.__contains__(currentNodeIndex):
        continue

    currentNode = GetNodeOf(currentNodeIndex)
    # PrintNodePath(currentNode)

    closedIndexes.append(GetIndexOf(currentNode.XPos, currentNode.YPos))
    # print("Lowest risk: " + str(currentNode.RiskValue) + " Total: " + str(GetTotalRiskOf(currentNode.Index)))
    x = currentNode.XPos
    y = currentNode.YPos

    if currentNode.XPos == worldSizeX - 1:
        if currentNode.YPos == worldSizeY - 1:
            break

    TryAddPosition(x + 1, y, currentNode)
    TryAddPosition(x - 1, y, currentNode)

    TryAddPosition(x, y + 1, currentNode)
    TryAddPosition(x, y - 1, currentNode)

PrintNodePath(currentNode)

print("Donw")