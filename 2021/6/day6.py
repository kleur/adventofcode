# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line for line in f]
    return [int(s) for s in lines[0].split(",")]

# part 1
def expand_recursive(fish_before, limit, day=0):
    if limit == 0: return sum(fish_before.values())
    day += 1
    # create a new dictionary with the timers reduced and fish added
    fish_after = {
        0: fish_before[1],
        1: fish_before[2],
        2: fish_before[3],
        3: fish_before[4],
        4: fish_before[5],
        5: fish_before[6],
        6: fish_before[7] + fish_before[0], # fish after birth
        7: fish_before[8],
        8: fish_before[0] # new fish
    }    
    return expand_recursive(fish_after, limit-1, day)

# driver function
def part1_recursive(lanternfish, limit):
    fish_dict = dict.fromkeys(range(0,9), 0) # create empty dict
    counts = dict((fish,lanternfish.count(fish)) for fish in set(lanternfish)) # count how many 0's, 1's etc.
    fish_dict.update(counts) # add the fish counts
    return expand_recursive(fish_dict, limit)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input, 80))
print("part 2 recursive:", part1_recursive(input, 256))