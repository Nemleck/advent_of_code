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

def return_glob_i(pos):
    dir_i = 0
    glob_i = 0
    while not pos.endswith("Z"):
        pos = get_next_direction(pos, instructions[dir_i])

        if glob_i % 10000000 == 0:
            print(glob_i)

        dir_i += 1
        glob_i += 1
        if dir_i >= len(instructions):
            dir_i = 0
    
    return glob_i

poss = [elm for elm in directions.keys() if elm.endswith("A")]
solutions = []
for i, pos in enumerate(poss):
    sol = return_glob_i(pos)
    print(sol)
    solutions.append(sol)

print(solutions)

import math
print(math.lcm(*solutions))