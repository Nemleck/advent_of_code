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

poss = [elm for elm in directions.keys() if elm.endswith("A")]
loopss = [[] for _ in poss]
# explore = [0:len(poss)]
explore = [3]
dir_i = 0
glob_i = 0
stop = False
while not stop:
    poss = [get_next_direction(pos, instructions[dir_i]) for pos in poss]

    dir_i += 1
    glob_i += 1
    if dir_i >= len(instructions):
        dir_i = 0
    
    if glob_i % 1000000 == 0:
        print(glob_i)
        for i, loops in enumerate(loopss):
            print(f"Loops #{i}: ", end='')
            summary = {}
            prec = 0
            for p in loops:
                loopLength = p - prec
                summary[loopLength] = summary.get(loopLength,0) + 1
                prec = p
            for loopLength in summary:
                print(f"{loopLength} x {summary[loopLength]}", end=', ')
            print()
    
    stop = True
    for i, pos in enumerate(poss):
        if pos.endswith("Z"):
            loopss[i].append(glob_i)
        else:
            stop = False
            break

print(glob_i)