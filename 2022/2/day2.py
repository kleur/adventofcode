# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

mapping = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors",
    "X" : "Rock",
    "Y" : "Paper",
    "Z" : "Scissors",
}

defeats = {
    "Rock" : ["Scissors", 1],
    "Paper" : ["Rock", 2],
    "Scissors" : ["Paper", 3]
}

def part1_iterative(raw_rounds):
    total_score = 0
    for raw_round in raw_rounds:
        score = 0
        elf_play = mapping[raw_round[:1]]
        our_play = mapping[raw_round[-1:]]
        
        played = defeats[our_play][1]
        score += played
        
        print(elf_play, "-", our_play)
        if (elf_play == our_play):
            score += 3
            print("draw", 3, score)
        elif (defeats[our_play][0] == elf_play):
            score += 6
            print("win!", played, score)
        else:
            score += 0
            print("Loss", played, score)
        total_score += score
    return total_score

# driver function
input = get_input("input.txt")

print("part 1 iterative:", part1_iterative(input))
#print("part 2 iterative:", part2_iterative(input))