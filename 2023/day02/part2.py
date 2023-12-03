with open("input.txt", "r") as f:
    data = f.readlines()

total = 0
for line in data:
    splitted = line.strip().split(": ")
    
    game_number = int(splitted[0].split(" ")[1])

    sorts = splitted[1].split("; ")
    
    lowest = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for sort in sorts:
        cubes = sort.split(", ")
        for cube_str in cubes:
            cube = cube_str.split(" ")

            if int(cube[0]) > lowest[cube[1]]:
                lowest[cube[1]] = int(cube[0])

    print(lowest["red"] * lowest["green"] * lowest["blue"])
    total += lowest["red"] * lowest["green"] * lowest["blue"]
    
print(total)