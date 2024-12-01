import re

with open("input.txt", "r") as f:
    data = f.readlines()

instructions = data[0].strip()

directions = {}
pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")

for line in data[2:]:
    match = pattern.match(line)
    if match:
        directions[match.group(1)] = (match.group(2), match.group(3))

def get_next_direction(pos, direction):
    return directions[pos][direction == "R"]

pos = "AAA"
dir_i = 0
glob_i = 0
while pos != "ZZZ":
    pos = get_next_direction(pos, instructions[dir_i])

    dir_i += 1
    glob_i += 1
    if dir_i >= len(instructions):
        dir_i = 0
    
    if glob_i > 100000:
        break

print(glob_i)