# Find the two entries that sum to 2020; what do you get if you multiply them together?
#
# 1721 *
# 979
# 366
# 299 *
# 675
# 1456
#
# In this list, the two entries that sum to 2020 are 1721 and 299.
# Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.


# Get data from file
def get_input(file):
    with open(file, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines


def find_numbers_loops(expenses, total):
    for num, expense in enumerate(expenses, start=1):
        part = total - expense
        for i in range(num, len(expenses)):
            actual = expenses[i]
            if actual == part:
                print("found", expense, "and", part, "product", expense * part)
                return expense * part


def find_numbers_recursive(array, n):
    if n > 0:
        first = array[0]
        last = array[n - 1]
        target = 2020 - first
        # print("*", array, "first", first, "last", last, "target", target)
        if last == target:
            print("found", first, "and", last, "product", first * last)
        if last > target:
            find_numbers_recursive(array[1:], n - 1)
        if last < target:
            find_numbers_recursive(array, n - 1)


# Driver program to test above function
expenses = get_input('input.txt')
expenses.sort(reverse=True)

find_numbers_loops(expenses, 2020)
find_numbers_recursive(expenses, len(expenses))
