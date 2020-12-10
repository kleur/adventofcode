def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def print_bag_capacities(data):
    for ln in data:
        raw = ln.split("contain")
        children = raw[1].split(",")
        parent = "-".join(str(raw[0].strip()).split()[:-1])
        print(">", parent)
        for bag_raw in children:
            str_list = bag_raw.split()
            first_str = str_list[0]
            if first_str == "no":
                print("no bag")
            else:
                child_split = "-".join(str_list[1:-1])
                print("qty:", int(first_str), ":", child_split)
        print()


raw_data = get_input("test_input.txt")
print_bag_capacities(raw_data)
