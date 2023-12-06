def check_if_neighbour_symbol(grid, i, j):
    positions = (
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1), (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    )
    for x, y in positions:
        if x <0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
            continue
        elif grid[x][y].isdigit() or grid[x][y] == ".":
            continue
        else:
            return True
    return False

def find_total_engine_part_sum(grid):
    sum = 0
    number = []
    is_engine_part = False
    
    count = 0
    numbers = []

    for i, line in enumerate(grid):
        for j, c in enumerate(line + " "):
            if c.isdigit():
                number.append(c)
                if not is_engine_part:
                    is_engine_part = check_if_neighbour_symbol(grid, i, j)
            
            elif number:
                count+=1
                numbers.append(int("".join(number)))
                if is_engine_part:
                    sum+=int("".join(number))
                    is_engine_part = False
                else:
                    print("Line", i, number)
                number = []

    return sum



        
with open("input.txt") as f:
    
    grid = list(i[:-1] for i in f)

    sum = find_total_engine_part_sum(grid)

    print(sum)
    
