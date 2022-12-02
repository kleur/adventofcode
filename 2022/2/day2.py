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

mapping2 = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors",
    "X" : "Loss",
    "Y" : "Draw",
    "Z" : "Win",
}

defeats = {
    "Rock" : ["Scissors", 1],
    "Paper" : ["Rock", 2],
    "Scissors" : ["Paper", 3]
}

defeated_by = {
    "Scissors" : ["Rock", 1],
    "Rock" : ["Paper", 2],
    "Paper" : ["Scissors", 3]
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

def part2_iterative(raw_rounds):
    total_score = 0
    for raw_round in raw_rounds:
        score = 0
        elf_play = mapping2[raw_round[:1]]
        directive = mapping2[raw_round[-1:]]
        played = ""
        print(elf_play, "-", directive)
        if (directive == "Loss"):
            print("Should lose from", elf_play)
            played = defeats[elf_play][0]
            score += 0
        if (directive == "Draw"):
            print("Should draw to", elf_play)
            played = elf_play
            score += 3
        if (directive == "Win"):
            print("Should win from", elf_play)
            played = defeated_by[elf_play][0]
            score += 6
        print("played", played)
        score += (defeats[played][1])
        total_score += score
    return total_score



# driver function
input = get_input("input.txt")

#print("part 1 iterative:", part1_iterative(input))
print("part 2 iterative:", part2_iterative(input))