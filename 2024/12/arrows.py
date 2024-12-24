from copy import deepcopy


data = """
AAA
A.A.
.AA
"""

m = [[e for e in line] for line in data.split("\n") if line]

As = []
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "A":
            As.append([x, y])

DIRECTIONS = [[0,-1], [-1, 0], [0, 1], [1, 0]]

stop = False
d = 3

for ax, ay in As:
    counter = 0
    for dx, dy in DIRECTIONS:
        if [ax+dx, ay+dy] not in As:
            counter = 1
    
    if counter >= 2:
        x, y = ax, ay

counter = 1
while not stop:
    vx, vy = DIRECTIONS[d]
    dx, dy = DIRECTIONS[(d-1)%len(DIRECTIONS)]
    gx, gy = DIRECTIONS[(d+1)%len(DIRECTIONS)]

    if [x+vx, y+vy] in As:
        x, y = x+vx, y+vy

        if [x, y] == [ax, ay]:
            stop = True

    else:
        if [x+dx, y+dy] in As:
            d = (d-1) % len(DIRECTIONS)
        else:
            d = (d+1) % len(DIRECTIONS)
        
        counter += 1
        right = False

    m_bis = deepcopy(m)
    char = ["^", "<", "v", ">"]

    m_bis[y][x] = char[d]

    print("\n".join([" ".join(line) for line in m_bis]))
    print("————————")

print(counter)