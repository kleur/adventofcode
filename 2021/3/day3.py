# get the input
def get_input(file):
    with open(file, 'r') as f:
        lines = [[int(char) for char in line.strip()] for line in f]
    return lines

# helper
def to_decimal(int_byte_array):
    byte_str = "".join([str(i) for i in int_byte_array])
    return int(byte_str, 2)

# part 1
def part1_iteration(numbers, bit):
    # count occurrences, for example [7, 5, 8, 7, 5]
    tally = [sum(x) for x in zip(*numbers)]
    # comparing boolean (is most prevalent?) to int (bit we're looking for)
    byte = [int((count * 2 > len(numbers)) == bit) for count in tally]
    return to_decimal(byte)

# part 2
def part2_iteration(numbers, criteria):
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
    
# driver function
input = get_input("test_input.txt")
print("part 1 iterative:", part1_iteration(input, 0) * part1_iteration(input, 1))
print("part 2 iterative:", part2_iteration(input, 0) * part2_iteration(input, 1))