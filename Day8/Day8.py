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
        # inputCombinations[len(inputCombinations) - 1].append(value.removesuffix("\n"))
        inputCombinations[len(inputCombinations) - 1].append("".join(sorted(value.removesuffix("\n"))))

    outputCombinations.append([])
    # Output numbers
    for valIndex, value, in enumerate(inputOutput[1].split(" ")):
        if value == '|\n':
            continue
        if len(value) == 0:
            continue
        # outputCombinations[len(outputCombinations) - 1].append(value.removesuffix("\n"))
        outputCombinations[len(outputCombinations) - 1].append("".join(sorted(value.removesuffix("\n"))))

cleanCombinations = ["abcefg","cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
uniqueCombinations = ["","cf","","","bcdf","","","acf","abcdefg",""]

count = 0
for outListIndex, outList in enumerate(outputCombinations):
    currentCount = 0

    #Find scambled connections. we know from part 1 that 1 4 5 7 can be matched.
    # # char -> int -> real char 
    foundConnections = ['0','0','0','0','0','0','0','0','0','0','0']
    ## do an simple pass. for the ones that we know the connections of
    for inputIndex, inputValue in enumerate(inputCombinations[outListIndex]):
        for combinationIndex, combinationValue in enumerate(uniqueCombinations):
            if len(combinationValue) != len(inputValue):
                continue

            print(inputValue + " @" + str(inputIndex) + " clean: " + combinationValue + " @" + str(combinationIndex))

            for letterIndex, letter in enumerate(inputValue):
                connectionIndex = ord(letter) - ord('a')
                foundConnections[connectionIndex] = combinationValue[letterIndex]
                print(letter + " equals " + combinationValue[letterIndex])

            print(foundConnections)

            
            

    # Now that we know most of the connections (abcdfg) missing (e)
    remainingLinks = ['a','b','c','d','e','f','g']
    for index, foundConnection in enumerate(foundConnections):
        if foundConnection == -1:
            continue
        remainingLinks.remove(foundConnection)
    
    foundConnections['e'] = remainingLinks[0]




    # we can connect most of the unknowns. 



    for outIndex, outValue in enumerate(outList):
        print("scanning: " + outValue)
        for combinationIndex, combinationValue in enumerate(combinations):

            if len(combinationValue) != len(outValue):
                continue
            print(outValue + " vs " + combinationValue + " Len match: " + str(combinationIndex))
            # Does all the letters exist in the combination?
            found = True
            for letterIndex in range(len(combinationValue)):
                letterFound = False
                for cominationLetterIndex in range(len(outValue)):
                    if combinationValue[letterIndex] == outValue[cominationLetterIndex]:
                        letterFound = True
                if not letterFound:
                    print("Missing letter: " + str(combinationValue[letterIndex]))
                found = found & letterFound            
            if not found:
                continue
            # 0 -> 1, 1->10, 2->100 
            val = combinationIndex * pow(10, 3 - outIndex % 4)
            print("Full match " + outValue + "  :  " + combinationValue + " -> " + str(val))

            currentCount += val
            break

    print("value "  + str(currentCount))
    count += currentCount

print("count: " + str(count))
    