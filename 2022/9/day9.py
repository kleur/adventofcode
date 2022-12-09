import sys
sys.setrecursionlimit(100000)

# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip().split(" ") for line in f]
    return lines
        
def part1_recursive(motions, head={"x":0, "y":0}, tail={"x":0, "y":0}, steps=0, direction="", acc=set()):
    rope = 1
    
    # register the visited position
    acc.add(str(tail["x"]) + "-" + str(tail["y"]))
    
    # check if the motion is still in progress
    if (steps > 0):
        if (direction == "U"): head["y"] = head["y"]+1
        if (direction == "D"): head["y"] = head["y"]-1
        if (direction == "R"): head["x"] = head["x"]+1
        if (direction == "L"): head["x"] = head["x"]-1
            
        xdiff = head["x"] - tail["x"]
        ydiff = head["y"] - tail["y"]
        xabs = abs(xdiff)
        yabs = abs(ydiff)
        
        print("move (extdir)", steps, direction, "head", head)
        print("x diff", xdiff, "abs", xabs, "y diff", ydiff, "abs", yabs)
        
        if (xabs <= rope and yabs <= rope):
            print("tail stays in place", tail)
        else:
            if (xabs > rope):
                tail["x"] = tail["x"] + (int(xdiff/xabs))
                if (tail["y"] == head["y"]):
                    print("still on the same line")
                else:
                    print("need to align!")
                    tail["y"] = head["y"]
                
            if (yabs > rope):
                tail["y"] = tail["y"] + (int(ydiff/yabs))
                if (tail["x"] == head["x"]):
                    print("still on the same line")
                else:
                    print("need to align!")
                    tail["x"] = head["x"]
            
            print("tail had to move", tail)

                
        print()
        return part1_recursive(motions, head, tail, steps-1, direction, acc)
    
    
    print("\n\n")
    print(">> new motion!\n")
    # execute a new motion if available
    if len(motions) == 0: 
        print(acc)
        return len(acc)
    return part1_recursive(motions[1:], head, tail, int(motions[0][1]), motions[0][0], acc)


# driver function
input = get_input("test_input.txt")

print("part 1 recursive:", part1_recursive(input))