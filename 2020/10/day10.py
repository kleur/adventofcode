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
        # print("input rating:", inp_rating, "effectively:", eff_max, "adapter:", eff_max, "diff", diff)
        print(diffs)
        print("device rating", eff_max)
        return diffs[1] * diffs[3]
    cur = adapters[n]
    diff = cur - inp_rating
    diffs[diff] += 1
    # print("input rating:", inp_rating, "effectively:", eff_max, "adapter:", cur, "diff", diff)
    return rec_connect(adapters, n + 1, cur, diffs)


def connect_adapters(adapters):
    diffs = {1: 0, 2: 0, 3: 0}
    return rec_connect(adapters, 0, 0, diffs)


data = get_input("input.txt")
data.sort()
print(connect_adapters(data))
