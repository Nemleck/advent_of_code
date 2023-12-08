with open("input.txt", "r") as f:
    data = f.readlines()

total = 0
for line in data:
    line_total = 0

    splitted = line[10:].split(" | ")
    winning_numbers = [int(num.strip()) for num in splitted[0].split(" ") if num != ""]
    playing_numbers = [int(num.strip()) for num in splitted[1].split(" ") if num != ""]

    won_numbers = [num for num in playing_numbers if num in winning_numbers]
    print(won_numbers)

    if len(won_numbers) > 0:
        print(len(won_numbers), 2**(len(won_numbers)-1))
        total += 2**(len(won_numbers)-1)

print(total)