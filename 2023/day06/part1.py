with open("input.txt", "r") as f:
    data = f.readlines()

times = [int(elm) for elm in data[0].split(" ")[1:] if elm != ""]
distances = [int(elm) for elm in data[1].split(" ")[1:] if elm != ""]
total = 1

def get_distance_from_holding(total_time: int, holding_time: int):
    return holding_time * (total_time - holding_time)

for run in range(len(times)):
    wins = 0
    for i in range(times[run]):
        if get_distance_from_holding(times[run], i) > distances[run]:
            wins += 1
    total *= wins

print(total)