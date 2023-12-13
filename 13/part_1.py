import re

def find_row_colum(pattern):
    # Check columns
    column_length = len(pattern[0])
    for col in range(1, column_length):
        start, stop = 0, column_length
        if col <= column_length//2:
            stop = 2*col
        else:
            start = 2*col - column_length
        for i in pattern:
            if i[start: col] != i[col: stop][::-1]:
                break
        else:
            return 0, col
    
    # Check rows
    for row in range(1, len(pattern)):
        row_length = len(pattern)
        start, stop = 0, row_length
        if row <= row_length//2:
            stop = 2 * row
        else:
            start = 2 * row - row_length
        if pattern[start: row] == pattern[row: stop][::-1]:
            return row, 0
            
    return 0, 0 

with open("input.txt") as f:
    x = re.split("\n\n", f.read())
    total = 0
    for idx, raw_pattern in enumerate(x):
        pattern  = raw_pattern.split("\n")
        row, col = find_row_colum(pattern)
        total += row * 100 + col

print(total)