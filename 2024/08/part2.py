data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

from copy import deepcopy

map = [[e for e in line] for line in data.split("\n")]
antennas = {}

def is_in_map(x, y):
    return 0 <= y < len(map) and 0 <= x < len(map[y])

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

def get_coprime(a, b):
    divisor = None
    while divisor != 1:
        divisor = gcd(a, b)
        a //= divisor
        b //= divisor
    return a,b

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
            
            vector = [ant1[pos] - ant2[pos] for pos in range(len(ant1))]
            vector[0], vector[1] = get_coprime(vector[0], vector[1])
            
            # Apply in both sides
            max_coef = len(map)
            for c in range(-max_coef, max_coef+1):
                antinode = [ant1[0] + c*vector[0], ant1[1] + c*vector[1]]
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
        if map2[elm[1]][elm[0]] == ".":
            map2[elm[1]][elm[0]] = "#"

print("\n".join(["".join(line) for line in map2]))
print(total)