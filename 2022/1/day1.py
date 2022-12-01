# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def to_packages(lines):
    packages = []
    current_package = 0
    for i in range(0, len(lines)+1):
        # make sure to catch the last one
        if (i == len(lines) or lines[i] == ""):
            packages.append(current_package)
            current_package = 0
        else:
            current_package += int(lines[i])
    return packages

def part1_iterative(lines):
    packages = to_packages(lines)
    return max(packages)

def part2_iterative(lines):
    packages = to_packages(lines)
    packages.sort()
    return sum(packages[-3:])

# driver function
input = get_input("test_input.txt")

print("part 1 iterative:", part1_iterative(input))
print("part 2 iterative:", part2_iterative(input))