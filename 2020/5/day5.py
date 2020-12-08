def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def determine_pos(str, s, e, x):
    if len(str) == 0:
        return s
    cur = str[0]
    x = int(x / 2)
    if cur in ["B", "R"]:
        start = e-x
        print(cur, "upper", [start, e])
        return determine_pos(str[1:], start, e, x)
    if cur in ["F", "L"]:
        end = s+x
        print(cur, "lower", [s, end])
        return determine_pos(str[1:], s, end, x)


def to_unique_ids(seat_ids):
    uids = []
    print()
    for seat_id in seat_ids:
        row_seq = seat_id[:7]
        col_seq = seat_id[7:]
        row = determine_pos(row_seq, 0, 128, 128)
        col = determine_pos(col_seq, 0, 8, 8)
        uid = row * 8 + col
        uids.append(uid)
        print([row, col], uid)
        print()
    return uids


boarding_passes = get_input("input.txt")
unique_seat_id = to_unique_ids(boarding_passes)

unique_seat_id.sort()

print(unique_seat_id[-1])


