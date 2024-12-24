import itertools

data = "..."

total_lines = len(data.split("\n"))

total = 0
j = -1
for line in data.split("\n"):
    j += 1
    if j%100 == 0:
        print(f"{j}/{total_lines}")
    
    splitted = line.split(": ")
    result = int(splitted[0])
    nums = [int(e) for e in splitted[1].split(" ")]
    
    combines = list(itertools.product([0, 1, 2], repeat=len(nums)-1))
    
    check = False
    for combine in combines:
        test_result = nums[0]
        for i in range(len(combine)):
            oper = combine[i]
            if oper == 0:
                test_result += nums[i+1]
            if oper == 1:
                test_result *= nums[i+1]
            if oper == 2:
                test_result = int(str(test_result) + str(nums[i+1]))
        
        if test_result == result:
            check = True
            break
    
    if check:
        total += result

print(total)