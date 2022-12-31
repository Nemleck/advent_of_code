with open("input.txt", "r") as f:
    data = f.readlines()

boxes = [[] for i in range(9)]

for i in range(8): #récupère chaque boite
    for j in range(9):
        elmToAppend = data[i][j*4:j*4+3]
        if elmToAppend != "   ":
            boxes[j].append(elmToAppend) 

[boxes[box].reverse() for box in range(len(boxes))] #inverse pour donner le bon ordre

def changeBox(box1Index: int, box2Index: int):
    global boxes

    boxes[box2Index].append(boxes[box1Index][-1])
    del boxes[box1Index][-1]

    # for elm in boxes:
    #     print(elm)
    # print(" ")

for i in range(len(data[10:])):
    line = data[i+10]
    #if line.startswith("move"):
    print(i)
    if i == 501:
        print(boxes)

    listLine = line.split(" ")
    # print(listLine)
    for j in range(int(listLine[1])):
        changeBox(int(listLine[3])-1,int(listLine[5])-1)

# print(boxes)
print([boxes[i][-1] for i in range(len(boxes))])