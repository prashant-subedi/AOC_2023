import math
def main():
    map = {}
    with open("input.txt") as f:
        directions = next(f).strip()
        next(f) # Skip
        for line in f:
            key = line[:3]
            left = line[7:10]
            right = line[12:15]
            map[key] = {"L": left, "R": right}

        all_start = [key for key in map if key.endswith("A")]
        all_steps = []
        for current in all_start:
            steps = 0
            while not current[-1] == "Z":
                current = map[current][directions[steps%len(directions)]]
                steps+=1
            print(steps%len(directions) == 0 ) # Sanitiy check for LCM applicable
            all_steps.append(steps)

    print(math.lcm(*all_steps)) # This eneded up working

if __name__ == "__main__":
    main()