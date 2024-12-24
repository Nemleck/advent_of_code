data = "..."

from copy import deepcopy

map  = [[f for f in e] for e in data.split("\n")]
guard = (0,0)
start_pos = None
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "^":
            guard = [x, y]
            start_pos = [x, y]
            break

def print_map(map):
    str_map = ""
    for y in range(len(map)):
        for x in range(len(map[y])):
            str_map += map[y][x]
        str_map += "\n"

    print(str_map)

total = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_i = 0
times_took_O = 0

def move(map):
    global dir_i, total, times_took_O
    direction = directions[dir_i]
    
    if 0 <= guard[1] + direction[1] < len(map) and 0 <= guard[0] + direction[0] < len(map[0]):
        
        curr_tile = map[guard[1] + direction[1]][guard[0] + direction[0]]
        if curr_tile in ["#", "O"]:
            dir_i = (dir_i+1) % len(directions)
            
            if curr_tile == "O":
                times_took_O += 1
            
                if times_took_O >= 5:
                    print(total)
                    return True, "loop"
        else:
            if map[guard[1]][guard[0]] != "@":
                map[guard[1]][guard[0]] = "@"
            
            guard[1] += direction[1]
            guard[0] += direction[0]
            
        
        return False, None
    else:
        return True, None

#stop = False
#while not stop:
#    stop, _ = move(map)

for y in range(len(map)):
    for x in range(len(map[y])):
        pos = [x, y]
        
        if map[y][x] != "#":
            dir_i = 0
            guard = deepcopy(start_pos)

            copy_map = [[f for f in e] for e in data.split("\n")]
            copy_map[pos[1]][pos[0]] = "O"
            times_took_O = 0
            
            stop = False
            end = None
            j = 0
            while j < 50000 and not stop:
                j += 1
                stop, end = move(copy_map)
            
            if end == "loop" or j >= 50000:
                if j >= 50000:
                    print("djfkglsjgjfldjfjgkfldjfj j>= 50000")
                total += 1
            if total == 39:
                print_map(copy_map)
                print(x, y, start_pos)

print(total)