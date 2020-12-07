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


# Helper function
def multiply_elements(selection):
    result = 1
    for expense in selection:
        result = result * expense
    return result


def find_numbers_loops(expenses, total):
    for num, expense in enumerate(expenses, start=1):
        part = total - expense
        for i in range(num, len(expenses)):
            actual = expenses[i]
            if actual == part:
                print("found", expense, "and", part, "product", expense * part)
                return expense * part


def find_numbers_recursive(slots, selection, nums, target):
    if len(nums) == 0 or slots == 0:
        if slots == 0 and target == 0:
            print("found", selection, "product",  multiply_elements(selection))
        return target == 0

    if target == 0:
        return slots == 0

    if target < 0:
        return False

    num = nums[0]

    is_chosen = find_numbers_recursive(slots - 1, selection + [num], nums[1:], target - num)
    not_chosen = find_numbers_recursive(slots, selection, nums[1:], target)

    return is_chosen or not_chosen


# Driver program to test above function
expenses = get_input('input.txt')
expenses.sort(reverse=True)

find_numbers_loops(expenses, 2020)
find_numbers_recursive(3, [], expenses, 2020)
