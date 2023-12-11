with open("input.txt") as t:
    map_before_expansion = t.read().split("\n")

    repeat_colums = []
    for i, _ in enumerate(map_before_expansion[0]):
        for j, _ in enumerate(map_before_expansion):
            if map_before_expansion[j][i] != ".":
                break
        else:
            repeat_colums.append(i)

    map_after_expansion = []
    for i in map_before_expansion:
        if i == "." * len(i):
            map_after_expansion.append("." * (len(i) + len(repeat_colums)))
        map_after_expansion.append(
            "".join(
                ".." if index in repeat_colums else j
                for index, j in enumerate(i)
            )
        )

    galaxy_positions = []
    for i, row in enumerate(map_after_expansion):
        for j, col in enumerate(row):
            if col == "#":
                galaxy_positions.append((i, j))

    distance = 0
    for index, galaxy in enumerate(galaxy_positions):
        for other_galaxy in galaxy_positions[index+1:]:
            distance += abs(galaxy[1]-other_galaxy[1]) + abs(galaxy[0] - other_galaxy[0])

    print(distance)