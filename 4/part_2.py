def extract_numbers(raw: str) -> set[int]:
    return {int(i) for i in raw.strip().split(" ") if i}

from collections import defaultdict
max_game_no = 0
with open("input.txt") as f:
    card_exec_count = defaultdict(lambda: 1)
    for idx, line in enumerate(f):
        max_game_no+=1
        _, rest = line.split(":")

        raw_winning, raw_result = rest.split("|")
        winning_numbers = extract_numbers(raw_winning)
        result_numbers = extract_numbers(raw_result)
        
        for i, _ in enumerate(winning_numbers.intersection(result_numbers)):
            card_exec_count[idx+i+1]+=card_exec_count[idx]
print(card_exec_count)
print(max_game_no)

count = 0
for i in range(max_game_no):
    count+=card_exec_count[i]
print(count)