def explore_light_path(reflectors, initial_path):
    # light = position, direction
    energiged = set()
    light_paths = [
        initial_path
    ]
    visited = set()
    while light_paths:
        light_path = light_paths.pop()
        current, direction = light_path

        visit = (*current, *direction)
        if visit in visited:
            continue
        visited.add(visit)

        current[0]+=direction[0] 
        current[1]+=direction[1]
        
        
        if not (
        0 <= current[0] < len(reflectors)
        and 0 <= current[1] < len(reflectors[1])
        ):
            continue

        energiged.add(tuple(current))

        reflector = reflectors[current[0]][current[1]] 
        
        match reflector:
            case ".":
                light_paths.append((list(current), direction))
            case "|":
                if direction[1]:
                    light_paths.append((list(current), [1, 0]))
                    light_paths.append((list(current), [-1, 0]))
                else:
                    light_paths.append((list(current), list(direction)))
            case "-":
                if direction[0]:
                    light_paths.append((list(current), [0, 1]))
                    light_paths.append((list(current), [0, -1]))
                else:
                    light_paths.append((list(current), direction))
            case "\\":
                light_paths.append((list(current), [direction[1], direction[0]]))
            case "/":
                light_paths.append((list(current), [-direction[1], -direction[0]]))

    return len(energiged)


def main():
    with open("input.txt") as f:
        reflectors = [
            [j for j in i.strip() ]for i in f
        ]
    
    coverage = []

    for i, _ in enumerate(reflectors):
        coverage.append(
            explore_light_path(
            reflectors,
            [[i, -1], [0, 1]] # Account for first case
        ))
        coverage.append(
            explore_light_path(
            reflectors,
            [[i, len(reflectors)], [0, -1]] # Account for first case
        ))


    for i, _ in enumerate(reflectors[0]):
        coverage.append(
            explore_light_path(
            reflectors,
            [[-1, i], [1, 0]] # Account for first case
        ))
        coverage.append(
            explore_light_path(
            reflectors,
            [[len(reflectors[0]), i], [-1, 0]] # Account for first case
        ))

    print(max(coverage))
if __name__ == "__main__":
    main()