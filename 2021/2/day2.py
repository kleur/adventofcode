import sys
sys.setrecursionlimit(2500)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

# recursion
def part1_recursive(commands, x=0, y=0):
    if len(commands) == 0:
        return x * y
    split = commands[0].split()
    direction = split[0]
    incr = int(split[1])
    if direction == "down":
        y += incr
    if direction == "up":
        y -= incr
    if direction == "forward":
        x += incr
    return part1_recursive(commands[1:], x, y)
        
def part2_recursive(commands, x=0, y=0, aim=0):
    if len(commands) == 0:
        return x * y
    split = commands[0].split()
    direction = split[0]
    incr = int(split[1])
    if direction == "down":
        aim += incr
    if direction == "up":
        aim -= incr
    if direction == "forward":
        x += incr
        y += incr * aim
    return part2_recursive(commands[1:], x, y, aim)

# iteration
def part1_iteration(commands, x=0, y=0):
    for i in range(len(commands)):
        split = commands[i].split()
        direction = split[0]
        incr = int(split[1])
        if direction == "down":
            y += incr
        if direction == "up":
            y -= incr
        if direction == "forward":
            x += incr
    return x * y
    
def part2_iteration(commands, x=0, y=0, aim=0):
    for i in range(len(commands)):
        split = commands[i].split()
        direction = split[0]
        incr = int(split[1])
        if direction == "down":
            aim += incr
        if direction == "up":
            aim -= incr
        if direction == "forward":
            x += incr
            y += incr * aim
    return x * y

# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 1 iterative:", part1_iteration(input))
print("part 2 recursive:", part2_recursive(input))
print("part 2 iterative:", part2_iteration(input))