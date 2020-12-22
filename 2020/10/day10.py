def get_input(file):
    with open(file, 'r') as f:
        lines = [int(line.strip()) for line in f]
    return lines


def loop_connect(adapters):
    for a in adapters:
        print(a)


def rec_connect(adapters, n, inp_rating, diffs):
    eff_max = inp_rating + 3
    if n == len(adapters):
        diff = eff_max - inp_rating
        diffs[diff] += 1
        return diffs[1] * diffs[3]
    cur = adapters[n]
    diff = cur - inp_rating
    diffs[diff] += 1
    return rec_connect(adapters, n + 1, cur, diffs)


def connect_adapters(adapters):
    diffs = {1: 0, 2: 0, 3: 0}
    return rec_connect(adapters, 0, 0, diffs)


def rec_find_paths(adapters, n, rating):
    if n == len(adapters):
        return 1
    current_adapter = adapters[n]
    diff_left = rating - current_adapter
    if diff_left > 0:
        do_choose = rec_find_paths(adapters, n + 1, current_adapter + 3)
        not_choose = rec_find_paths(adapters, n + 1, rating)
        return do_choose + not_choose
    if diff_left == 0:
        do_choose = rec_find_paths(adapters, n + 1, current_adapter + 3)
        return do_choose
    return 0


def find_paths(adapters):
    return rec_find_paths(adapters, 0, 3)


data = get_input("test_input.txt")
data.sort()
print(connect_adapters(data))
print(find_paths(data))
