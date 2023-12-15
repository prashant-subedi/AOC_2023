with open("input.txt") as t:
    platform = list([[j for j in i.strip()] for i in t])

for row_idx, row in enumerate(platform): 
    for col_idx, col in enumerate(row):
        if col!="O":
            continue
        current_idx = row_idx
        while current_idx > 0 and platform[current_idx-1][col_idx] == ".":
            current_idx-=1
        platform[row_idx][col_idx] = "."
        platform[current_idx][col_idx] = "O"

total = 0
for idx, row in enumerate(reversed(platform)):
    for col in row:
        if col == "O":
            total+=(idx+1)
    

print(total)