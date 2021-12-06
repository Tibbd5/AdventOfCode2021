inputFile = open("Day6/input.txt", "r")
inputFish = inputFile.read()
splitInput = inputFish.split(",")
inputList = []

for index, value in enumerate(splitInput):
    inputList.append(int(value))


timeToSimulate = 256
maxLife = 6
addedFishLife = 8

totalFish = len(inputList)
growPoints = [0,0,0,0,0,0,0,0,0,0]

for index in range(len(inputList)):
    growPoints[inputList[index]] += 1


for day in range(timeToSimulate):

    amountToAdd = growPoints[0]
    totalFish += amountToAdd
    print("Day " + str(day) + " adds: " + str(growPoints[0]) + " amount: " + str(totalFish))

# move day count
    for index in range(len(growPoints) - 1):
        growPoints[index] =  growPoints[index + 1]

    growPoints[addedFishLife] += amountToAdd
    growPoints[maxLife] += amountToAdd
print("num: " + str(totalFish))