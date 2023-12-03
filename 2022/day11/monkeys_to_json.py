def get_monkeys():
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    monkeys = {}
    cursor = 0
    for line in data:
        real_line = line.replace("\n","").lower().strip()
        
        if real_line == "":
            continue

        if real_line.startswith("monkey"):
            temp_cursor = real_line.replace("monkey ","").replace(":","")

            try:
                int(temp_cursor)
            except:
                continue
                
            cursor = temp_cursor
            
            monkey_object = {
                "items": [],
                "operation": "",
                "test": None,
                "true": None,
                "false": None,
                "inspect_num": 0
            }

            monkeys[cursor] = monkey_object
        
        if cursor not in monkeys.keys():
            continue
        
        elif real_line.startswith("starting items"):
            monkeys[cursor]["items"] = [int(elm) for elm in real_line.replace("starting items: ","").split(", ")]
        
        elif real_line.startswith("operation"):
            monkeys[cursor]["operation"] = real_line.replace("operation: new = old ","").replace(" ","")
        
        elif real_line.startswith("test"):
            monkeys[cursor]["test"] = int(real_line.replace("test: divisible by ",""))
        
        elif "true" in real_line:
            monkeys[cursor]["true"] = real_line.replace("if true: throw to monkey ","")

        elif "false" in real_line:
            monkeys[cursor]["false"] = real_line.replace("if false: throw to monkey ","")
                                           
        print(real_line)
    
    return monkeys