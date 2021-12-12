import sys
sys.setrecursionlimit(2000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
   
# helper methods
def sort_str(signal):
    return "".join(sorted(set(signal)))
 
def find_difference(a, b):
    return "".join(set(a).difference(set(b)))
    
def find_diff(all_segments, minus_arr):
    return "".join(set(all_segments).difference(set(minus_arr)))
    
def occurs(signals, digit, count=0):
    for signal in signals:
        for c in set(signal):
            if c == digit:
                count += 1
    return count
    
def part1_recursive(entries, count=0):
    if len(entries) == 0: return count
    outputs = [s.split() for s in entries[0].split(" | ")][1]
    lengths = [len(segments) for segments in outputs]
    count += sum([1 if length in (2,4,3,7) else 0 for length in lengths])
    return part1_recursive(entries[1:], count)
    
def part2_recursive(entries, count=0, letters_str="abcdefg"):
    if len(entries) == 0: return count
    split_raw = [s.split() for s in entries[0].split(" | ")]
    patterns = split_raw[0]
    
    uniques = {len(p) : p for p in patterns if len(p) not in (5,6)}
    fives = [p for p in patterns if len(p) == 5]
    sixes = [p for p in patterns if len(p) == 6]
    
    mappings = {"top" : find_difference(uniques[3], uniques[2])}
    
    all_letters = set(letters_str)
    all_letters.remove(mappings["top"])
    
    for digit in set(all_letters):
        if occurs(fives, digit) == 2 == occurs(sixes, digit):
            mappings["top_right"] = digit
        if occurs(fives, digit) == 3 == occurs(sixes, digit):
            mappings["bottom"] = digit
        if occurs(fives, digit) == 2 and occurs(sixes, digit) == 3:
            mappings["bottom_right"] = digit
        if occurs(fives, digit) == 1 and occurs(sixes, digit) == 3:
            mappings["top_left"] = digit
        if occurs(fives, digit) == 1 and occurs(sixes, digit) == 2:
            mappings["bottom_left"] = digit
        if occurs(fives, digit) == 3 and occurs(sixes, digit) == 2:
            mappings["middle"] = digit
        all_letters.remove(digit)
    
    segments = {
        sort_str(uniques[2]): 1,
        sort_str(uniques[4]): 4,
        sort_str(uniques[3]): 7,
        sort_str(uniques[7]): 8,
        sort_str(find_diff(letters_str, [mappings["middle"]])) : 0,
        sort_str(find_diff(letters_str, [mappings["top_right"]])) : 6,
        sort_str(find_diff(letters_str, [mappings["bottom_left"]])): 9,
        sort_str(find_diff(letters_str, [mappings["bottom_right"], mappings["top_left"]])): 2,
        sort_str(find_diff(letters_str, [mappings["bottom_left"], mappings["top_left"]])): 3,
        sort_str(find_diff(letters_str, [mappings["bottom_left"], mappings["top_right"]])): 5,
    }
    
    nums = [segments[sort_str(outputvalue)] for outputvalue in split_raw[1]]
    count += int("".join([str(num) for num in nums]))
    return part2_recursive(entries[1:], count)
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 2 recursive:", part2_recursive(input))
