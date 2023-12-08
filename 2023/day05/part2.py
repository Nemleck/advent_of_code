from part1 import *

# seeds = []
str_nums = data[0].split(": ")[1].split(" ")
# for i in range(len(str_nums)):
#     if i % 2 == 0:
#         seeds.append(range(int(str_nums[i]), int(str_nums[i])+int(str_nums[i+1])))

seeds = [int(str_nums[i]) for i in range(len(str_nums)) if i % 2 == 0]

# seeds = list(range(379216444-10, 379216444+10))

print(return_lowest(seeds))