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
        print("add", incr, "to y position, total", y + incr)
        return part1_recursive(commands[1:], x, y + incr)
    if direction == "up":
        print("subtract", incr, "from y position, total", y - incr)
        return part1_recursive(commands[1:], x, y - incr)
    if direction == "forward":
        print("add", incr, "to x position, total", x + incr)
        return part1_recursive(commands[1:], x + incr, y)

# iteration
def part1_iteration(commands, x=0, y=0):
    for i in range(len(commands)):
        split = commands[i].split()
        direction = split[0]
        incr = int(split[1])
        print([direction, incr])
        if direction == "down":
            print("add", incr, "to y position, total", y + incr)
            y += incr
        if direction == "up":
            print("subtract", incr, "from y position, total", y - incr)
            y -= incr
        if direction == "forward":
            print("add", incr, "to x position, total", x + incr)
            x += incr
    return x * y

# driver function
input = get_input("test_input.txt")
print("part 1 recursive:", part1_recursive(input))
print("part 1 iterative:", part1_iteration(input))