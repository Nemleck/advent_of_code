#boucle avec param qui s'incrémente de 1
#valeur x modifiable autre que le param de la boucle
#le 20e cycle et ensuite tous les 40 (20, 60, 100, 140, 180, 220) 
#   -> multiplier le n° du cycle par x et ajouter ça au total (3e valeur de la boucle)

#get file
with open("input.txt","r") as f:
    data = f.readlines()

def cycleRemain(num: int, instruct):
    global cycle
    for i in range(num):
        cycle += 1
        check()
        if i == (num - 1):
            instruct()

def check():
    global total

    if (cycle - 20) % 40 == 0:
        total += cycle * x

#main loop
global cycle, x, total

x = 1
total = cycle = 0
for instruct in data:
    if instruct.startswith("addx"):
        def addx():
            global x

            x += int(instruct.split(" ")[1])
            print(x)

        cycleRemain(2, addx)
    else:
        cycle += 1
        check()

print(total)