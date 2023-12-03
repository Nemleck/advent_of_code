with open("input.txt", "r") as f:
    data = f.readlines()

stock = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
for line in data:
    splitted = line.strip().split(": ")
    
    game_number = int(splitted[0].split(" ")[1])

    sorts = splitted[1].split("; ")

    is_possible = True
    for sort in sorts:
        cubes = sort.split(", ")
        for cube_str in cubes:
            cube = cube_str.split(" ")

            if int(cube[0]) > stock[cube[1]]:
                print(int(cube[0]), stock[cube[1]], cube[1])
                is_possible = False
        
    if is_possible:
        total += game_number
        
    print(game_number, sorts, is_possible)

print(total)