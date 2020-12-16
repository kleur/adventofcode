def get_input(file):
    with open(file, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines


def find_numbers_recursive(slots, nums, target):
    if len(nums) == 0 or slots == 0:
        return target == 0
    if target == 0:
        return slots == 0
    if target < 0:
        return False
    num = nums[0]
    is_chosen = find_numbers_recursive(slots - 1, nums[1:], target - num)
    not_chosen = find_numbers_recursive(slots, nums[1:], target)
    return is_chosen or not_chosen


def group_sum(nums, target, selection):
    if len(nums) == 0:
        return target == 0
    if target == 0:
        selection.sort()
        if len(selection) > 1:
            print(selection[0] + selection[-1])
        return True
    if target < 0:
        return False
    num = nums[0]
    return group_sum(nums[1:], target - num, selection + [num])


def find_first_number(nums, preamble, consider):
    for n in range(len(nums)):
        if n >= preamble:
            adds_up = find_numbers_recursive(2, nums[n - consider: n], nums[n])
            if not adds_up:
                for x in range(len(nums)):
                    group_sum(nums[x:], nums[n], [])
                return nums[n]


# print(find_first_number(get_input("test_input.txt"), 5, 5))
print(find_first_number(get_input("input.txt"), 25, 25))
