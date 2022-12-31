with open("input.txt", "r") as f:
    data = f.readlines()

boxes = [[] for i in range(9)]

for i in range(8): #récupère chaque boite
    for j in range(9):
        elmToAppend = data[i][j*4:j*4+3]
        if elmToAppend != "   ":
            boxes[j].append(elmToAppend) 

[boxes[box].reverse() for box in range(len(boxes))] #inverse pour donner le bon ordre

def changeBox(box1Index: int, box2Index: int, elementIndex: int):
    global boxes

    boxes[box2Index].append(boxes[box1Index][elementIndex])
    del boxes[box1Index][elementIndex]

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
    
    changeList = []
    for j in range(int(listLine[1])):
        changeList.append((j+1)*(-1))
    
    print(changeList)
    changeList.reverse()
    for element in changeList:
        changeBox(int(listLine[3])-1, int(listLine[5])-1, element)

# print(boxes)
print([boxes[i][-1] for i in range(len(boxes))])