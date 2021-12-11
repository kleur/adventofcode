import sys
sys.setrecursionlimit(2000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
    
def part1_recursive(entries, count=0):
    if len(entries) == 0: return count
    outputs = [s.split() for s in entries[0].split(" | ")][1]
    lengths = [len(segments) for segments in outputs]
    count += sum([1 if length in (2,4,3,7) else 0 for length in lengths])
    return part1_recursive(entries[1:], count)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))

