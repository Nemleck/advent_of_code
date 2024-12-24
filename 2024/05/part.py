data = "..."

rules = []
sequences = []
seq_mode = False
for line in data.split("\n"):
    if line == "":
        seq_mode = True
        continue
    
    if not seq_mode:
        rules.append(line.split("|"))
    else:
        dico = {}
        elements = line.split(",")
        for i in range(len(elements)):
            dico[elements[i]] = i
            
        sequences.append(dico)

print(rules, sequences)

total = 0
for dico in sequences:
    check = True
    elms = list(dico.keys())
    for j in range(30):
        for rule in rules:
            if rule[0] in elms and rule[1] in elms:
                if dico[rule[0]] > dico[rule[1]]:
                    check = False
                    dico[rule[0]], dico[rule[1]] = dico[rule[1]], dico[rule[0]]
    
    if not check:
        elms = sorted(elms, key=lambda e: dico[e])
        total += int(elms[len(elms)//2])
        print(elms)

print(total)