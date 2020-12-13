def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def to_operations(raw_data):
    operations = {}
    for n in range(0, len(raw_data)):
        item = raw_data[n].split()
        operations[int(n)] = {"op": item[0], "arg": int(item[1])}
    return operations


def run_rec(operations, n, acc):
    if n not in operations:
        return acc
    else:
        cur = operations[n]
        if cur["op"] == "nop":
            pass
        if cur["op"] == "acc":
            acc += cur["arg"]
        if cur["op"] == "jmp":
            del operations[n]
            return run_rec(operations, n + cur["arg"], acc)
        del operations[n]
        return run_rec(operations, n + 1, acc)


data = get_input("input.txt")
ops = to_operations(data)

result = run_rec(ops, 0, 0)
print(result)