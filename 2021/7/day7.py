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
    
    print_grid(grid)
    
    left = min(grid.keys())
    right= max(grid.keys())
    
    left_crabs = grid[left]
    right_crabs = grid[right]
    
    left_fuel = left_crabs * 1
    right_fuel = right_crabs * 1
    
    if left_fuel <= right_fuel:
        fuel += left_fuel
        next_left = grid[left+1]
        grid[left+1] = next_left + left_crabs
        del grid[left]
        
    if right_fuel <= left_fuel:
        fuel += right_fuel
        next_right = grid[right-1]
        grid[right-1] = next_right + right_crabs
        del grid[right]
    
    return align_recursive(grid, fuel)

# driver function
def part1_recursive(crabs):
    pretty_print(crabs)
    crabs_dict = dict.fromkeys(range(min(crabs),max(crabs)), 0) # create empty dict
    counts = dict((crab,crabs.count(crab)) for crab in set(crabs)) # count how many 0's, 1's etc.
    crabs_dict.update(counts) # add the crab counts
    return align_recursive(crabs_dict)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))