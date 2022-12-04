import sys
sys.setrecursionlimit(2000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
        
def part1_recursive(lines, acc):
    if len(lines) == 0:
        return acc
    pair = [[int(b) for b in a.split("-")] for a in lines[0].split(",")]
    
    start1 = pair[0][0]
    start2 = pair[1][0]
    end1 = pair[0][1]
    end2 = pair[1][1]
    
    l_contains = start1 <= start2 and end1 >= end2
    r_contains = start2 <= start1 and end2 >= end1
    
    if (l_contains or r_contains): acc += 1
    return part1_recursive(lines[1:], acc)

# driver function
input = get_input("test_input.txt")

print("part 1 recursive:", part1_recursive(input, 0))