from time import sleep

with open("input.txt", "r") as f:
    data = f.readlines()

conversion = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0
for line in data:
    first = None
    last = None

    treatment = ""
    for letter in line:
        treatment += letter
        if treatment[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if first == None:
                first = letter
            last = letter
        else:
            for key in list(conversion.keys()):
                if treatment.endswith(key):
                    if first == None:
                        first = key
                    last = key

    try:
        int(first)
    except:
        first = conversion[first]
    
    try:
        int(last)
    except:
        last = conversion[last]
    
    total += int(first+last)
    print(int(first+last))

print(total)