fileInput = open("Input.txt", "r")
inputNumbersStrings = fileInput.read().split(",")

highestValue = 0
inputNubers = []
for index, value in enumerate(inputNumbersStrings):
    inputNubers.append(int(value))
    if highestValue < int(value):
        highestValue = int(value)

numberCount = []
for index in range(highestValue + 1):
    numberCount.append(0)

for index, value in enumerate(inputNubers):
    numberCount[value] += 1

costs = []
costs.append(0)
for index in range(int(highestValue)):
    prevValue = costs[index]
    newValue = prevValue + index + 1
    costs.append(newValue)

def TryNumber(InNumber):
    combinedValue = 0

    for index, value in enumerate(inputNubers):
        distance = abs(value - InNumber)
        combinedValue += costs[distance]

    return combinedValue

lowest = 9999999999
lowestIndex = 0
for index, value in enumerate(inputNubers):
    value = TryNumber(index)
    if value < lowest:
        lowest = value
        lowestIndex = index
        
for index, value in enumerate(inputNubers):
    distance = abs(value - lowestIndex)
    print(str(distance) + " " + str(costs[distance]))

print(str(lowest) + " @" + str(lowestIndex))
