# Find the two entries that sum to 2020; what do you get if you multiply them together?


def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


for line in get_input('test_input.txt'):
    print(line)
