data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

m = [[e for e in line] for line in data.split("\n") if line]
b_m = [[0 for e in line] for line in data.split("\n") if line]
l_m = [[[] for e in line] for line in data.split("\n") if line]

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

                l_m[y][x].append([nx, ny])
        for i in range(len(start_pos)):
            if to_check[0] == start_pos[i]:
                start_pos.pop(i)
                break

        group.append(to_check[0])
        checked.append(to_check[0])
        tiles_left -= 1
        to_check.pop(0)

    next_pos = group[0]
    not_treated = [e for e in group]
    while len(not_treated) > 0:
        not_treated.remove(next_pos)
        x, y = next_pos
        next_pos = None

        for nx, ny in [[0,1], [0,-1], [1,0], [-1,0]]:
            if abs(nx) == 1:
                for i in [-1, 1]:
                    if not ([x, y+i] in group and [nx, ny] in l_m[y+i][x]):
                        b_m[y][x] += 1
                    else:
                        if [x, y+i] in not_treated:
                            next_pos = x, y+i
                        break
            elif abs(ny) == 1:
                for i in [-1, 1]:
                    if not ([x+i, y] in group and [nx, ny] in l_m[y][x+i]):
                        b_m[y][x] += 1
                    else:
                        if [x, y+i] in not_treated:
                            next_pos = x+i, y
                        break

            l_m[y][x].append([nx, ny])
        
        if not next_pos:
            next_pos = not_treated[0]

        # print(not_treated)
    
    # print(l_m)
    mini_total = 0
    for pos in group:
        mini_total += b_m[pos[1]][pos[0]]
    
    print(f"{len(group)} * {mini_total} = {mini_total * len(group)}")
    total += mini_total * len(group)

print(total)