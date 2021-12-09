import sys
sys.setrecursionlimit(10000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

# to bingo boards
def to_boards(raw_lines, cells={}, boards=[], y=0):
    if len(raw_lines) == 0 or len(raw_lines[0]) == 0:
        boards.append({"cells": cells, "score": 0})
    if len(raw_lines) == 0:
        return boards
    if len(raw_lines[0]) == 0:
        return to_boards(raw_lines[1:], {}, boards, 0)
    else:
        for x, char in enumerate(raw_lines[0].split()):
            cells[int(char)] = {"x":x, "y":y}
        return to_boards(raw_lines[1:], cells, boards, y+1)

# organize into numbers & boards
def transform(raw_lines, data={}):
    data["numbers"] = [int(raw) for raw in raw_lines[0].split(",")]
    data["boards"] = to_boards(raw_lines[2:])
    return data

# determine if there's a vertical or horizontal row crossed    
def is_bingo(board):
    x = set([cell["x"] for cell in board["cells"].values()])
    y = set([cell["y"] for cell in board["cells"].values()])
    return len(x) < 5 or len(y) < 5

# score a board: bingo after how many draws, and what's the score?
def score(board, nums, draws=0):
    num = nums[0]
    if num in board["cells"].keys():
        del board["cells"][num]
    if len(nums) == 1 or is_bingo(board):
        board_score = num * sum(board["cells"].keys())
        board["score"] = board_score
        board["after"] = draws
        return board
    return score(board, nums[1:], draws+1)


def part1and2(data, sort):
    nums=data["numbers"]
    boards=data["boards"]    
    scored_boards = map(lambda board : score(board, nums), boards)
    scored_boards.sort(key=lambda brd: brd["after"])
    return scored_boards[sort]["score"]
        
# driver function
input = transform(get_input("test_input.txt"))
print("part 1 recursive:", part1and2(input, -1))