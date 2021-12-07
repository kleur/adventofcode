# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
    
def to_position(raw, p):
    return [int(char) for char in raw.split()[p].split(",")]
    
def to_range(arr):
    if len(arr) > 1 and arr[1] > arr[0]:
        rng = [pos for pos in range(arr[0], arr[1]+1, 1)]
    else:
        rng = [pos for pos in range(arr[0], arr[1]-1, -1)]
    return rng
    
def to_positions(line1):    
    x1range = to_range([line1[0][0], line1[1][0]])
    y1range = to_range([line1[0][1], line1[1][1]])    
    
    positions = []
    if len(x1range) > 1:
        for i in range(len(x1range)):        
            ix = min(i, len(x1range)-1)
            iy = min(i, len(y1range)-1)
            positions.append([x1range[ix], y1range[iy]])
    else:
        for i in range(len(y1range)):        
            ix = min(i, len(x1range)-1)
            iy = min(i, len(y1range)-1)
            positions.append([x1range[ix], y1range[iy]])
    
    return positions
    
def intersect(line1, line2):
    pos1 = to_positions(line1)
    pos2 = to_positions(line2)
    collisions = []
    for p1 in pos1:
        for p2 in pos2:
            if p1 == p2:
                collisions.append(p1)
    return collisions

def part1_iteration(data):
    all_lines = map(lambda g : [to_position(g,0), to_position(g,2)], data)
    lines = filter(lambda u : u[0][0]==u[1][0] or u[0][1]==u[1][1], all_lines)
    collisions = []
    for i in range(len(lines)-1):
        cur = lines[i]
        print("checking with line", cur)
        for line in lines[i+1:]:
            col_cur = intersect(cur, line)
            if len(col_cur) > 0:
                collisions.extend(str(pos) for pos in col_cur)
        
    return len(set(collisions))
    
def part2_iteration(data):
    lines = map(lambda g : [to_position(g,0), to_position(g,2)], data)
    collisions = []    
    for i in range(len(lines)-1):
        cur = lines[i]
        print("checking with line", cur)
        for line in lines[i+1:]:
            col_cur = intersect(cur, line)
            if len(col_cur) > 0:
                collisions.extend(str(pos) for pos in col_cur)

    return len(set(collisions))

# driver function
input = get_input("test_input.txt")
print("part 1 iterative:", part1_iteration(input))
print("part 2 iterative:", part2_iteration(input))

