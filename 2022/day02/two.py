with open("input.txt", "r") as f: #get data from file
    data = f.read().splitlines()

# data = ["A X","C X","C Y","A X","A Z","B Y"]

points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
lose = {"A": 3, "B": 1, "C": 2}
win = {"A": 2, "B": 3, "C": 1}

def gameIndex(data):
    index = []

    for line in data:
        if line != "":
            index.append([line[2], line[0]])
    
    return index


def game(choiceA, choiceB): #choiceA = X, choiceB = A
    won = 0
    if choiceA == "X":
        won = 0 + lose[choiceB]
    elif choiceA == "Y":
        won = 3 + points[choiceB]
    elif choiceA == "Z":
        won = 6 + win[choiceB]
    
    # print(won)
    return won

index = gameIndex(data)

totalPoints = 0
for turn in index:
    totalPoints += game(turn[0], turn[1])

print(totalPoints)