with open("input.txt", "r") as f:
    data = f.read()

m = [["." for i in range(70+1)] for j in range(70+1)]
lines = data.split("\n")

for i in range(1024):
    x, y = [int(e) for e in lines[i].split(",")]
    m[y][x] = "#"

print("\n".join(["".join(line) for line in m]))


DIRECTIONS = [[0,1],[1,0],[0,-1],[-1,0]]
to_check = [[0,0]]
m[0][0] = 0

steps = None
while len(to_check) > 0:
    for dx, dy in DIRECTIONS:
        x, y = to_check[0]
        nx, ny = to_check[0][0]+dx, to_check[0][1]+dy

        if 0 <= ny < len(m) and 0 <= nx < len(m[ny]):
            if nx == 70 and ny == 70:
                new_score = m[y][x] + 1
                if steps == None or new_score < steps:
                    steps = new_score

            elif m[ny][nx] == ".":
                m[ny][nx] = m[y][x] + 1
                to_check.append([nx, ny])
    
    to_check.pop(0)

print("\n".join([" ".join([f"{e:2}" for e in line]) for line in m]))
print(steps)