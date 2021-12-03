# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [[int(char) for char in line.strip()] for line in f]
    return lines

# helper
def to_str(int_byte_array):
    byte = [str(i) for i in int_byte_array]
    return "".join(byte)
    
def to_decimal(int_byte_array):
    byte_str = to_str(int_byte_array)
    return int("".join(byte_str), 2)

# iteration
def part1_iteration(numbers):
    half = len(numbers) / 2
    
    # count occurrence of 1
    tally = [sum(bit) for bit in zip(*numbers)]
    
    # to binary
    gamma_byte = [1 if count > half else 0 for count in tally]
    epsilon_byte = [0 if count > half else 1 for count in tally]
    
    # join string & convertical to decimal
    gamma = to_decimal(gamma_byte)
    epsilon = to_decimal(epsilon_byte)
    
    # multiply
    return gamma * epsilon

def find(numbers, criteria):
    # loop over position
    for x in range(len(numbers[0])):
        
        # sum the bits in this vertical position
        vertical_sum = sum([line[x] for line in numbers])
        
        # this is False if there's less 0 than 1
        more_1 = vertical_sum * 2 >= len(numbers)
        
        # here we switch by criteria, as True == 1
        match = more_1 == criteria
        
        # filter the numbers
        numbers = filter(lambda line: line[x] == match, numbers) 
        
        # quit the loop and return if there's only one left
        if len(numbers) == 1:
            return to_decimal(numbers[0])

def part2_iteration(numbers):
    return find(numbers, 1) * find(numbers, 0)
    
# driver function
input = get_input("test_input.txt")
print("part 1 iterative:", part1_iteration(input))
print("part 2 iterative:", part2_iteration(input))