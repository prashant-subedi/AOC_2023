with open("input.txt") as t:
    galaxy_map = t.read().split("\n")

    repeat_colums = []
    repeat_rows = []
    expansion_value = 1_000_000

    for i, _ in enumerate(galaxy_map[0]):
        for j, _ in enumerate(galaxy_map):
            if galaxy_map[j][i] != ".":
                break
        else:
            repeat_colums.append(i)

    for i, row in enumerate(galaxy_map):
        if row == "." * len(row):
            repeat_rows.append(i)

    print(repeat_colums, repeat_rows)


    galaxy_positions = []
    for i, row in enumerate(galaxy_map):
        for j, col in enumerate(row):
            if col == "#":
                galaxy_positions.append((i, j))

    distance = 0
    for index, galaxy in enumerate(galaxy_positions):
        for other_galaxy in galaxy_positions[index+1:]:
            distance += abs(galaxy[1]-other_galaxy[1]) + abs(galaxy[0] - other_galaxy[0])
            for repeat_row in repeat_rows:
                if (repeat_row > galaxy[0]) !=  (repeat_row > other_galaxy[0]):
                    distance+=expansion_value-1
            for repeat_col in repeat_colums:
                if (repeat_col > galaxy[1]) !=  (repeat_col > other_galaxy[1]):
                    distance+=expansion_value-1

    print(distance)