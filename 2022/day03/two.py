import math

#get data from input
with open("input.txt") as f:
    lines = f.readlines()

# data = [
#     ["LHC","RlC","CvC"],
#     ["LVt","HPt","CHt"]
# ]

# data = [
#     "LHC","RlC","CvC",
#     "LVt","HPt","CHt",
#     "LHC","RlC","CvC"
# ]

#split every line in two parts
def splitData(lines):
    data = []
    for l in range(0, len(lines), 3):
        data.append(lines[l:l+3])
    
    return data

# def splitData(lines):
#     i = 0
#     temp = []
#     data = []
#     for line in lines:
#         i += 1
#         if i <= 3:
#             temp.append(line)
#         else:
#             data.append(temp)
#             temp = []
#             i = 0
#     data.append(temp)

#     return data

#check if a character is in two strings
def checkChar(string1, string2, string3):
    chars = [chr(i) for i in range(65, 123)]
    found = []

    for i in chars:
        if (i in string1) and (i in string2) and (i in string3):
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
data = splitData(lines)
for group in data:
    commonChar = checkChar(group[0], group[1], group[2])
    total += sum([charToNum(i) for i in commonChar])

print(total)