from monkeys_to_json import get_monkeys
from utils import *

monkeys = get_monkeys()

print(get_items(monkeys))
for round in range(20):
    for monk_i in range(len(monkeys.keys())):
        monkey = monkeys[str(monk_i)]

        print(f"Monkey {monk_i}:")
        for item_i in range(len(monkey["items"])):
            item = monkey["items"][item_i]

            print(f"  Monkey inspects an item with a worry level of {item}.")
            monkey["inspect_num"] += 1

            mod_num = monkey["operation"][1:]
            if "old" in mod_num:
                mod_num = item
            else:
                mod_num = int(mod_num)

            if "+" in monkey["operation"]:
                item += mod_num
                print(f"    Worry level increases by {mod_num} to {item}.")
            
            else:
                item *= mod_num
                print(f"    Worry level is multiplied by {mod_num} to {item}.")
            
            item /= 3
            item = int(item)

            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}.")

            if item % monkey["test"] == 0:
                test_str = ""
                throw_monkey = monkey["true"]
            else:
                test_str = " not"
                throw_monkey = monkey["false"]
            
            monkeys[throw_monkey]["items"].append(item)
            
            print(f"    Current worry level if{test_str} divisible by {monkey['test']}.")
            print(f"    Item with worry level {item} is thrown to monkey {throw_monkey}.")
        
        monkey["items"] = []
    
    print(get_items(monkeys))

print([monkey["inspect_num"] for monkey in monkeys.values()])