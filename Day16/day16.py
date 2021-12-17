# fileInput = open("Input.txt", "r")
# inputHex = fileInput.read()
# inputHex.replace("\n", "")
inputHex = "005410C99A9802DA00B43887138F72F4F652CC0159FE05E802B3A572DBBE5AA5F56F6B6A4600FCCAACEA9CE0E1002013A55389B064C0269813952F983595234002DA394615002A47E06C0125CF7B74FE00E6FC470D4C0129260B005E73FCDFC3A5B77BF2FB4E0009C27ECEF293824CC76902B3004F8017A999EC22770412BE2A1004E3DCDFA146D00020670B9C0129A8D79BB7E88926BA401BAD004892BBDEF20D253BE70C53CA5399AB648EBBAAF0BD402B95349201938264C7699C5A0592AF8001E3C09972A949AD4AE2CB3230AC37FC919801F2A7A402978002150E60BC6700043A23C618E20008644782F10C80262F005679A679BE733C3F3005BC01496F60865B39AF8A2478A04017DCBEAB32FA0055E6286D31430300AE7C7E79AE55324CA679F9002239992BC689A8D6FE084012AE73BDFE39EBF186738B33BD9FA91B14CB7785EC01CE4DCE1AE2DCFD7D23098A98411973E30052C012978F7DD089689ACD4A7A80CCEFEB9EC56880485951DB00400010D8A30CA1500021B0D625450700227A30A774B2600ACD56F981E580272AA3319ACC04C015C00AFA4616C63D4DFF289319A9DC401008650927B2232F70784AE0124D65A25FD3A34CC61A6449246986E300425AF873A00CD4401C8A90D60E8803D08A0DC673005E692B000DA85B268E4021D4E41C6802E49AB57D1ED1166AD5F47B4433005F401496867C2B3E7112C0050C20043A17C208B240087425871180C01985D07A22980273247801988803B08A2DC191006A2141289640133E80212C3D2C3F377B09900A53E00900021109623425100723DC6884D3B7CFE1D2C6036D180D053002880BC530025C00F700308096110021C00C001E44C00F001955805A62013D0400B400ED500307400949C00F92972B6BC3F47A96D21C5730047003770004323E44F8B80008441C8F51366F38F240"

def HexadecimalToBinary(InHex):
    if InHex == '0': return "0000"
    if InHex == '1': return "0001"
    if InHex == '2': return "0010"
    if InHex == '3': return "0011"
    if InHex == '4': return "0100"
    if InHex == '5': return "0101"
    if InHex == '6': return "0110"
    if InHex == '7': return "0111"
    if InHex == '8': return "1000"
    if InHex == '9': return "1001"
    if InHex == 'A': return "1010"
    if InHex == 'B': return "1011"
    if InHex == 'C': return "1100"
    if InHex == 'D': return "1101"
    if InHex == 'E': return "1110"
    if InHex == 'F': return "1111"

def BinaryToHexadecimal(InBinary):
    if InBinary == "0000": return '0'
    if InBinary == "0001": return '1'
    if InBinary == "0010": return '2'
    if InBinary == "0011": return '3'
    if InBinary == "0100": return '4'
    if InBinary == "0101": return '5'
    if InBinary == "0110": return '6'
    if InBinary == "0111": return '7'
    if InBinary == "1000": return '8'
    if InBinary == "1001": return '9'
    if InBinary == "1010": return 'A'
    if InBinary == "1011": return 'B'
    if InBinary == "1100": return 'C'
    if InBinary == "1101": return 'D'
    if InBinary == "1110": return 'E'
    if InBinary == "1111": return 'F'

def BinaryToNumberControlled(InBinaryString, InStart, InEnd):
    value = 0
    debugString = ""
    for index in range(InEnd - InStart):
        realIndex = InStart + index
        mulValue = pow(2, (InEnd - InStart) - index - 1)
        binaryValue = int(InBinaryString[realIndex])
        debugString += InBinaryString[realIndex]
        value += binaryValue * mulValue

    print("Binary test was: " + debugString + " Res: " + str(value))
    return value



def BinaryToNumber(InBinaryString):
    return BinaryToNumberControlled(InBinaryString, 0, len(InBinaryString))

def GetPacketValueFrom(InBinaryString, InPosition):
    completeBinaryString = ""
    currentBinaryPosition = InPosition

    while True:
        shouldContinue = BinaryToNumberControlled(InBinaryString, currentBinaryPosition, currentBinaryPosition + 1)
        currentBinaryPosition += 1

        for i in range(4):
            index = i + currentBinaryPosition
            completeBinaryString += InBinaryString[index]
        currentBinaryPosition += 4
        
        if not shouldContinue == 1:
            break
        
    value = BinaryToNumber(completeBinaryString)
    print("Packet size was: " + str(len(completeBinaryString)) + " value was: " + str(value))
    return value, currentBinaryPosition - InPosition

binaryInput = ""
for index, hexValue in enumerate(inputHex):
    binaryInput = binaryInput + HexadecimalToBinary(hexValue)


print(binaryInput)

class Packet:
    Version = -1
    PacketType = -1
    LengthType = -1

    StartPosition = -1
    EndPosition = -1

    Value = -1
    Remaning = -1

    SubPackets = []
    ParentPacketID = -1


versionSum = 0
currentBinaryPosition = 0
packets = [ Packet()]
currentPacketID = 0
inputLen = len(binaryInput)
while currentPacketID !=-1:
    
    currentPacket = packets[currentPacketID]

    # print("")
    # print("-----")
    # print("")

    # Load header only if current entry isnt initialized
    if currentPacket.Version == -1:
        currentPacket.StartPosition = currentBinaryPosition
        currentPacket.SubPackets = []
        currentPacket.Version = BinaryToNumberControlled(binaryInput, currentBinaryPosition,currentBinaryPosition + 3)
        currentBinaryPosition += 3
        # print("Version: " + str(currentPacket.Version))
        versionSum += currentPacket.Version

        currentPacket.PacketType = BinaryToNumberControlled(binaryInput, currentBinaryPosition , currentBinaryPosition +3)
        currentBinaryPosition += 3
        # print("Packet type: " + str(currentPacket.PacketType))

        if currentPacket.PacketType != 4:

            currentPacket.LengthType = BinaryToNumberControlled(binaryInput, currentBinaryPosition , currentBinaryPosition + 1)
            currentBinaryPosition += 1
            print("Length type: " + str(currentPacket.LengthType ))

            # Read 15 bits, this is the length of the packets.
            # Assumption: each packet is 11, untill the remaning bits is less than 22, where the last packet fills the remaning
            if currentPacket.LengthType == 0:
                lengthOfPackets = BinaryToNumberControlled(binaryInput, currentBinaryPosition,  currentBinaryPosition + 15)
                currentBinaryPosition += 15

                currentPacket.Remaning = lengthOfPackets

            else:
                # next 11 bytes are the amount of packages
                amountOfPackages = BinaryToNumberControlled(binaryInput, currentBinaryPosition,  currentBinaryPosition + 11)
                currentBinaryPosition += 11

                currentPacket.Remaning = amountOfPackages    

        elif currentPacket.PacketType == 4:
            value, readAmount = GetPacketValueFrom(binaryInput, currentBinaryPosition)
            currentBinaryPosition += readAmount
            currentPacket.Value = value
            # print("Value: " + str(value))

            currentPacket.EndPosition = currentBinaryPosition
            # close the packet
            currentPacketID = currentPacket.ParentPacketID
            # restart loop
            continue
    else:
        # will only reach this point if it is a operator aka type != 4
        shouldExit = False
        # check exit condition
        if currentPacket.LengthType == 1:
            # we have created X sub packets
            shouldExit = len(currentPacket.SubPackets) >= currentPacket.Remaning
        
        elif currentPacket.LengthType == 0:
            firstSubPacket = packets[currentPacketID + 1]
            lastPackage = packets[currentPacket.SubPackets[len(currentPacket.SubPackets) - 1]]
            
            shouldExit = lastPackage.EndPosition - firstSubPacket.StartPosition >= currentPacket.Remaning

        if shouldExit:
            # sum
            if currentPacket.PacketType == 0:
                sum = 0
                for i, packetID in enumerate(currentPacket.SubPackets):
                    sum += packets[packetID].Value
                currentPacket.Value = sum

            # product
            elif currentPacket.PacketType == 1:
                sum = packets[currentPacket.SubPackets[0]].Value
                for i, packetID in enumerate(currentPacket.SubPackets):
                    if i <= 0:
                        continue
                    sum *= packets[packetID].Value
                currentPacket.Value = sum

            # Minimum
            elif currentPacket.PacketType == 2:
                minimum = packets[currentPacket.SubPackets[0]].Value
                for i, packetID in enumerate(currentPacket.SubPackets):
                    minimum = min([packets[packetID].Value, minimum])
                currentPacket.Value = int(minimum)

            # Maximum
            elif currentPacket.PacketType == 3:
                maximum = packets[currentPacket.SubPackets[0]].Value
                for i, packetID in enumerate(currentPacket.SubPackets):
                    maximum = max([packets[packetID].Value, maximum])
                currentPacket.Value = int(maximum)

            # Greater
            elif currentPacket.PacketType == 5:
                # garanteed
                a = packets[currentPacket.SubPackets[0]].Value
                b = packets[currentPacket.SubPackets[1]].Value
                currentPacket.Value = int(a > b)

            # Lesser
            elif currentPacket.PacketType == 6:
                # garanteed
                a = packets[currentPacket.SubPackets[0]].Value
                b = packets[currentPacket.SubPackets[1]].Value
                currentPacket.Value = int(a < b)

            # Equals
            elif currentPacket.PacketType == 7:
                # garanteed
                a = packets[currentPacket.SubPackets[0]].Value
                b = packets[currentPacket.SubPackets[1]].Value
                currentPacket.Value = int(a == b)


            currentPacketID = currentPacket.ParentPacketID
            currentPacket.EndPosition = currentBinaryPosition
            continue
        
    # The following data is a subpacket, so create one.
    newPacket = Packet()
    newPacket.ParentPacketID = currentPacketID
    packets.append(newPacket)
    currentPacket.SubPackets.append(len(packets) - 1)
    currentPacketID = len(packets) - 1

    # continue reading packet data.    
print("Val: " + str(packets[0].Value))