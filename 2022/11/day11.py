# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def pretty(troop):
    for monkey in troop.keys():
        print(monkey, troop[monkey])

def print_holdings(troop):
    for monkey in troop.keys():
        print('Monkey', monkey, ':', troop[monkey]['items'])
    print()
        
def execute(op, item):
    x = item if op[1] == 'old' else int(op[1])
    if (op[0] == '*'):
        item = item * x
        print('  Worry level is multiplied by', x, 'to', item)
    if (op[0] == '+'):
        item = item + x
        print('  Worry level increases by', x, 'to', item)
    return int(item/3)
        
def part1_iterative(lines, rounds=20, troop={}):
    
    # parse the input
    for i in range(0, len(lines), 7):
        monkey = int(lines[i][:-1].split(' ')[1])
        troop[monkey] = {
            'items': [int(s.strip()) for s in lines[i+1].split(':')[1].split(',')],
            'op': lines[i+2].split(' ')[4:],
            'test': int(lines[i+3].split(' ')[3]),
            'true': int(lines[i+4].split(' ')[5]),
            'false': int(lines[i+5].split(' ')[5]),
            'inspected': 0
        }
    pretty(troop)
    
    # loop through rounds 1-20
    for rnd in range(1, rounds+1):
        print('round', rnd)
        for monkey_id in troop.keys():
            print('Monkey', monkey_id, ':')
            monkey = troop[monkey_id]
            for item in monkey['items']:
                print(' Monkey inspects an item with a worry level of', item)
                monkey['inspected'] = monkey['inspected']+1 
                
                new = execute(monkey['op'], item)
                print('  Monkey gets bored with item. Worry level is divided by 3 to', new)
                divisible = new % monkey['test'] == 0
                
                throwee = monkey['true'] if divisible else monkey['false']
                print('  Current worry level is divisible by', monkey['test'], divisible)
                print('  Item with worry level', new, 'is thrown to monkey', throwee)
                
                # throw the item
                new_items = troop[throwee]['items'] + [new]
                troop[throwee]['items'] = new_items
            
            # all items thrown
            monkey['items'] = []
            
        print('\nAfter round', rnd, 'the monkeys are holding items with these worry levels:')
        print_holdings(troop)
    
    pretty(troop)
    top_inspectors = sorted([monkey['inspected'] for monkey in troop.values()])[-2:]
    return top_inspectors[0] * top_inspectors[1] 
    

# driver function
input = get_input("test_input.txt")

print("part 1 iterative:", part1_iterative(input))