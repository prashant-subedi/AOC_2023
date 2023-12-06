from collections import defaultdict

class SeedMapper:
    def __init__(self) -> None:
        self.key_range = []
        self.destination_start = []

    def __getitem__(self, key: int):
        for i, (source_start, source_end) in enumerate(self.key_range):
            if source_start <= key < source_end:
                return self.destination_start[i] + (key - source_start)
        return key

    def __setitem__(self, key, value: tuple[int, int]):
        destination, range_ = value
        self.key_range.append((key, source+range_))
        self.destination_start.append(destination)

def find_final(seed, maps):
    next_value = seed
    for map in maps:
        next_value = maps[map][next_value]
    return next_value

parsed_input = defaultdict(SeedMapper)
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
            parsed_input[current_map][source] = (destination, range_)

all_final = []
for seed in seeds:
    all_final.append(find_final(seed, parsed_input))

print(min(all_final))