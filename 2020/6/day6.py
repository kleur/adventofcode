def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def sum_of_questions_anyone(raw_lines):
    count = 0
    current_set = set()
    for i in range(0, len(raw_lines)):
        if raw_lines[i] != "":
            for c in raw_lines[i]:
                current_set.add(c)
        if raw_lines[i] == "" or i == len(raw_lines) - 1:
            count += len(current_set)
            current_set = set()
    return count


def sum_of_questions_everyone_recursive(group, prev):
    if len(group) == 0:
        return len(prev)
    nxt = ""
    for c in group[0]:
        if c in prev:
            nxt += c
    return sum_of_questions_everyone_recursive(group[1:], nxt)


def sum_of_questions_everyone(raw_lines):
    total = 0
    current_list = []
    for i in range(0, len(raw_lines)):
        if raw_lines[i] != "":
            current_list.append(raw_lines[i])
        if raw_lines[i] == "" or i == len(raw_lines) - 1:
            total += sum_of_questions_everyone_recursive(current_list[1:], current_list[0])
            current_list = []
    return total


raw_input_lines = get_input("input.txt")
print("sum of questions answered by anyone in group:", sum_of_questions_anyone(raw_input_lines))
print("sum of questions answered by everyone in group:", sum_of_questions_everyone(raw_input_lines))