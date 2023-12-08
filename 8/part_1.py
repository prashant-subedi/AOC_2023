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

        current = "AAA"
        steps = 0
        while current!="ZZZ":
            current = map[current][directions[steps%len(directions)]]
            steps+=1

        print(steps)



if __name__ == "__main__":
    main()