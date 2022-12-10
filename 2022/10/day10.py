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

def draw_sprite(register):
    line = ''
    for pos in range(0, 40):
        line += ('#' if (abs(pos-register) <= 1) else '.')
    return line

def part2_iterative(instructions):
    register = 1
    cycle = 0
    screen_end = 40
    crt_lines = []
    cur_line = ''
    
    for inst in instructions:
        operation = {}
        if (inst[0] == 'noop'):
            operation = {'cmd': inst[0], 'cycles':1}
        if (inst[0] == 'addx'):
            operation = {'cmd': inst[0], 'cycles':2, 'add': int(inst[1])}
        for i in range(0, operation['cycles']):
            cycle += 1            
            if (i == 0): print('Start cycle', cycle, ' : begin executing', inst)
            print('During cycle', cycle, ': CRT draws pixel in position', len(cur_line))           
            cur_line += ('#' if (abs(len(cur_line)-register) <= 1) else '.')
            print('Current CRT row:', cur_line)
            if (cycle == screen_end):
                screen_end += 40
                crt_lines.append(cur_line)
                cur_line = ''
            if (i == operation['cycles']-1):
                if (operation['cmd'] == 'addx'): register += operation['add']
                print('End of cycle', cycle, ': finish executing', inst, '(Register X is now', register, ')')
                print('Sprite position:', draw_sprite(register))
            print()
    for crt_line in crt_lines:
        print(crt_line)
    return 'Done'
        
# driver function
input = get_input("test_input2.txt")

print("part 1 iterative:", part1_iterative(input))
print("part 2 iterative:", part2_iterative(input))