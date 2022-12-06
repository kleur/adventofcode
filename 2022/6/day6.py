import sys
sys.setrecursionlimit(10000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def find_start(signal, i, marker_length):
    segment = signal[i:min(len(signal), i+marker_length)]
    if (len(segment) < marker_length):
        return "Did not find"
    if (len(set(segment)) == marker_length):
        return (i+marker_length)
    return find_start(signal, i+1, marker_length)
        
def part1_recursive(signals, marker_length):
    indices = []
    for signal in signals:
        indices.append(find_start(signal, 0, marker_length))
    return indices
    

# driver function
input = get_input("test_input.txt")

print("part 1 recursive:", part1_recursive(input, 4))
print("part 2 recursive:", part1_recursive(input, 14))