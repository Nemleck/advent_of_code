entry = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

data = [[f for f in e] for e in entry.split("\n")]
print(entry)

xpos = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "A":
            xpos.append((i,j))
print(xpos)

def get_next(x, y, dx, dy):
    if x+dx in range(len(data)) and y+dy in range(len(data[0])):
        return (x+dx, y+dy)

total = 0
for pos in xpos:
    check = 0
    for i in range(-1,2):
        for j in range(-1, 2):
            if i != 0 and j != 0:
                word = "A"
                for k in [-1, 1]:
                    next = get_next(pos[0], pos[1], i*k, j*k)
                    if next != None:
                        word += data[next[0]][next[1]]
                    else:
                        break
                
                if word == "AMS":
                    check += 1
                else:
                    print(word)
    
    if check >= 2:
        total += 1
    else:
        print(check, pos)

print(total)