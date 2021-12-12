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
    
def find_difference(a, b):
    return "".join(set(a).difference(set(b)))
    
def find_diff(all_segments, minus_arr):
    return "".join(sorted(set(all_segments).difference(set(minus_arr))))
    
def count_occurrence(signals, digit, count=0):
    for signal in signals:
        for c in set(signal):
            if c == digit:
                count += 1
    return count
    
def part2_recursive(entries, count=0):
    if len(entries) == 0: return count
    split = [s.split() for s in entries[0].split(" | ")]
    patterns = split[0]
    
    uniques = {len(pattern) : pattern for pattern in [p for p in patterns if len(p) not in (5,6)]}
    
    fives = [p for p in patterns if len(p) == 5]
    sixes = [p for p in patterns if len(p) == 6]
    
    mappings = {}
    mappings["top"] = find_difference(uniques[3], uniques[2])    
    
    
    all_letters = "abcdefg"
    
    all_letters = all_letters.replace(mappings["top"], "")
    
    for digit in set(all_letters):
        if (count_occurrence(fives, digit) == 3 == count_occurrence(sixes, digit)):
            mappings["bottom"] = digit
            all_letters = all_letters.replace(digit, "")
    for digit in set(all_letters):
        if (count_occurrence(fives, digit) == 1 and count_occurrence(sixes, digit)) == 3:
            mappings["top_left"] = digit
            all_letters = all_letters.replace(digit, "")
    for digit in set(all_letters):
        if (count_occurrence(fives, digit) == 1 and count_occurrence(sixes, digit)) == 2:
            mappings["bottom_left"] = digit
            all_letters = all_letters.replace(digit, "")
    for digit in set(all_letters):
        if (count_occurrence(fives, digit) == 3 and count_occurrence(sixes, digit)) == 2:
            mappings["middle"] = digit
            all_letters = all_letters.replace(digit, "")
    for digit in set(all_letters):
        if (count_occurrence(fives, digit) == 2 and count_occurrence(sixes, digit)) == 2:
            mappings["top_right"] = digit
            all_letters = all_letters.replace(digit, "")
    for digit in set(all_letters):
        if (count_occurrence(fives, digit) == 2 and count_occurrence(sixes, digit)) == 3:
            mappings["bottom_right"] = digit
            all_letters = all_letters.replace(digit, "")
    
    mydict = {
        find_diff("abcdefg", [mappings["middle"]]) : 0,
        find_diff(uniques[2], []): 1,
        find_diff("abcdefg", [mappings["bottom_right"], mappings["top_left"]]): 2,
        find_diff("abcdefg", [mappings["bottom_left"], mappings["top_left"]]): 3,
        find_diff(uniques[4], []): 4,
        find_diff("abcdefg", [mappings["bottom_left"], mappings["top_right"]]): 5,
        find_diff("abcdefg", [mappings["top_right"]]) : 6,
        find_diff(uniques[3], []): 7,
        find_diff(uniques[7], []): 8,
        find_diff("abcdefg", [mappings["bottom_left"]]):9,
    }
    
    nums = [mydict["".join(sorted(set(outputvalue)))] for outputvalue in split[1]]
    count += int("".join([str(num) for num in nums]))
            
    return part2_recursive(entries[1:], count)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 2 recursive:", part2_recursive(input))
