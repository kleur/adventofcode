# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip().split(' ') for line in f]
    return lines
        
def part1_iterative(instructions, register=1, cycle=0, nxt_check=20, the_sum=0):
    for inst in instructions:
        op_cycles = 0
        if (inst[0] == 'noop'): op_cycles = 1
        if (inst[0] == 'addx'): op_cycles = 2
        for i in range(0, op_cycles):
            cycle += 1
            
            if (cycle == nxt_check):
                # set when to check the signal next
                nxt_check += 40
                
                # calculate signal strength
                signal_strength = cycle * register
                print('cycle', cycle, 'adding', cycle, 'x', register, '=', signal_strength)
                the_sum += signal_strength
            
            # on the last cycle, execute the operation
            if (i == op_cycles-1 and inst[0] == 'addx'): register += int(inst[1])
    return the_sum

def draw_sprite(register):
    line = ''
    for pos in range(0, 40):
        line += ('#' if (abs(pos-register) <= 1) else '.')
    return line

def part2_iterative(instructions, register=1, cycle=0, screen_end=40, crt_lines=[], cur_line=''):
    for inst in instructions:
        op_cycles = 0
        if (inst[0] == 'noop'): op_cycles = 1
        if (inst[0] == 'addx'): op_cycles = 2
        for i in range(0, op_cycles):
            cycle += 1            
            
            if (i == 0): print('Start cycle', cycle, ' : begin executing', inst)
            print('During cycle', cycle, ': CRT draws pixel in position', len(cur_line))           
            
            # add lit pixel if current pixel is the same as register, or next to it (sprite is 3 wide)
            cur_line += ('#' if (abs(len(cur_line)-register) <= 1) else '.')
            print('Current CRT row:', cur_line)
            
            # end of the screen, new line
            if (cycle == screen_end):
                screen_end += 40
                crt_lines.append(cur_line)
                cur_line = ''
            
            # on the last cycle, execute the operation
            if (i == op_cycles-1):
                if (inst[0] == 'addx'): register += int(inst[1])
                print('End of cycle', cycle, ': finish executing', inst, '(Register X is now', register, ')')
                print('Sprite position:', draw_sprite(register))
            print()
    
    # print the whole screen
    for crt_line in crt_lines:
        print(crt_line)
    return 'Done'
        
# driver function
input = get_input("test_input2.txt")

print("part 1 iterative:", part1_iterative(input))
print("part 2 iterative:", part2_iterative(input))