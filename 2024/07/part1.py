data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

import itertools

total = 0
operations = ["+", "*"]

for line in data.split("\n"):
    splitted = line.split(": ")
    result = int(splitted[0])
    nums = [int(e) for e in splitted[1].split(" ")]
    
    combines = list(itertools.product([0, 1], repeat=len(nums)-1))
    
    check = False
    for combine in combines:
        test_result = nums[0]
        for i in range(len(combine)):
            oper = combine[i]
            if oper == 0:
                test_result += nums[i+1]
            if oper == 1:
                test_result *= nums[i+1]
        
        if test_result == result:
            check = True
            break
    
    if check:
        total += result

print(total)