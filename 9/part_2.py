def find_next(history: int) -> int: 
    current = history
    sequences = [history]
    while any(current):
        current = [i-j for i, j in zip(current[1:], current)]
        sequences.append(current)
    
    added_number = 0
    for sequence in reversed(sequences[:-1]):
        added_number =  sequence[0] - added_number

    return added_number

sum = 0

with open("input.txt") as f:
    for line in f:
        sum += find_next([int(i) for i in line.split()])
print(sum)


