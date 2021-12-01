import sys
sys.setrecursionlimit(2500)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines

# recursion
def recursive(depths, window, count=0):
    if len(depths) == window:
        return count
    if (depths[window] > depths[0]):
        count += 1
    return recursive(depths[1:], window, count)

# iteration
def iteration(depths, window, count=0):
    for i in range(len(depths)):
        if depths[i] > depths[i-window]:
            count += 1
    return count

# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", recursive(input, 1))
print("part 1 iterative:", iteration(input, 1))
print("part 2 recursive:", recursive(input, 3))
print("part 2 iterative:", iteration(input, 3))
