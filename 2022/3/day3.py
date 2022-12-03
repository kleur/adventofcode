# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

prio_mapping = "*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def split_rucksack(rucksack):
    middle = int(len(rucksack)/2)
    return [rucksack[0:middle], rucksack[middle:]]

def part1_iterative(lines):
    rucksacks = [split_rucksack(line) for line in lines]
    priorities = []
    for rucksack in rucksacks:
        common = list(set(rucksack[0]).intersection(set(rucksack[1])))[0]
        priorities.append(prio_mapping.index(common))
    return sum(priorities)

# driver function
input = get_input("test_input.txt")

print("part 1 iterative:", part1_iterative(input))
#print("part 2 iterative:", part2_iterative(input))