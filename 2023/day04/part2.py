with open("input.txt", "r") as f:
    data = f.readlines()

cards = {}
cards_len = {}
for i in range(len(data)):
    cards[i+1] = 1

    splitted = data[i][10:].split(" | ")
    winning_numbers = [int(num.strip()) for num in splitted[0].split(" ") if num != ""]
    playing_numbers = [int(num.strip()) for num in splitted[1].split(" ") if num != ""]

    cards_len[i+1] = [num for num in playing_numbers if num in winning_numbers]

total = 0
for i in cards.keys():
    print(f"{i} / {len(cards.keys())}")
    print(cards[i])
    total += cards[i]
    while cards[i] > 0:
        line_total = 0

        for j in range(len(cards_len[i])):
            if i+j+1 <= len(data):
                cards[i+j+1] += 1
        
        cards[i] -= 1

print(total)