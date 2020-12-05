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


def get_input(file):
    with open(file, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines


def find_numbers(expenses, total):
    for num, expense in enumerate(expenses, start=1):
        part = total - expense
        for i in range(num, len(expenses)):
            actual = expenses[i]
            if actual == part:
                return expense * part

expense_report = get_input('input.txt')
print("the answer:", find_numbers(expense_report, 2020))
