import sys
sys.setrecursionlimit(10000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
    
def pretty_print(boards):
    for board in boards:
        for pos in board:
            print(pos)
        print(" ")

def transform(raw_lines, data = {}, boards = [], board = {}, x = 0, y = 0):
    data["numbers"] = [int(rw) for rw in raw_lines[0].split(",")]
    raw_boards = raw_lines[2:]
    boards_count = 0
    # loop over raw lines
    for i in range(0, len(raw_boards)+1):
        # save if empty line or last line
        if i == len(raw_boards) or len(raw_boards[i]) == 0:
            boards.append(board)
            boards_count += 1
            board = {}
            x = 0
            y = 0
        else:
            line = raw_boards[i]
            for x, char in enumerate(line.split()):
                board[int(char)] = {"x": x, "y": y}
            y += 1
    data["boards"] = boards
    return data
    
def bingo(board):
    x = set([v["x"] for v in board.values()])
    y = set([v["y"] for v in board.values()])
    return len(x) != len(y)
        
def part1_recursive(data, idx_drawn=0, idx_board=0):
    if idx_drawn == len(data["numbers"]):
        return "End"

    num = data["numbers"][idx_drawn]
    board = data["boards"][idx_board]
    
    if num in board:
        del board[num]
        for key in board:
            print(key, board[key])
        print(" ")
    if (bingo(board)):
        print("BINGO!")
        return num * sum(board.keys()) # bingo!!!
    
    idx_board += 1 # consider next board
    if idx_board == len(data["boards"]):
        print("starting from the top")
        idx_drawn += 1 # draw a new number
        idx_board = 0  # start at the first board
    return part1_recursive(data, idx_drawn, idx_board)
        
# driver function
input = transform(get_input("test_input.txt"))
print("part 1 recursive:", part1_recursive(input))