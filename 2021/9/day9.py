import sys
sys.setrecursionlimit(100000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [[int(char) for char in line.strip()] for line in f]
    return lines
    
def part1_recursive(entries, x=0, y=0, count=0):
    if y == len(entries): return count    
    cur = entries[y][x]
    if cur < 9:
        adj = []
        if x > 0: adj.append(entries[y][x-1])
        if y > 0: adj.append(entries[y-1][x])
        if x < len(entries[y])-1: adj.append(entries[y][x+1])
        if y < len(entries)-1: adj.append(entries[y+1][x])
        if all([a > cur for a in adj]):
            count += (1 + cur)
    if x < len(entries[y]) -1:
        return part1_recursive(entries, x+1, y, count)
    else:
        return part1_recursive(entries, 0, y+1, count)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
