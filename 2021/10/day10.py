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

# lookup table
mir2 = {
    "(": {"close":")", "points": 1},
    "[": {"close":"]", "points": 2},
    "{": {"close":"}", "points": 3},
    "<": {"close":">", "points": 4}
}
    
def autocomplete(remaining, acc=""):
    if len(remaining) == 0:
        if len(acc) > 0:
            points =[mir2[g]["points"] for g in acc][::-1]
            score = 0
            for p in points:
                score = (5 * score) + p
            return score
    cur = remaining[0]
    if cur in [v["open"] for v in mir.values()]:
        acc += cur
    elif len(acc) > 0:
        if acc[-1] != mir[cur]["open"]:
            return 0
        else:
            return autocomplete(remaining[1:], acc[:-1])
    return autocomplete(remaining[1:], acc)
    
def part2_recursive(lines, scores=[]):
    if len(lines) == 0: 
        result = sorted(filter(lambda c: c > 0, scores))
        halfway = len(result)/2
        return result[halfway]
    scores.append(autocomplete(lines[0]))
    return part2_recursive(lines[1:])
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 2 recursive:", part2_recursive(input))