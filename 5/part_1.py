from collections import defaultdict

def find_final(seed, maps):
    next_value = seed
    for map in maps:
        next_value = maps[map].get(next_value, next_value)
    return next_value

parsed_input = defaultdict(dict)
with open("input.txt") as f:
    seeds = [int(i) for i in next(f).strip()[len("seeds: "):].split(" ")]
    current_map = None
    for line in f:
        line = line.strip()
        if not line:
            continue
        elif line.endswith(":"):
            print(current_map)
            current_map = line
        else:
            destination, source, range_ = [int(i) for i in line.split()]
            for i in range(range_):
                parsed_input[current_map][source+i] = destination+i

all_final = []
for seed in seeds:
    all_final.append(find_final(seed, parsed_input))

print(min(all_final))