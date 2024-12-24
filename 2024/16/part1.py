data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

def sin(x: int):
    x = abs(x)
    if x == 3:
        return 1
    else:
        return x

m = [[e for e in line] for line in data.split("\n")]
start_pos = end_pos = None
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "S":
            start_pos = [x, y]
        elif m[y][x] == "E":
            end_pos = [x, y]

DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
solution = None

paths = [{"pos":[start_pos[0], start_pos[1]],"direction":0, "score": 0}]
while len(paths) > 0:
    x, y = paths[0]["pos"]

    for i in range(len(DIRECTIONS)):
        dx, dy = DIRECTIONS[i]
        
        if type(m[y][x]) is int:
            if m[y][x] != paths[0]["score"]:
                break

            new_points = m[y][x] + 1 + 1000 * sin( (i - paths[0]["direction"]) )
        else:
            new_points = 1 + 1000 * sin( (i - paths[0]["direction"]) )

        if m[y+dy][x+dx] == ".":
            paths.append({"pos":[x+dx, y+dy],"direction":i, "score":new_points})
            m[y+dy][x+dx] = new_points

            if new_points in [1005, 1006, 1007]:
                print(paths[0], sin(i - paths[0]["direction"]), DIRECTIONS[i])
                print("\n".join([" ".join([f"{e:4}" for e in line]) for line in m]))

        elif m[y+dy][x+dx] == "E":
            if solution == None or new_points < solution:
                solution = new_points

        elif type(m[y+dy][x+dx]) is int:
            if new_points <= m[y+dy][x+dx]:
                paths.append({"pos":[x+dx, y+dy],"direction":i, "score":new_points})
                m[y+dy][x+dx] = new_points

        
    paths.pop(0)

print("\n".join([" ".join([f"{e:4}" for e in line]) for line in m]))
print(solution)