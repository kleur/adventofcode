def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def parse_line(line):
    parts = line.split(":")
    policy = parts[0]
    policy_parts = policy.split()
    glyph = policy_parts[1]
    nums = policy_parts[0].split("-")
    num1 = int(nums[0])
    num2 = int(nums[1])
    password = parts[1].strip()
    return num1, num2, glyph, password


def is_valid_pt1(min_occ, max_occ, glyph, password):
    if len(password) == 0:
        return min_occ <= 0 <= max_occ

    if max_occ < 0:
        return False

    cur = password[0]
    if cur == glyph:
        return is_valid_pt1(min_occ - 1, max_occ - 1, glyph, password[1:])
    else:
        return is_valid_pt1(min_occ, max_occ, glyph, password[1:])


def is_valid_pt2(pos, glyph, password, n):
    if n > len(password) or (len(pos) > 0 and n > pos[-1]):
        return len(pos) == 1

    cur = password[n - 1]

    if glyph == cur:
        if n in pos:
            pos.remove(n)

    return is_valid_pt2(pos, glyph, password, n + 1)


def run_pt1(lines):
    count = 0
    for line in lines:
        num1, num2, glyph, password = parse_line(line)
        valid = is_valid_pt1(num1, num2, glyph, password)
        if valid:
            count += 1
    return count


def run_pt2(lines):
    count = 0
    for line in lines:
        num1, num2, glyph, password = parse_line(line)
        valid = is_valid_pt2([num1, num2], glyph, password, 1)
        if valid:
            count += 1
    return count


print("valid for sled rental policy", run_pt1(get_input("input.txt")))
print("valid for Toboggan policy", run_pt2(get_input("input.txt")))
