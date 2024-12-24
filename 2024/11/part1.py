import matplotlib.pyplot as plt
from random import randint

data = "0 4 4979 24 4356119 914 85734 698829"
def get_stone_len(data, turns=25):
    stones = {}
    for elm in data.split(" "):
        if elm in stones.keys():
            stones[int(elm)] += 1
        else:
            stones[int(elm)] = 1

    for _ in range(turns):
        if _ % 10 == 0:
            print(_)

        new_stones = {}
        for s in stones.keys():
            ss = str(s)

            if s == 0:
                result = [1]
            elif len(ss) % 2 == 0:
                result = [int(ss[len(ss) // 2:]), int(ss[:len(ss) // 2])]
            else:
                result = [s * 2024]
            
            for elm in result:
                if elm in new_stones.keys():
                    new_stones[elm] += stones[s]
                else:
                    new_stones[elm] = stones[s]
        
        stones = new_stones
    
    total = 0
    for value in stones.values():
        total += value

    return total

fig, ax = plt.subplots()

lengths = []
for i in range(1):
    print(get_stone_len(data, 75))

# lengths2 = []
# for i in range(1000):
#     lengths2.append(get_stone_len(f"{i}", 10))

#     if i % 10 == 0:
#         print(i)

# lengths3 = []
# for i in range(1000):
#     lengths3.append(get_stone_len(f"{i}", 8))

# lengths4 = []
# for i in range(1000):
#     lengths4.append(get_stone_len(f"{i}", 8))

# print()
# print("\n".join([str(e) for e in lengths]))

# results = []
# for i in range(1000000):
#     if i == 0:
#         results.append(1)
#     elif len(str(i)) % 2 == 0:
#         results.append(0)
#     else:
#         results.append(2024*i)

# ax.plot(list(range(1000000)), results)
# ax.bar(list(range(1000)), lengths, color="blue")
# ax.bar(list(range(1000)), lengths2, color="red")
# ax.bar(list(range(1000)), lengths3, color="green")
# ax.bar(list(range(1000)), [100*lengths[i]/lengths2[i]/lengths3[i]/lengths4[i] for i in range(1000)], color="purple")
# ax.bar(list(range(1000)), [lengths[i]/lengths2[i] for i in range(1000)], color="magenta")
# plt.show()

# print(stones)
# print(len(stones))