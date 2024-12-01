with open("input.txt", "r") as f:
    data = f.read().replace("\n","")

floor = 0
for char in data:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        print(char)

print(f"Total : {floor}")