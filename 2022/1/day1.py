# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def part1_iterative(lines):
    packages = []
    current_package = 0
    for i in range(0, len(lines)+1):
        print(i, "of", len(lines))
        # make sure to catch the last one
        if (i == len(lines) or lines[i] == ""):
            print("adding", current_package)
            packages.append(current_package)
            current_package = 0
        else:
            print(lines[i])
            current_package += int(lines[i])
    print(packages)
    return max(packages)

# driver function
input = get_input("test_input.txt")

print("part 1 iterative:", part1_iterative(input))