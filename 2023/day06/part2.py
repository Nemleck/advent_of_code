with open("input.txt", "r") as f:
    data = f.readlines()

time = int("".join([elm for elm in data[0].split(" ")[1:] if elm != ""]))
distance = int("".join([elm for elm in data[1].split(" ")[1:] if elm != ""]))

def get_distance_from_holding(total_time: int, holding_time: int):
    return holding_time * (total_time - holding_time)

wins = 0
for i in range(time):
    if get_distance_from_holding(time, i) > distance:
        wins += 1

print(wins)