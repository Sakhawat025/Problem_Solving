def calculate_move(r, c):
    row_index = r + 1
    col_index = c + 1

    return abs(row_index - 3) + abs (col_index - 3)

if __name__ == "__main__":
    row_pos = -1
    col_pos = -1

    for r in range(5):
        row = list(map(int, input().split()))

        if 1 in row:
            row_pos = r
            col_pos = row.index(1)

    res = calculate_move(row_pos, col_pos)
    print(res)