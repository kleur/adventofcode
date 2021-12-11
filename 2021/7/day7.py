import sys
sys.setrecursionlimit(2000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [int(c) for c in [line.strip() for line in f][0].split(",")]
    return lines
    
def pretty_print(crabs, i=0):
    if i == len(crabs):
        return
    print "".join([("xx" if x == crabs[i] else "..") for x in range(min(crabs), max(crabs))])
    return pretty_print(crabs, i+1)
    
def print_grid(grid):
    for key in grid:
        if grid[key] > 0:
            print " ".join([str(grid[key]) if key == x else "." for x in range(min(grid.keys()), max(grid.keys())+1)])
    print
    
def align_recursive(grid, fuel=0):
    if len(grid.keys()) == 1:
        return [grid.keys()[0], fuel]
    
    # print_grid(grid)
    
    left = min(grid.keys()) # leftmost position of grid
    right= max(grid.keys()) # rightmost position of grid
    
    left_crabs = grid[left]
    right_crabs = grid[right]
    
    left_fuel = left_crabs # total crabs on x position = amount of fuel it costs to move them
    right_fuel = right_crabs
    
    if left_fuel <= right_fuel:
        fuel += left_fuel # add fuel to accumulator
        grid.pop(left) # remove the position
        next_left = grid[left+1] # take the next position
        grid[left+1] = next_left + left_crabs # move the crabs to next position
        
    if right_fuel <= left_fuel:
        fuel += right_fuel # add fuel to accumulator
        grid.pop(right) # remove the position
        next_right = grid[right-1] # take the next position
        grid[right-1] = next_right + right_crabs # move the crabs to next position
    
    return align_recursive(grid, fuel)
    
def align_recursive_exponential(grid, fuel=0):
    if len(grid.keys()) == 1:
        return [grid.keys()[0], fuel]
    
    left = min(grid.keys()) # leftmost position of grid
    right= max(grid.keys()) # rightmost position of grid
    
    left_crabs = [c+1 for c in grid[left]]
    right_crabs = [c+1 for c in grid[right]]
    
    left_fuel = sum(left_crabs)
    right_fuel = sum(right_crabs)
    
    if left_fuel <= right_fuel:
        fuel += left_fuel # add fuel to accumulator
        grid.pop(left) # remove the position
        next_left = grid[left+1] # take the next position
        grid[left+1] = (next_left + left_crabs) # move the crabs to next position
    
    if right_fuel <= left_fuel:
        fuel += right_fuel # add fuel to accumulator
        grid.pop(right) # remove the position
        next_right = grid[right-1] # take the next position
        grid[right-1] = (next_right + right_crabs) # move the crabs to next position
    
    return align_recursive_exponential(grid, fuel)

# driver function
def part1_recursive(crabs):
    # pretty_print(crabs)
    crabs_dict = dict.fromkeys(range(min(crabs),max(crabs)), 0) # create empty dict
    counts = dict((crab,crabs.count(crab)) for crab in set(crabs)) # count how many 0's, 1's etc.
    crabs_dict.update(counts) # add the crab counts
    return align_recursive(crabs_dict)
    
# driver function
def part2_recursive(crabs):
    # pretty_print(crabs)
    crabs_dict = dict.fromkeys(range(min(crabs),max(crabs)), []) # create empty dict
    arrays = dict((crab,[0 for i in range(crabs.count(crab))]) for crab in set(crabs)) # three crabs with x=2 -> [0,0,0] at key 2
    crabs_dict.update(arrays)
    return align_recursive_exponential(crabs_dict)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 2 recursive:", part2_recursive(input))
