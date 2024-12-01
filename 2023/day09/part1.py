with open("input.txt", "r") as f:
    data = f.readlines()

def get_depths_list(nums: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)):
        if i+1 < len(nums):
            result.append(nums[i+1] - nums[i])
    return result

def get_next_value(nums):
    all_nums_list = [nums]
    
    # Get all depths lists from 1st list
    while len(set(all_nums_list[-1])) != 1:
        all_nums_list.append(get_depths_list(all_nums_list[-1]))
        print(all_nums_list[-1])
    
    # Append new element
    for i in range(len(all_nums_list)-2, -1, -1):
        if i == len(all_nums_list)-1:
            all_nums_list[i].append(all_nums_list[i][-1])
        
        else:
            all_nums_list[i].append(all_nums_list[i+1][-1] + all_nums_list[i][-1])

    return all_nums_list

total = 0
for line in data:
    total += get_next_value([int(elm) for elm in line.strip().split(" ")])[0][-1]
    print(total)