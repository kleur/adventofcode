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
    if len(entries) == 0: return count # break recursion
    outputs = [s.split() for s in entries[0].split(" | ")][1] # consider only outputs after | delimiter
    lengths = [len(segments) for segments in outputs] # map to lengths
    count += sum([1 if length in (2,4,3,7) else 0 for length in lengths]) # only consider 2,4,3,7 lengths as they're unique
    return part1_recursive(entries[1:], count) # continue recursion
    
def part2_recursive(entries, count=0, letters_str="abcdefg"):
    if len(entries) == 0: return count # break recursion
    split_raw = [s.split() for s in entries[0].split(" | ")]
    patterns = split_raw[0]
    
    uniques = {len(p) : p for p in patterns if len(p) not in (5,6)} # dict with unique lengths
    fives = [p for p in patterns if len(p) == 5] # array with 5-segment patterns
    sixes = [p for p in patterns if len(p) == 6] # array with 6-segment patterns
    
    mappings = {"tp" : find_difference(uniques[3], uniques[2])} # difference between 7 and 1 is the top segment
    
    all_letters = set(letters_str)
    all_letters.remove(mappings["tp"]) # remove the top as we already identified it
    
    for digit in set(all_letters): # loop over set of letters to identify
        if occurs(fives, digit) == 2 == occurs(sixes, digit): mappings["tr"] = digit        # [0,9] [2,3]
        if occurs(fives, digit) == 3 == occurs(sixes, digit): mappings["bt"] = digit        # [0,6,9] [2,3,5]
        if occurs(fives, digit) == 2 and occurs(sixes, digit) == 3: mappings["br"] = digit  # [0,6,9] [5,3]
        if occurs(fives, digit) == 1 and occurs(sixes, digit) == 3: mappings["tl"] = digit  # [0,6,9] [5]
        if occurs(fives, digit) == 1 and occurs(sixes, digit) == 2: mappings["bl"] = digit  # [0,6] [2]
        if occurs(fives, digit) == 3 and occurs(sixes, digit) == 2: mappings["md"] = digit  # [2,3,5] [6,9]
        all_letters.remove(digit) # remove digit from set after identifying
    
    segments = {
        # the uniques
        sort_str(uniques[2]): 1,
        sort_str(uniques[4]): 4,
        sort_str(uniques[3]): 7,
        sort_str(uniques[7]): 8,
        # the sixes
        sort_str(find_diff(letters_str, [mappings["md"]])): 0,  # zero is missing middle segment
        sort_str(find_diff(letters_str, [mappings["tr"]])): 6,  # six is missing top-right segment
        sort_str(find_diff(letters_str, [mappings["bl"]])): 9,  # nine is missing bottom-left segment
        # the fives
        sort_str(find_diff(letters_str, [mappings["br"], mappings["tl"]])): 2,  # two misses bottom-right & top-left
        sort_str(find_diff(letters_str, [mappings["bl"], mappings["tr"]])): 5,  # five misses bottom-left & top-right
        sort_str(find_diff(letters_str, [mappings["bl"], mappings["tl"]])): 3,  # three misses top-left & bottom-left
    }
    
    nums = [segments[sort_str(outputvalue)] for outputvalue in split_raw[1]] # map output values to sorted strings to match keys
    count += int("".join([str(num) for num in nums])) # join [5,3,5,3] as string 5353, cast to int and add to accumulator
    return part2_recursive(entries[1:], count) # continue recursion
    
# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 2 recursive:", part2_recursive(input))
