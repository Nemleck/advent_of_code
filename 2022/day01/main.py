with open("input.txt", "r") as f:
    data = f.read().splitlines()

temp: int = 0
calories = []
for line in data:
    if line != "":
        temp += int(line)
    else:
        calories.append(temp)
        temp = 0
        continue

calories.sort()
print(calories[-1])