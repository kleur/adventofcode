import sys
sys.setrecursionlimit(1000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

# lookup table
mir = {
    ")": {"open":"(", "score": 3},
    "]": {"open":"[", "score": 57},
    "}": {"open":"{", "score": 1197},
    ">": {"open":"<", "score": 25137}
}

def check_line(remaining, acc=""):
    if len(remaining) == 0: return 0
    cur = remaining[0]
    if cur in [v["open"] for v in mir.values()]:
        acc += cur
    elif len(acc) > 0:
        if acc[-1] != mir[cur]["open"]:
            return mir[cur]["score"]
        else:
            return check_line(remaining[1:], acc[:-1])
    return check_line(remaining[1:], acc)
    
def part1_recursive(lines, scores=[]):
    if len(lines) == 0: 
        return sum(scores)
    scores.append(check_line(lines[0]))
    return part1_recursive(lines[1:])
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))