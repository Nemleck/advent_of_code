code = "029A"
keys = {"7":0,"8":1,"9":2, "4":1j,"5":1+1j,"6":2+1j, "1":2j,"2":1+2j,"3":2+2j, "0":1+3j,"A":2+3j, \
        "^":1, "A":2, "<": 1j, "v":1+1j, ">":2+1j}

DIRECTIONS = {1:">", -1:"<", 1j:"v", -1j:"^"}

def get_2d_distance(pos1: complex, pos2: complex):
    diff = pos1 - pos2
    return abs(diff.real) + abs(diff.imag)*1j

def sign(value: complex):
    return value.real/abs(value.real) + value.imag/abs(value.imag)

distance = 0
numpad_pos = 2 + 3j
keypad1_pos = 2
for char in code:
    numpad_distance = keys[char] - numpad_pos
    numpad_pos = keys[char]
    numpad_sign = sign(numpad_distance)

    arrow_x, arrow_y = DIRECTIONS[numpad_sign.real], DIRECTIONS[numpad_sign.imag]
    first_arrow = arrow_x
    second_arrow = arrow_y
    if keypad1_pos-keys[arrow_y] < keypad1_pos-keys[arrow_x]:
        first_arrow = arrow_y
        second_arrow = arrow_x
    
    

print(distance)