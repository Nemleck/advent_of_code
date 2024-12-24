data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

map  = [[f for f in e] for e in data.split("\n")]
guard = (0,0)
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "^":
            guard = [x, y]
            break

def print_map():
    str_map = ""
    for y in range(len(map)):
        for x in range(len(map[y])):
            str_map += map[y][x]
        str_map += "\n"

    print(str_map)

total = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_i = 0
def move():
    global dir_i, total
    direction = directions[dir_i]
    
    if 0 <= guard[1] + direction[1] < len(map) and 0 <= guard[0] + direction[0] < len(map[0]):
        
        if map[guard[1] + direction[1]][guard[0] + direction[0]] == "#":
            dir_i = (dir_i+1) % len(directions)
        else:
            if map[guard[1]][guard[0]] != "@":
                map[guard[1]][guard[0]] = "@"
                total += 1
            
            guard[1] += direction[1]
            guard[0] += direction[0]
        
        return False
    else:
        total += 1
        return True

stop = False
while not stop:
    stop = move()

print(total)