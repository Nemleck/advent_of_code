

# dico = {"1": [[2], [3], [4], [5], [6]]}

# MAX_TIME = 5
# def get_next(stone, time_left):
#     stones = []
    
#     while time_left > 0:
#         if stone in dico.keys():
#             if time_left-1 < len(dico[stone]):
#                 stones = dico[stone][time_left-1]
#                 time_left = 0
#             else:
#                 stones = dico[stone][-1]
#                 time_left -= len(dico[stone])

#         indent = 0
#         print(stones)
#         for i in range(len(stones)):
#             s = str(stones[i+indent])
            
#             if s == "0":
#                 stones[i+indent] = 1
#             elif len(s) % 2 == 0:
#                 stones[i+indent] = int(s[len(s) // 2:])
#                 stones.insert(i+indent, int(s[:len(s) // 2]))
                
#                 indent += 1
#             else:
#                 stones[i+indent] *= 2024
        
#         time_left -= 1
    
#     return stones

# print(get_next("1", 7))

# exit()

def get_stone_len(data):
    stones = data

    for _ in range(25):
        # print(_)
        indent = 0
        for i in range(len(stones)):
            s = str(stones[i+indent])
            
            if s == "0":
                stones[i+indent] = 1
            elif len(s) % 2 == 0:
                stones[i+indent] = int(s[len(s) // 2:])
                stones.insert(i+indent, int(s[:len(s) // 2]))
                
                indent += 1
            else:
                stones[i+indent] *= 2024
    
    return stones

data = "17"
stones = [int(e) for e in data.split(" ")]

pattern = [0, 7435, 6369, 6371, 5614, 3504, 4472, 4166, 3675, 4716]
dizaines = [19778, 32121, 31055, 31057, 30300, 28190]

import json
with open("stats.json", "r") as f:
    data = json.load(f)

total = 0
for j in range(3):
    new_stones = []
    for i in range(len(stones)):
        if j == 2:
            if stones[i] < 60:
                total += pattern[stones[i] % 10] + dizaines[stones[i] // 10]
        
            elif stones[i] < 1000:
                total += data[stones[i]]
            
            else:
                total += len(data[stones[i]])

        else:
            if stones[i] < 1000:
                new_stones += data[stones[i]]
                print("yay !:")
            else:
                new_stones += get_stone_len(stones)
        
        if i % 100 == 0:
            print("i=", i, "/", len(stones))
    
    print(j)
    stones = new_stones

print(total)