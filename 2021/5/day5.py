# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
    
def to_position(raw, p):
    pos_strings = raw.split()[p].split(",")
    return [int(ps) for ps in pos_strings]
    
#TODO: refactor
def to_positions(raw, include_diagonal):
    a = to_position(raw, 0)
    b = to_position(raw, 2)
    
    x_range = []
    y_range = []
    
    if a[0] == b[0]:
        # vertical
        y_range = range(min(a[1], b[1]), max(a[1], b[1])+1)
        return [str([a[0],y]) for y in y_range]
    if a[1] == b[1]:
        # horizontal
        x_range = range(min(a[0], b[0]), max(a[0], b[0])+1)
        return [str([x,a[1]]) for x in x_range]
    elif include_diagonal:
        # diagonal
        if a[0] < b[0]:
            x_range = range(a[0], b[0] + 1, 1)
        if a[0] > b[0]:
            x_range = range(a[0], b[0] - 1, -1)
        if a[1] < b[1]:
            y_range = range(a[1], b[1] + 1, 1)            
        if a[1] > b[1]:
            y_range = range(a[1], b[1] - 1, -1)            
        return [str([x_range[i],y_range[i]]) for i in range(len(x_range))]
    return []

def find_duplicates(positions):
    seen = {}
    dupes = []

    for x in positions:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    return dupes
            
def part1_iteration(data):
    all_pos = []
    for raw in data:
        all_pos.extend(to_positions(raw, False))
    return len(set(find_duplicates(all_pos)))
    
def part2_iteration(data):
    all_pos = []
    for raw in data:
        all_pos.extend(to_positions(raw, True))
    return len(set(find_duplicates(all_pos)))
    
# driver function
input = get_input("test_input.txt")
print("part 1 iterative:", part1_iteration(input))
print("part 2 iterative:", part2_iteration(input))