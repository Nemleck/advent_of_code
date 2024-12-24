with open("input", "r") as f:
    data = f.read()

from copy import deepcopy

map_string, instructions_string = data.split("\n\n")
double_map_string = ""

for char in map_string:
    if char == "#":
        double_map_string += "##"
    elif char == "O":
        double_map_string += "[]"
    elif char == ".":
        double_map_string += ".."
    elif char == "@":
        double_map_string += "@."
    else:
        double_map_string += char
        
m = [[e for e in line] for line in double_map_string.split('\n') if line]
arrows = [a for a in instructions_string.replace("\n","")]
directions = {"v": [0,1], "<": [-1,0], ">": [1,0], "^": [0,-1]}

def move_obj(x, y, d):
    if not m[y][x] in ["[","]"]:
        return False

    elif m[y][x] == "[":
        pair = x+1, y
    else:
        pair = x-1, y
    
    objects = [[x, y], pair]
    if d[1] == 0:
        objects = [[x, y]]
    
    for pos in objects:
        if m[pos[1]+d[1]][pos[0]+d[0]] in ["[", "]"]:
            moved = move_obj(pos[0]+d[0], pos[1]+d[1], d)
            if not moved:
                return False
        elif m[pos[1]+d[1]][pos[0]+d[0]] == "#":
            return False
    
    for pos in objects:
        t = m[pos[1]][pos[0]]
        m[pos[1]][pos[0]] = deepcopy(m[pos[1]+d[1]][pos[0]+d[0]])
        m[pos[1]+d[1]][pos[0]+d[0]] = t
    
    return True


bot_pos = [2, 2]
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "@":
            bot_pos = [x, y]
            m[y][x] == "."
            break

for a in arrows:
    m[bot_pos[1]][bot_pos[0]] = "."

    dx, dy = directions[a]
    nx, ny = bot_pos[0]+dx, bot_pos[1]+dy

    if 0 <= ny < len(m) and 0 <= nx <= len(m[ny]):
        if m[ny][nx] == ".":
            bot_pos = [nx, ny]
        elif m[ny][nx] in ["[","]"]:
            if move_obj(nx, ny, [dx, dy]):
                bot_pos = [nx, ny]
    else:
        print("whut ?")

    m[bot_pos[1]][bot_pos[0]] = "@"
# print("\n".join(["".join(l) for l in m]))

total = 0
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "[":
            total += 100*y + x
            print([y, x], end=", ")

print(total)