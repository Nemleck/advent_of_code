with open("input.txt", "r") as f:
    data = f.readlines()

seeds = [int(num) for num in data[0].split(": ")[1].split(" ")]

converter = {}
curr_title = ""
for line in data[1:]:
    line = line.strip()
    
    if line == "":
        continue
    elif line[0] in ["0","1","2","3","4","5","6","7","8","9"]:
        numbers = [int(num) for num in line.split(" ")]
        converter[curr_title].append([range(numbers[1], numbers[1]+numbers[2]), range(numbers[0], numbers[0]+numbers[2])])
            # -> 1st elm is source and 2nd destination
    else:
        curr_title = line.split(" ")[0]
        converter[curr_title] = []

def convert(source, destination, number):
    for field in converter[f"{source}-to-{destination}"]:
        if number in field[0]:
            return number - field[0][0] + field[1][0]
    
    return number

def get_destination(source):
    for key in converter.keys():
        if key.startswith(source):
            return key.split("-")[-1]

def get_location(number):
    source = "seed"
    while source != "location":
        destination = get_destination(source)
        number = convert(source, destination, number)
        source = destination
    
    return number

def return_lowest(seeds):
    locations = []
    for seed in seeds:
        print(seed, get_location(seed))
        locations.append(get_location(seed))

    locations.sort()

    return locations[0]

# Part 1 Answer here
print(return_lowest(seeds))