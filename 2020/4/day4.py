import re


def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def birth_year_valid(year):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return len(year) == 4 and year.isnumeric() and 1920 <= int(year) <= 2002


def issue_year_valid(year):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return len(year) == 4 and year.isnumeric() and 2010 <= int(year) <= 2020


def exp_year_valid(year):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return len(year) == 4 and year.isnumeric() and 2020 <= int(year) <= 2030


def height_valid(height):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if len(height) > 2:
        height_unit = height[-2:]
        height_str = height[:-2]
        if height_str.isnumeric():
            height_num = int(height_str)
            if height_unit == "cm":
                return 150 <= height_num <= 193
            if height_unit == "in":
                return 59 <= height_num <= 76
    return False


def hair_color_valid(color):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hex_regex = "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$"
    return re.match(hex_regex, color)


def eye_color_valid(color):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    valid_colors = 'amb blu brn gry grn hzl oth'.split()
    return color in valid_colors


def passport_id_valid(id):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return len(id) == 9 and id.isnumeric()


def country_id_valid(id):
    # cid (Country ID) - ignored, missing or not.
    return True


def create_validator():
    return {
        'byr': birth_year_valid,
        'iyr': issue_year_valid,
        'eyr': exp_year_valid,
        'hgt': height_valid,
        'hcl': hair_color_valid,
        'ecl': eye_color_valid,
        'pid': passport_id_valid
    }


def is_valid_pt1(passport, validator):
    for mandatory_field in validator.keys():
        if mandatory_field not in passport:
            return False
    return True


def is_valid_pt2(passport, validator):
    for mandatory_field in validator.keys():
        if mandatory_field not in passport:
            return False
        else:
            valid = validator[mandatory_field](passport[mandatory_field])
            if not valid:
                return False

    return True


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
                for key_val in [k.split(":") for k in x.split()]:
                    key = key_val[0]
                    val = key_val[1]
                    current_dict[key] = val
            passports += [current_dict]
            current_raw = []
            current_dict = {}
        i += 1
    return passports


def count_valid(passports, validator, flag):
    count = 0
    for p in passports:
        valid = False
        for i in p.items():
            print(i)
        if flag == "part1" and is_valid_pt1(p, validator):
            valid = True
            count += 1
        if flag == "part2" and is_valid_pt2(p, validator):
            valid = True
            count += 1
        print("Valid:", valid, "\n")
    return count


all_passports = to_passports(get_input("input.txt"))
print(count_valid(all_passports, create_validator(), "part2"))
