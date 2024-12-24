from copy import deepcopy

data = "..."

map = [[e for e in line] for line in data.split("\n")]
antennas = {}

def is_in_map(x, y):
    return 0 <= y < len(map) and 0 <= x < len(map[y])
    

# Get all antennas
for y in range(len(map)):
    for x in range(len(map[y])):
        tile = map[y][x]
        if tile != ".":
            if tile in antennas.keys():
                antennas[tile].append((x,y))
            else:
                antennas[tile] = [(x,y)]

# Create vectors and apply them
antinodes = {}
for key in antennas.keys():
    antinodes[key] = []
    for i in range(len(antennas[key])-1):
        for j in range(i+1, len(antennas[key])):
            ant1 = antennas[key][i]
            ant2 = antennas[key][j]
            
            # Apply in both sides
            antinode1 = [2*ant1[pos] - ant2[pos] for pos in range(len(ant1))]
            antinode2 = [2*ant2[pos] - ant1[pos] for pos in range(len(ant1))]
            
            for antinode in [antinode1, antinode2]:
                check = True
                for k in antinodes.keys():
                    if antinode in antinodes[k]:
                        check = False
                        break
                
                if check and is_in_map(*antinode):
                    antinodes[key].append(antinode)

print(antinodes)

total = 0
map2 = deepcopy(map)
for key in antinodes.keys():
    total += len(antinodes[key])
    
    for elm in antinodes[key]:
        map2[elm[1]][elm[0]] = "#"

print("\n".join(["".join(line) for line in map2]))
print(total)