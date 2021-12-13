from os import startfile


file = open("input.txt", "r")
lines = file.readlines()

caves = []

class Connection:
    Start = ""
    End = ""

allConnections = []

for index, line in enumerate(lines):
    split = line.split("-")
    a = split[0]
    b = split[1]
    b = b.removesuffix("\n")

    if not caves.__contains__(a):
        caves.append(a)

    if not caves.__contains__(b):
        caves.append(b)

    forward = Connection()
    forward.Start = a
    forward.End = b
    allConnections.append(forward)

    backwards = Connection()
    backwards.Start = b
    backwards.End = a
    allConnections.append(backwards)

def IsBigCave(InCave):
    # Never re-visit start
    if InCave == "start":
        return False

    if InCave == "end":
        return False

    big = InCave.isupper()
    return big

def GetConnectionsFrom(InPosition):
    retValues = []
    for index, value in enumerate(allConnections):
        if value.Start == InPosition:
            retValues.append(value)

    return retValues


def PrintPath(InPath):
    for i, point in enumerate(InPath):
        print(point + ",", end= "")
    print("")



allPaths = []
def TryPath(InPosition, InVisited, bInHasDoubleVisited):
    # print("")

    # Get the connections from the currennt position
    # Check if the connections are avail.
    # Try path with them
    # If we dont end up on "end" return false
    # else, add all together
    if InPosition == "end":
        # print("Found:")
        # PrintPath(InVisited)
        allPaths.append(InVisited)
        return

    connections = GetConnectionsFrom(InPosition)
    currentVisited = InVisited.copy()
    currentVisited.append(InPosition)

    # print("Trying:")
    # PrintPath(currentVisited)

    for index, connection in enumerate(connections):
        # Cant visit small caves twice
        
        if InVisited.__contains__(connection.End):
            if connection.End == "start":
                continue
            
            if not IsBigCave(connection.End):
                if bInHasDoubleVisited:
                    continue
                else:
                    TryPath(connection.End, currentVisited, True)
                    continue
        
        TryPath(connection.End, currentVisited, bInHasDoubleVisited)


TryPath("start", [], False)

# for index, path in enumerate(allPaths):
#     print("-----------")
#     PrintPath(path)
print("PathCount: " + str(len(allPaths)))    