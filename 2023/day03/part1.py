with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

RED = "\033[0;31m"
GREEN = "\033[0;32m"
DEFAULT = "\033[0m"

total = 0
total_text = ""
found = False
for i in range(len(data)):
    text = ""
    for char_i in range(len(data[i])):
        mod_char = data[i][char_i]
        text += mod_char
        
        if mod_char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            for y in range(-1, 1+1):
                for x in range(-1, 1+1):
                    try:
                        if not data[i+y][char_i+x] in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            found = True
                            break
                    except:
                        pass
                        
            if found:
                mod_char = GREEN + mod_char + DEFAULT
            else:
                mod_char = RED + mod_char + DEFAULT
        
        else:
            
            if found:
                print(GREEN + text[0:-1] + DEFAULT + text[-1], end="")
                
                text_num = "0"
                for char in text:
                    if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        text_num += char
                total_text += f" + {text_num}"
                total += int(text_num)
            else:
                print(text, end="")
            
            found = False
            text = ""

    print()

print(total)
# print(total_text)