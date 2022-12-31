with open("input.txt", "r") as f:
    data = f.read().splitlines()

# data = ["A X","C X","C Y","A X","A Z","B Y"]

points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

def gameIndex(data):
    index = []

    for line in data:
        if line != "":
            index.append([line[2], line[0]])
    
    return index


def game(choiceA, choiceB):
    # Lost ?
    won = 0

    # Draw ?
    if points[choiceA] == points[choiceB]:
        won = 3

    # Won ?
    elif choiceA == "X" and choiceB == "C" or\
        choiceA == "Y" and choiceB == "A" or\
        choiceA == "Z" and choiceB == "B":
        won = 6
    
    print(won + points[choiceA])
    return won + points[choiceA]

index = gameIndex(data)

totalPoints = 0
for turn in index:
    totalPoints += game(turn[0], turn[1])

print(totalPoints)