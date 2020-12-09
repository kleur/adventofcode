def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def determine_pos(seat_code, pos):
    if 0 == len(seat_code):
        return pos - 1
    # stay
    if seat_code[0] in ["B", "R"]:
        return determine_pos(seat_code[1:], pos)
    # move
    if seat_code[0] in ["F", "L"]:
        move = int(pow(2, len(seat_code)) / 2)
        return determine_pos(seat_code[1:], pos - move)


def to_unique_ids(seat_ids):
    uids = {}
    for seat_id in seat_ids:
        row_seq = seat_id[:7]
        col_seq = seat_id[7:]
        row = determine_pos(row_seq, 128)
        col = determine_pos(col_seq, 8)
        uid = row * 8 + col
        uids[row, col] = uid
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
empty_seat = determine_missing_seat(seats_dict)

print("highest id", unique_seat_ids[-1])
print("my seat", empty_seat)
