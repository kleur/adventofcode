import sys
sys.setrecursionlimit(10000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def is_visible(grid, x, y):
    cur = grid[y][x]
    if (x == 0 or x == len(grid[0])-1): return 1
    if (y == 0 or y == len(grid)-1): return 1
    
    left = list(grid[y][:x])
    right = list(grid[y][x+1:])
    top = list([grid[i][x] for i in range(0, y)])
    bottom = list([grid[i][x] for i in range(y+1, len(grid))])
    
    if cur > min(max(left), max(right)): return 1
    if cur > min(max(top), max(bottom)): return 1    
    
    return 0

def view_distance(treehouse, trees, distance=0):
    if (len(trees) == 0): return distance
    if (trees[0] >= treehouse): return distance + 1
    return view_distance(treehouse, trees[1:], distance + 1)

def scenic_score(grid, x, y):
    cur = grid[y][x]
    
    left = list(grid[y][:x])
    right = list(grid[y][x+1:])
    top = list([grid[i][x] for i in range(0, y)])
    bottom = list([grid[i][x] for i in range(y+1, len(grid))])
    
    l_dist = view_distance(cur, left[::-1])
    r_dist = view_distance(cur, right)
    t_dist = view_distance(cur, top[::-1])
    b_dist = view_distance(cur, bottom)
    
    return l_dist * r_dist * t_dist * b_dist
        
def part1_recursive(grid, x=0, y=0, acc=0):
    visible = is_visible(grid, x, y)
    acc += visible
    if (x+1 < len(grid[0])): return part1_recursive(grid, x+1, y, acc)
    elif(y+1 < len(grid)): return part1_recursive(grid, 0, y+1, acc)
    else: return acc

def part2_recursive(grid, x=0, y=0, acc=[]):
    acc.append(scenic_score(grid, x, y))
    if (x+1 < len(grid[0])): return part2_recursive(grid, x+1, y, acc)
    elif(y+1 < len(grid)): return part2_recursive(grid, 0, y+1, acc)
    else: return max(acc)

# driver function
input = get_input("test_input.txt")

print("part 1 recursive:", part1_recursive(input))
print("part 2 recursive:", part2_recursive(input))