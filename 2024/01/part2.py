list1 = []
list2 = {}

with open("input.txt", "r") as f:
    for line in f.readlines():
        elements = line.replace('\n','').split("   ")
        list1.append(int(elements[0]))

        right_elm = int(elements[1])
        if right_elm in list2.keys():
            list2[right_elm] += 1
        else:
            list2[right_elm] = 1


total = 0
for i in range(len(list1)):
    if list1[i] in list2.keys():
        total += list1[i] * list2[list1[i]]

print(total)