import sys
sys.setrecursionlimit(2500)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
    
def to_position(raw, p):
    return [int(char) for char in raw.split()[p].split(",")]
    
def to_positions(line1):
    x1 = sorted([line1[0][0], line1[1][0]])
    y1 = sorted([line1[0][1], line1[1][1]])
    
    x1range = [x for x in range(x1[0], x1[1]+1)]
    y1range = [y for y in range(y1[0], y1[1]+1)]
    
    positions = []
    for x in x1range:
        for y in y1range:
            positions.append([x,y])
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
            # print("compare", line, "with", cur, "intersect", col_cur)
        # print("")
        
    return len(set(collisions))

# driver function
input = get_input("input.txt")
print("part 1 iterative:", part1_iteration(input))

