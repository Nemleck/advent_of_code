with open("input") as f:
    data = f.read()
    ls, moves = data.strip().split("\n\n")

    map_string, instructions_string = data.split("\n\n")
    double_map_string = ""

    for char in map_string:
        if char == "#":
            double_map_string += "##"
        elif char == "O":
            double_map_string += ".."
        elif char == ".":
            double_map_string += ".."
        elif char == "@":
            double_map_string += "@."
        else:
            double_map_string += char
    
    m = [[e for e in line] for line in double_map_string.split('\n') if line]


dirs = {"^": -1, "v": 1, "<": -1j, ">": 1j}
moves = [dirs[x] for x in moves.replace("\n", "")]


def solve(part2):
    walls = set()
    boxes = set()

    for i, l in enumerate(ls.split("\n")):
        for j, x in enumerate(l):
            z = i + j * (2j if part2 else 1j)
            match x:
                case "#":
                    walls |= {z, z + 1j} if part2 else {z}
                case "O":
                    boxes.add(z)
                case "@":
                    robot = z

    for dz in moves:
        to_move = set()
        to_check = [robot + dz]
        while to_check:
            z = to_check.pop()
            is_right_side = part2 and (left := z - 1j) in boxes
            if z in boxes or is_right_side:
                to_move.add(left if is_right_side else z)
                to_check.append(z + dz)
                if part2 and dz.real:
                    other = left if is_right_side else z + 1j
                    to_check.append(other + dz)
            elif z in walls:
                break
        else:
            boxes -= to_move
            boxes |= {w + dz for w in to_move}
            robot += dz

    for box in boxes:
        m[int(box.real)][int(box.imag)] = "O"
    print("\n".join(["".join(l) for l in m]))
    print("a,", boxes)

    tot = sum(boxes)
    return tot.real * 100 + tot.imag


# Part 1
print(solve(False))

# Part 2
print(solve(True))