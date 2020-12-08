def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def to_passports(raw_lines):
    passports = []
    current_raw = []
    current_dict = {}
    i = 0
    while i < len(raw_lines):
        if raw_lines[i] != "":
            current_raw += [raw_lines[i]]
        if raw_lines[i] == "" or i == len(raw_lines) - 1:
            for x in current_raw:
                props = x.split()
                for pp in props:
                    key_val = pp.split(":")
                    key = key_val[0]
                    val = key_val[1]
                    current_dict[key] = val
            passports += [current_dict]
            current_raw = []
            current_dict = {}

        i += 1
    return passports


def count_valid(passports):
    count = 0
    for p in passports:
        for i in p.items():
            print(i)
        fields = list(p.keys())
        fields.sort()
        if "cid" in fields:
            fields.remove("cid")
        valid_example = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
        valid = len(fields) >= 7 and fields[:7] == valid_example
        print("valid", valid, "\n")
        if valid:
            count += 1
    return count


all_passports = to_passports(get_input("input.txt"))
print(count_valid(all_passports))