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
    uids = {}
    for seat_id in seat_ids:
        row_seq = seat_id[:7]
        col_seq = seat_id[7:]
        row = determine_pos(row_seq, 0, 128, 128)
        col = determine_pos(col_seq, 0, 8, 8)
        uid = row * 8 + col
        uids[row, col] = uid
        print()
    return uids


def determine_missing_seat(seats):
    my_seat = " "
    for row in range(0, 128):
        cols = []
        for col in range(0, 8):
            if (row, col) in seats:
                seat = seats[(row, col)]
                if seat < 100:
                    cols.append(" " + str(seat))
                else:
                    cols.append(str(seat))
            else:
                uid = row * 8 + col
                if uid + 1 in seats.values() and uid - 1 in seats.values():
                    my_seat = uid
                cols.append("   ")
        print(cols)
    return my_seat


boarding_passes = get_input("input.txt")
seats_dict = to_unique_ids(boarding_passes)
unique_seat_ids = list(seats_dict.values())
unique_seat_ids.sort()
print("highest id", unique_seat_ids[-1])
print("my seat", determine_missing_seat(seats_dict))
