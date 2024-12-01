with open("input.txt", "r") as f:
    data = f.read().replace("\n","")

floor = 0
first_char_under = None
for i, char in enumerate(data):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        print(char)
    
    if not first_char_under and floor < 0:
        first_char_under = i+1

print(f"Total : {floor}, First pos under : {first_char_under}")