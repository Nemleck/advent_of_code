with open("input.txt", "r") as f:
    data = f.readlines()

#get all pairs of places
pairs = [[[int(t) for t in part.split("-")] for part in line.replace("\n","").split(",")] for line in data]

total = 0
for pair in pairs:
    found = False
    for i in range(2):
        list = [1,0]
        if pair[i][0] >= pair[list[i]][0] and pair[i][1] <= pair[list[i]][1]:
            found = True
            print(pair[i], pair[list[i]])

    if found:
        total += 1
print(total)