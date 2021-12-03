# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [[int(char) for char in line.strip()] for line in f]
    return lines

# iteration
def part1_iteration(numbers):
    half = len(numbers) / 2
    
    # count occurrence of 1
    tally = [sum(bit) for bit in zip(*numbers)]
    
    # to binary
    gamma_byte = ["1" if count > half else "0" for count in tally]
    epsilon_byte = ["0" if count > half else "1" for count in tally]
    
    # join string & convert to decimal
    gamma = int("".join(gamma_byte), 2)
    epsilon = int("".join(epsilon_byte), 2)
    
    # multiply
    return gamma * epsilon
    
# driver function
input = get_input("test_input.txt")
print("part 1 iterative:", part1_iteration(input))