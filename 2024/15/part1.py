with open("input", "r") as f:
    data = f.read()

map_string, instructions_string = data.split("\n\n")
m = [[e for e in line] for line in map_string.split('\n') if line]
arrows = [a for a in instructions_string.replace("\n","")]
directions = {"v": [0,1], "<": [-1,0], ">": [1,0], "^": [0,-1]}

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
        elif m[ny][nx] == "O":
            o_nx, o_ny = nx+dx, ny+dy
            while m[o_ny][o_nx] == "O":
                o_nx += dx
                o_ny += dy
            
            if m[o_ny][o_nx] == ".":
                m[o_ny][o_nx] = "O"
                m[ny][nx] = "."
                bot_pos = [nx, ny]
    else:
        print("whut ?")

    m[bot_pos[1]][bot_pos[0]] = "@"
print("\n".join(["".join(l) for l in m]))

total = 0
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "O":
            total += 100*y + x

print(total)