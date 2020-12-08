def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def is_tree(x, y, grid):
    x2 = x % len(grid[0])
    y2 = y % len(grid)
    return grid[y2][x2] == "#"


def travel(x, y, grid, step, count):
    if y > len(grid):
        return count

    if is_tree(x, y, grid):
        count += 1

    return travel(x + step["x"], y + step["y"], grid, step, count)


grid_map = get_input("input.txt")
slopes = [
    {"x": 1, "y": 1},
    {"x": 3, "y": 1},
    {"x": 5, "y": 1},
    {"x": 7, "y": 1},
    {"x": 1, "y": 2},
]


def multiply(grid, array, total=1):
    if len(array) == 0:
        return total
    trees = travel(0, 0, grid_map, array[0], 0)
    print("trees", trees)
    return trees * multiply(grid, array[1:], total)


print("product", multiply(grid_map, slopes))
