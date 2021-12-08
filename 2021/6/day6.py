# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line for line in f]
    return [int(s) for s in lines[0].split(",")]

# part 1
def part1_recursive(lanternfish, limit, day=0): 
    if limit == 0: return len(lanternfish)
    if day == 0: print("Initial state:", lanternfish)
    day += 1
    fishtoday = []
    for fish in lanternfish:
        if fish == 0:
            fishtoday.extend([6,8])
        else:
            fishtoday.append(fish-1)
    
    print("After " + str(day) + " days:", len(fishtoday), fishtoday)
    return part1_recursive(fishtoday, limit-1, day)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input, 18))