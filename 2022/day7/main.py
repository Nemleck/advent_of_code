with open("input.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

cursor = "."
directory = {}
to_analyse = []
# i = 0
for line in data:
    # i += 1
    # if i > 20:
    #     break

    line = line.replace("\n","")

    if line.startswith("$ cd"):
        file = line.split(" ")[-1]

        if file == "..":
            found = False
            while not found:
                cursor = cursor[:-1]
                print(cursor)

                if cursor[-1] == "/":
                    cursor = cursor[:-1]
                    print("MMM : " + cursor)
                    found = True
        elif file == "/":
            print("hello there")
            cursor = "."
        else:
            print("file : '" + file + "'")
            cursor += "/" + file
    
    if line[0] in ["0","1","2","3","4","5","6","7","8","9"]:
        elements = line.split(" ")
        
        directory[cursor + "/" + elements[1]] = int(elements[0])
    
    if not cursor in to_analyse:
        to_analyse.append(cursor)

# print(directory, to_analyse)

root_directory = {}

for analyse_dir in to_analyse:
    root_directory[analyse_dir] = 0

for path in directory.keys():
    for analyse_dir in to_analyse:
        if path.startswith(analyse_dir):
            root_directory[analyse_dir] += directory[path]

print(directory)
print("------------------------------------------------")
print(root_directory)

total_sum = 0
for root_size in root_directory.values():
    if root_size <= 100000:
        total_sum += root_size

print(total_sum)