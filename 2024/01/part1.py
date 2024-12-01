list1 = []
list2 = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        elements = line.replace('\n','').split("   ")
        list1.append(int(elements[0]))
        list2.append(int(elements[1]))

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)