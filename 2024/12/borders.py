from copy import deepcopy


data = """
.AA
A.A.
.AA
"""

m = [[e for e in line] for line in data.split("\n") if line]

As = []
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "A":
            As.append([x, y])

lefter = None
righter = None
higher = None
bottomer = None
for x, y in As:
    if lefter == None or x < lefter:
        lefter = x
    if righter == None or x > righter:
        righter = x
    if higher == None or y < higher:
        higher = y
    if bottomer == None or y > bottomer:
        bottomer = y

border_variations = {"..":4, "X.":4, ".X":0, "XX":2}
advanced_variations = {"..X.":0, "..XX":2, "X.X.":2, ".XX.":-2, "X.XX":4, ".XXX":0, "XXX.":-2, "XXXX":0}

counter = 0
temp_m = [["." for x in range(lefter, righter+1)] for y in range(higher, bottomer+1)]
for x in range(lefter, righter+1):
    for y in range(higher, bottomer+1):
        if [x, y] in As:
            neighbors = ""
            for dx, dy in [[-1, -1], [0, -1], [-1, 0], [-1, 1]]:
                if ( not (0 <= dy+y < len(temp_m) and 0 <= dx+x < len(temp_m[y])) ) or temp_m[dy+y][dx+x] == ".":
                    neighbors += "."
                else:
                    neighbors += "X"
            
            temp_m[y][x] = "X"
            
            if neighbors[2] == ".":
                counter += border_variations[neighbors[0:2]]
            else:
                counter += advanced_variations[neighbors]

            print(neighbors)

print(counter)