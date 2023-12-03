def get_items(monkeys: dict[str, dict]):
    result = "Items :\n"

    for monk_i in range(len(monkeys.values())):
        monkey = monkeys[str(monk_i)]
        
        result += f"Monkey {monk_i}: " + ", ".join([str(elm) for elm in monkey["items"]]) + "\n"
    
    return result