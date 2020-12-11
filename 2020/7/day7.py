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


def raw_data_to_dict(data):
    dict_all = {}
    for ln in data:
        raw = ln.split("contain")
        children = raw[1].split(",")
        parent = "-".join(str(raw[0].strip()).split()[:-1])
        children_list = []
        dict_all[parent] = children_list
        for bag_raw in children:
            str_list = bag_raw.split()
            first_str = str_list[0]
            if first_str != "no":
                qty = int(first_str)
                child = "-".join(str_list[1:-1])
                dict_all[parent].append({child: qty})
    return dict_all


def find_possibilities(bags_dict, my_bag, accumulator):
    for parent, children in bags_dict.items():
        for child_dict in children:
            if my_bag in child_dict:
                child_bag = list(child_dict.keys())[0]
                # print(child_bag, "fits in", parent)
                accumulator.add(parent)
                find_possibilities(bags_dict, parent, accumulator)
    return accumulator


raw_data = get_input("input.txt")
bags = raw_data_to_dict(raw_data)
print_bag_capacities(raw_data)
result = find_possibilities(bags, "shiny-gold", set())
print("total:", len(result))
