def rotate_90(platform):
    return [
        [
           platform[row_idx][col_idx] for row_idx in range(len(platform)-1, -1, -1)
        ] for col_idx in range(len(platform[1]))
    ]

def cycle(platform):
    for i in range(4):
        for row_idx, row in enumerate(platform): 
            for col_idx, col in enumerate(row):
                if col!="O":
                    continue
                current_idx = row_idx
                while current_idx > 0 and platform[current_idx-1][col_idx] == ".":
                    current_idx-=1
                platform[row_idx][col_idx] = "."
                platform[current_idx][col_idx] = "O"
        platform = rotate_90(platform)
    return platform

def calculate_value(platform):
    total = 0
    for idx, row in enumerate(reversed(platform)):
        for col in row:
            if col == "O":
                total+=(idx+1)
    return total

def platform_to_str(platform):
    return "\n".join(
        "".join(row) for row in platform
    )

with open("input.txt") as t:
    platform = list([[j for j in i.strip()] for i in t])
    print(calculate_value(platform))
    platforms = []
    platform_value = {}
    for i in range(1000000000):
        platform_str = platform_to_str(platform)
        if  platform_str in platforms:
            break
        platform_value[platform_str] = calculate_value(platform) 
        platforms.append(platform_str)
        platform = cycle(platform)
    cycle_start = platforms.index(platform_str)
    print(f"{cycle_start=}")
    cycle_length =  i - cycle_start
    print(f"{cycle_length=}")
    index =   cycle_start + (1000000000 - cycle_start) % cycle_length
    print(f"{index=}")
    print(platform_value.values())
    print(platform_value[platforms[index]])
