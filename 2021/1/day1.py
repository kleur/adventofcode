import sys
sys.setrecursionlimit(2500)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines

# recursion
def part1_recursive(depths, count=0):
    if len(depths) == 1:
        return count
    if (depths[1] > depths[0]):
        count += 1
    return part1_recursive(depths[1:], count)

# iteration
def part1_iteration(depths, count=0):
    for i in range(len(depths)):
        if depths[i] > depths[i-1]:
            count += 1
    return count

# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 1 iterative:", part1_iteration(input))