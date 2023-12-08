with open("input.txt") as f:
    data = f.readlines()

bids = {}
for line in data:
    splitted = line.strip().split(" ")
    bids[splitted[0]] = int(splitted[1])

types = {
    "five of a kind": 7,
    "four of a kind": 6,
    "full house": 5,
    "three of a kind": 4,
    "two pairs": 3,
    "one pair": 2,
    "high card": 1
}

cards = {
    "A": 13, 
    "K": 12, 
    "Q": 11, 
    "J": 10, 
    "T": 9, 
    "9": 8, 
    "8": 7, 
    "7": 6, 
    "6": 5, 
    "5": 4, 
    "4": 3, 
    "3": 2, 
    "2": 1
}

def get_type(cards_set: str):
    chars = {}
    for char in cards_set:
        if not char in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    
    values = list(chars.values())
    game_type = "high card"

    if 5 in values:
        game_type = "five of a kind"
    elif 4 in values:
        game_type = "four of a kind"
    elif 3 in values:
        if 2 in values:
            game_type = "full house"
        else:
            game_type = "three of a kind"
    elif 2 in values:
        values.remove(2)
        if 2 in values:
            game_type = "two pairs"
        else:
            game_type = "one pair"

    return game_type

def get_strongest(set1, set2):
    set_type1 = types[get_type(set1)] # Type to number
    set_type2 = types[get_type(set2)]

    if set_type1 == set_type2:
        strongest = 0
        for i in range(len(set1)):
            if cards[set2[i]] == cards[set1[i]]:
                continue
            else:
                strongest = int(cards[set2[i]] > cards[set1[i]]) + 1
                break
        return strongest
    
    else:
        return (int(set_type2 > set_type1) + 1)


def sort_sets(sets: list[str]):
    final_list = []
    for set_ in sets:
        placed = False

        for i in range(len(final_list)):
            # print(f"Current list : {final_list}")
            # print(f"Testing set {i} ({set_} vs. {final_list[i]}), and {[set_, final_list[i]][get_strongest(set_, final_list[i])-1]} won.")
            if get_strongest(set_, final_list[i]) == 1:
                # print(f"Won. Placing {set_} at index {i}")
                final_list.insert(i, set_)
                placed = True
                break
            
        if not placed:
            # print(f"Never won. Placing {set_} at the end.")
            final_list.append(set_)
        
    return final_list

def get_final_points():
    sorted_list = sort_sets(bids.keys())
    print(sorted_list)
    total = 0
    for i in range(len(sorted_list)):
        total += (len(sorted_list) - i) * bids[sorted_list[i]]
    
    return total

print(get_final_points())