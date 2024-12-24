data = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

m = [[e for e in line] for line in data.split("\n") if line]
b_m = [[0 for e in line] for line in data.split("\n") if line]

start_pos = []
for y in range(len(m)):
    last_plant = None
    for x in range(len(m[y])):
        if m[y][x] != last_plant:
            last_plant = m[y][x]
            start_pos.append([x, y])

tiles_left = len(m) * len(m[0])

total = 0
found = True
while len(start_pos) > 0:
    coo = start_pos[0]
    
    # Get all plant group
    group = []
    checked = []

    to_check = [coo]
    while len(to_check) > 0:
        x, y = to_check[0]
        for nx, ny in [[0,1], [0,-1], [1,0], [-1,0]]:
            in_limits = 0 <= y+ny < len(m) and 0 <= x+nx < len(m[y+ny])
            if in_limits and m[y+ny][x+nx] == m[y][x]:
                if (not [x+nx, y+ny] in checked+to_check):
                    to_check.append([x+nx, y+ny])
            else:
                b_m[y][x] += 1
            
        for i in range(len(start_pos)):
            if to_check[0] == start_pos[i]:
                start_pos.pop(i)
                break

        group.append(to_check[0])
        checked.append(to_check[0])
        tiles_left -= 1
        to_check.pop(0)
    
    print(b_m)
    for pos in group:
        total += b_m[pos[1]][pos[0]] * len(group)

print(total)