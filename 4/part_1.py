def extract_numbers(raw: str) -> set[int]:
    return {int(i) for i in raw.strip().split(" ") if i}


with open("input.txt") as f:
    sum = 0
    for line in f:
        card, rest = line.split(":")
        raw_winning, raw_result = rest.split("|")
        winning_numbers = extract_numbers(raw_winning)
        result_numbers = extract_numbers(raw_result)
        
        overlap = winning_numbers.intersection(result_numbers)
        if overlap:
            sum = sum + 2**(len(overlap) - 1)
print(sum)