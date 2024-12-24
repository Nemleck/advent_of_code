from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.read()

SIZE = 70

base_map = [["." for i in range(SIZE+1)] for j in range(SIZE+1)]
lines = data.split("\n")

DIRECTIONS = [[0,1],[1,0],[0,-1],[-1,0]]
base_map[0][0] = 0

for i in range(len(lines)):
    pixel_x, pixel_y = [int(e) for e in lines[i].split(",")]
    base_map[pixel_y][pixel_x] = "#"

    if i % 100 == 0:
        print(i)

    m = deepcopy(base_map)

    to_check = [[0,0]]
    steps = None
    while len(to_check) > 0:
        for dx, dy in DIRECTIONS:
            x, y = to_check[0]
            nx, ny = to_check[0][0]+dx, to_check[0][1]+dy

            if 0 <= ny < len(m) and 0 <= nx < len(m[ny]):
                if nx == SIZE and ny == SIZE:
                    new_score = m[y][x] + 1
                    if steps == None or new_score < steps:
                        steps = new_score

                elif m[ny][nx] == ".":
                    m[ny][nx] = m[y][x] + 1
                    to_check.append([nx, ny])
        
        to_check.pop(0)

    # print("\n".join([" ".join([f"{e:2}" for e in line]) for line in m]))

    if steps == None:
        print(pixel_x, pixel_y)
        break