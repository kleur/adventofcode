import sys
sys.setrecursionlimit(2000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip().split(' ') for line in f]
    return lines
        
def part1_iterative(instructions):
    register = 1
    cycle = 0
    
    nxt_check = 20
    the_sum = 0
    
    for inst in instructions:
        operation = {}
        if (inst[0] == 'noop'):
            operation = {'cmd': inst[0], 'cycles':1}
        if (inst[0] == 'addx'):
            operation = {'cmd': inst[0], 'cycles':2, 'add': int(inst[1])}
        for i in range(0, operation['cycles']):
            cycle += 1
            if (cycle == nxt_check):
                nxt_check += 40
                signal_strength = cycle * register
                print('cycle', cycle, 'adding', cycle, 'x', register, '=', signal_strength)
                the_sum += signal_strength
            
            if (i == operation['cycles']-1):
                if (operation['cmd'] == 'addx'):
                    register += operation['add']
    return the_sum
            
        
# driver function
input = get_input("test_input2.txt")

print("part 1 iterative:", part1_iterative(input))