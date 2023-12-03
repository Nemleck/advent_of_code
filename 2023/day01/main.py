from time import sleep

with open("input.txt", "r") as f:
    data = f.readlines()

total = 0
for line in data:
    first = None
    last = None

    for letter in line:
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if first == None:
                first = letter
            last = letter
    
    total += int(first+last)
    print(first, last)
    sleep(1)

print(total)