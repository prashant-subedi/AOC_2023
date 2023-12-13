import re
from tqdm import tqdm

def find_row_colum(pattern, skip_row=0, skip_col=0):
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
            if col!=skip_col:
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
            if row!=skip_row:
                return row, 0
            
    return 0, 0 

with open("input.txt") as f:
    x = re.split("\n\n", f.read())
    total = 0
    for idx, raw_pattern in enumerate(tqdm(x)):
        pattern  = [list(i) for i in raw_pattern.split("\n")]
        o_r, o_c = find_row_colum(pattern)
        found = False
        for row_idx, row in enumerate(pattern):
            for col_idx, col in enumerate(row):
                current_value = col
                pattern[row_idx][col_idx] = "." if col == "#" else "#"  
                r, c = find_row_colum(pattern, o_r, o_c)
                pattern[row_idx][col_idx] = current_value
                if (r or c):
                    total += r * 100 + c
                    found = True
                    break
            if found:
                break
print(total)