from itertools import permutations

def HasAllLetters(InA, InB):
# Does all the letters exist in the combination?
    found = True
    for letterIndex in range(len(InA)):
        letterFound = False
        for cominationLetterIndex in range(len(InB)):
            if InA[letterIndex] == InB[cominationLetterIndex]:
                letterFound = True
        found = found & letterFound   
    return found

def CharToInt(InChar):
    return ord(InChar) - ord('a')

def ExistsIn(InValue, InArray):
    for index, value in enumerate(InArray):
        if value == InValue:
            return index

    return -1

cleanCombinations = ["abcefg","cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

outNumbers = []
currentInput = []
def CouldBeNumber(InScanIndex, InScrambledToClean, depth):
    global outNumbers
    global currentInput
    if InScanIndex == 9:
        return True
    
    cleanString = cleanCombinations[InScanIndex]
    for inputIndex, inputString in enumerate(currentInput):

        # Not same length
        if len(cleanString) != len(inputString):
            continue

        # Iterate the word, Make sure all match

        allPermutations = permutations(inputString)

        for permIndex, permutatedValue in enumerate(allPermutations):
            # print(cleanString + " : " + "".join(permutatedValue) + " @ " + str(depth))
            
            validWord = True
            scrambledToClean = InScrambledToClean.copy()
            for letterIndex, cleanLetter in enumerate(cleanString):

                scambledLetterValue = permutatedValue[letterIndex]
                scambleLetterIndex = CharToInt(scambledLetterValue)

                cleanLetterValue = cleanLetter
                cleanLetterIndex = CharToInt(cleanLetterValue)

                if scrambledToClean[scambleLetterIndex] == -1:
                    # Assume that the wire can go to the clean output
                    scrambledToClean[scambleLetterIndex] = cleanLetterValue
                    # print("Wire: " + str(scambleLetterIndex) + " = " + str(cleanLetterValue))
                else:
                    if scrambledToClean[scambleLetterIndex] != cleanLetterValue:
                        validWord = False
                        # print("Wire: " + str(scambleLetterIndex) + " != " + str(cleanLetterValue))

                        break
                    else:
                        continue
                    
            if not validWord:
                continue
            
            
            # If all numbers are fine with this, return the connections
            if not CouldBeNumber(InScanIndex + 1, scrambledToClean, depth + 1):
                continue
            else:
                if len(outNumbers) == 0:
                    print("Found")
                    outNumbers = scrambledToClean
                return True

    return False




inputFile = open("input.txt", "r")
inputLines = inputFile.readlines()
outputCombinations = []
inputCombinations = []

for index, line in enumerate(inputLines):
    inputOutput = line.split("|")
    # First half of the input
    inputCombinations.append([])
    for valIndex, value, in enumerate(inputOutput[0].split(" ")):
        if value == '|\n':
            continue
        if len(value) == 0:
            continue
        inputCombinations[len(inputCombinations) - 1].append(value.removesuffix("\n"))
        # inputCombinations[len(inputCombinations) - 1].append("".join(sorted(value.removesuffix("\n"))))

    outputCombinations.append([])
    # Output numbers
    for valIndex, value, in enumerate(inputOutput[1].split(" ")):
        if value == '|\n':
            continue
        if len(value) == 0:
            continue
        outputCombinations[len(outputCombinations) - 1].append(value.removesuffix("\n"))
        # outputCombinations[len(outputCombinations) - 1].append("".join(sorted(value.removesuffix("\n"))))

count = 0
for outListIndex, outList in enumerate(outputCombinations):
    currentCount = 0
    
    # print("")
    # print("")
    # print("")
    # print("")
    # print("")

    currentInput = inputCombinations[outListIndex]
    remaningNumbers = [0,1,2,3,4,5,6,7,8,9]
    outNumbers = []
    CouldBeNumber(0, [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], 0)
            



    for i, val in enumerate(outList):
        charArray = []
        for letter, letterVal in enumerate(val):
            charArray.append(outNumbers[CharToInt(letterVal)])

        inputValue = "".join(sorted(charArray))
        # print(inputValue)
        for combinationIndex, combinationValue in enumerate(cleanCombinations):

            if len(combinationValue) != len(inputValue):
                continue

            found = HasAllLetters(combinationValue, inputValue)

            if not found:
                continue

            # print("Match")
            # 0 -> 1, 1->10, 2->100 
            val = combinationIndex * pow(10, 3 - i % 4)
            currentCount += val
            break

    print("value "  + str(currentCount))
    count += currentCount

print("count: " + str(count))
    