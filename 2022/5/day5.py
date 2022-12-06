import sys
sys.setrecursionlimit(2000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line for line in f]
    return lines

def to_procedures(procedure_lines):
    split_lines = [pl.split(' ') for pl in procedure_lines]
    return [[int(x[1]), int(x[3]), int(x[5])] for x in split_lines]
    
        
def part1_iterative(lines):
    drawing_lines = []
    procedure_lines = []
    for line in lines:
        if (line.startswith("move")):
            procedure_lines.append(line)
        elif (line != ""):
            drawing_lines.append(line)
            
    procedures = to_procedures(procedure_lines)
    
    number_line = drawing_lines[-2]
    stack_numbers = dict.fromkeys({int(k.strip()) for k in number_line.split('  ')}, [])
    stacks = []

    for i in range(1, len(number_line), 4):
        stack = []
        for dline in drawing_lines[:-2]:
            char = dline[i].strip()
            if (char != ''): stack.append(char)
        stacks.append(stack)
    
    for i in range(1, len(stacks) +1):
        stack_numbers[i] = stacks[i-1]
        
    print(stack_numbers)
    for p in procedures:
        stack_rm = stack_numbers[p[1]]
        stack_ad = stack_numbers[p[2]]
        stack_sq = stack_rm[:p[0]]
        #stack_sq = stack_rm[:p[0]][::-1]
        stack_lf = stack_rm[p[0]:]
        stack_ri = stack_sq + stack_ad
        
        stack_numbers[p[1]] = stack_lf
        stack_numbers[p[2]] = stack_ri
        
        print()
        print("move", p[0], stack_sq, "from", p[1], stack_rm, "to", p[2], stack_ad)
        print(stack_numbers)
    
    return "".join([s[0] for s in stack_numbers.values()])
        

# driver function
input = get_input("test_input.txt")

print("part 2 iterative:", part1_iterative(input))