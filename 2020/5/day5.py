def get_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
    return lines


def determine_pos(seat_code, n, pos):
    if n == len(seat_code):
        return pos - 1
    move = int(pow(2, len(seat_code) - n) / 2)
    if seat_code[n] in ["B", "R"]:
        # stay
        return determine_pos(seat_code, n + 1, pos)
    if seat_code[n] in ["F", "L"]:
        # move
        return determine_pos(seat_code, n + 1, pos - move)


def to_unique_ids(seat_ids):
    uids = {}
    for seat_id in seat_ids:
        row_seq = seat_id[:7]
        col_seq = seat_id[7:]
        row = determine_pos(row_seq, 0, 128)
        col = determine_pos(col_seq, 0, 8)
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
