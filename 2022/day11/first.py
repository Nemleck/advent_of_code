class Monkey:
    def __init__(self, items: list = [], modifier = lambda x: x, test = lambda x: x==x, trueState = 0, falseState = 0):
        self.items = items
        self.modifier = modifier
        self.test = test
        self.testResult = [trueState, falseState]
        self.inspect = 0
    
    def worryLevelIncrease(self, objIndex):
        self.items[objIndex] = self.modifier(self.items[objIndex])
        self.items[objIndex] //= 3
    
    def whichMonkey(self, objIndex):
        return self.test(self.items[objIndex])
    
    def throwObj(self, objIndex, monkeyIndex: int):
        monkey = monkeys[monkeyIndex]

        monkey.addInventory(self.items[objIndex])
        del self.items[objIndex]
        print(self.items)

    def addInventory(self, object):
        self.items.append(object)

#Get file data
with open("input.txt", "r") as f:
    data = f.readlines()

#Monkeys declaration
global monkeys
monkeys = []

currentMonkey: int = 0
for line in data:
    strippedLine = line.strip()

    try:
        lastElm = int(strippedLine.split(" ")[-1])
    except:
        lastElm = 0

    if strippedLine.startswith("Monkey"):
        currentMonkey = int(strippedLine.split(" ")[1][:-1])
        monkeys.append(Monkey())

    elif strippedLine.startswith("Starting items"):
        monkeys[currentMonkey].items = [int(elm.replace(",","")) for elm in strippedLine.split(" ")[2:]]
    
    elif strippedLine.startswith("Operation"):
        # print(currentMonkey)
        if "+" in line:
            monkeys[currentMonkey].modifier = lambda x, Elm=lastElm: x + Elm
        else:
            # print("hey", lastElm)
            monkeys[currentMonkey].modifier = lambda x, Elm=lastElm: x * Elm
    
    elif strippedLine.startswith("Test"):
        num = lastElm
        # print(2%num == 0)
        monkeys[currentMonkey].test = lambda x, num=num: x % num == 0
    
    elif strippedLine.startswith("If true"):
        throwMonkey = lastElm
        monkeys[currentMonkey].testResult[0] = throwMonkey
    
    elif strippedLine.startswith("If false"):
        throwMonkey = lastElm
        monkeys[currentMonkey].testResult[1] = throwMonkey

#boucle principale
for turn in range(20):
    print(f"Turn {turn}")
    for monkeyIndex in range(len(monkeys)):
        print(f"    Monkey {monkeyIndex}")

        monkey = monkeys[monkeyIndex]
        for i in range(len(monkey.items)):
            print(f"        Monkey inspects an item with a worry level of {monkey.items[0]}")
            monkey.inspect += 1
            
            monkey.worryLevelIncrease(0)
            print(f"        New worry level is {monkey.items[0]}")

            #divisible ?
            if monkey.whichMonkey(0):
                print(f"        Worry level is divisible")
                num = 0
            else:
                print(f"        Worry level is not divisible")
                num = 1
            
            print(f"        Object with worry level of {monkey.items[0]} is thrown to monkey {monkey.testResult[num]}")
            monkey.throwObj(0, monkey.testResult[num])

total = 1
for i in range(len(monkeys)):
    monkey = monkeys[i]

    total *= monkey.inspect
    print(f"Monkey number {i} inspected {monkey.inspect} items")

print(total)