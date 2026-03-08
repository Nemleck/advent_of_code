import math

#get data from input
with open("input.txt") as f:
    lines = f.readlines()

#split every line in two parts
def splitData(line):
    lenLine = math.floor(len(line)/2)
    splitLine = []

    splitLine.append(line[0:(lenLine)])
    splitLine.append(line[lenLine:])

    return splitLine

#check if a character is in two strings
def checkChar(string1, string2):
    chars = [chr(i) for i in range(65, 123)]
    found = []

    for i in chars:
        if (i in string1) and (i in string2):
            found.append(i)
    
    return found

#convert char to number
def charToNum(char):
    unicodePos = ord(char)

    if unicodePos in range(65, 91):
        return unicodePos - 38
    else:
        return unicodePos - 96

total = 0
for line in lines:
    splitLine = splitData(line)
    commonChar = checkChar(splitLine[0], splitLine[1])
    total += sum([charToNum(i) for i in commonChar])

print(total)