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
        self.key_range.append((key, key+range_))
        self.destination_start.append(destination)


def find_final(seed, maps):
    next_value = seed
    for map in maps:
        next_value = maps[map][next_value]
    return next_value


import math

def find_min_for_seed(start, range_, parsed_input) -> int:
    min = math.inf
    for actual_seed in range(start, start + range_):
        final_value = find_final(actual_seed, parsed_input)
        if final_value < min:
            min = final_value
    return min


import concurrent.futures

def main():
    parsed_input = defaultdict(SeedMapper)
    with open("input.txt") as f:
        seeds = [int(i) for i in next(f).strip()[len("seeds: "):].split(" ")]
        current_map = None
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif line.endswith(":"):
                current_map = line
            else:
                destination, source, range_ = [int(i) for i in line.split()]
                parsed_input[current_map][source] = (destination, range_)
                
    from itertools import repeat
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = []
        for result in executor.map(find_min_for_seed, seeds[::2], seeds[1::2], repeat(parsed_input)):
            results.append(result)

    print(min(results))

if __name__ == "__main__":
    main()