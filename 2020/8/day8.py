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


def run_rec1(operations, n, acc):
    if n not in operations:
        return acc
    else:
        cur = operations[n]
        del operations[n]
        if cur["op"] == "nop":
            return run_rec1(operations, n + 1, acc)
        if cur["op"] == "acc":
            return run_rec1(operations, n + 1, acc + cur["arg"])
        if cur["op"] == "jmp":
            return run_rec1(operations, n + cur["arg"], acc)


def run_rec2(operations, n, acc, executed):
    if n == len(operations):
        return [acc]
    if n in executed:
        return []
    executed.add(n)
    cur = operations[n]
    if cur["op"] == "nop":
        return run_rec2(operations, n + 1, acc, executed)
    if cur["op"] == "acc":
        return run_rec2(operations, n + 1, acc + cur["arg"], executed)
    if cur["op"] == "jmp":
        return run_rec2(operations, n + cur["arg"], acc, executed)


def fix_program(opz):
    final_result = 0
    for n in range(0, len(opz)):
        cur = opz[n]
        if cur["op"] == "nop":
            res2 = []
            if cur["arg"] < 0 or cur["arg"] > 0:
                ops_copy3 = opz.copy()
                ops_copy3[n] = {"op": "jmp", "arg": cur["arg"]}
                res2 = run_rec2(ops_copy3, 0, 0, set())
            if len(res2) > 0:
                final_result = res2[0]
        if cur["op"] == "jmp":
            ops_copy4 = opz.copy()
            ops_copy4[n] = {"op": "nop", "arg": cur["arg"]}
            res2 = run_rec2(ops_copy4, 0, 0, set())
            if len(res2) > 0:
                final_result = res2[0]
    return final_result


data = get_input("input.txt")
print("accumulator at start of infinite loop", run_rec1(to_operations(data), 0, 0))
print("accumulator at end of (fixed) program", fix_program(to_operations(data)))
