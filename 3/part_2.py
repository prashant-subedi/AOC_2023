from collections import defaultdict

def neighbouring_starts(grid, i, j):
    positions = (
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1), (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    )
    neighbouring_starts = []
    for x, y in positions:
        if x <0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
            continue
        elif grid[x][y] == "*":
            neighbouring_starts.append((x, y))

    return neighbouring_starts

def find_total_engine_part_sum(grid):
    number = []
    star_part_number = defaultdict(list)
    neignboarding_star_coordinates = set()
     
    for i, line in enumerate(grid):
        for j, c in enumerate(line + " "):
            if c.isdigit():
                number.append(c)
                for star_coor in neighbouring_starts(grid, i, j):
                    neignboarding_star_coordinates.add(star_coor)
            
            elif number:
                for neigboring_star in neignboarding_star_coordinates:
                    star_part_number[neigboring_star].append(int("".join(number)))
                number = []
                neignboarding_star_coordinates = set()
    sum = 0
    for i, j in star_part_number.items():
        if len(j) == 2:
            sum+=(j[0]*j[1])
    print(sum)




        
with open("input.txt") as f:
    
    grid = list(i[:-1] for i in f)

    sum = find_total_engine_part_sum(grid)

    print(sum)
    
