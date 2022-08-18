def falling_circle(
    pattern=[
        [". O ."],
        [". . ."],
        ["X X X"],
    ]
):
    # . é espaço vazio
    # O é bloco móvel
    # X é bloco fixo

    circles_coords = {}

    for row in range(len(pattern)):
        if row == len(pattern) - 1:
            break

        row_list = pattern[row][0].split(" ")
        next_row = pattern[row + 1][0].split(" ")

        circles = row_list.count("O")

        if not circles:
            continue

        for circle in range(circles):
            circles_coords[row_list.index("O")] = row

            if next_row[row_list.index("O")] == "X":
                continue

            if next_row[row_list.index("O")] == "O":
                placed = False
                acc = 2

                while not placed:
                    next_next_row = pattern[row + acc][0].split(" ")

                    if next_next_row[row_list.index("O")] == ".":
                        next_next_row[row_list.index("O")] = "O"
                        pattern[row + acc][0] = " ".join(next_next_row)
                        placed = True
                    elif next_next_row[row_list.index("O")] == "X":
                        break
                    else:
                        acc += 1

                if placed == False:
                    row_list[row_list.index("O")] = "U"
                    continue

            next_row[row_list.index("O")] = "O"
            row_list[row_list.index("O")] = "."

        for obj in row_list:
            if obj == "U":
                row_list[row_list.index(obj)] = "O"

        pattern[row][0] = " ".join(row_list)
        pattern[row + 1][0] = " ".join(next_row)

    return pattern

