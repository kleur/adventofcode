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

def part2_recursive(lines, acc):
    if len(lines) == 0:
        return acc
    pair = [[int(b) for b in a.split("-")] for a in lines[0].split(",")]
    
    start1 = pair[0][0]
    start2 = pair[1][0]
    end1 = pair[0][1]
    end2 = pair[1][1]
    
    hit1 = start1 <= start2 <= end1 or start1 <= end2 <= end1
    hit2 = start2 <= start1 <= end2 or start2 <= end1 <= end2
    if (hit1 or hit2): acc += 1

    return part2_recursive(lines[1:], acc)

# driver function
input = get_input("test_input.txt")

print("part 1 recursive:", part1_recursive(input, 0))
print("part 2 recursive:", part2_recursive(input, 0))