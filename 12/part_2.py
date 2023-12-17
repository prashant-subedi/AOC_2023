from functools import cache

@cache
def count(report, redudancy):
    if not report:
        return 1 if len(redudancy) == 0 else 0
    if not redudancy:
        return 0 if "#" in report else 1

    number_of_ways = 0
    
    if report[0] in ".?":
        number_of_ways+=count(report[1:], redudancy)

    next_hash = redudancy[0]
    if report[0] in "#?":
        if len(report)>=next_hash and "." not in report[:next_hash]:
            if next_hash < len(report):
                if report[next_hash]!="#":
                    number_of_ways+=count(report[next_hash+1:] , redudancy[1:])
            else:
                number_of_ways+=count(report[next_hash:] , redudancy[1:])

    return number_of_ways

total = 0
with open("input.txt") as f:
    for line in f:
        report, redundancy_raw = line.split()
        redundancy = tuple((int(i) for i in redundancy_raw.split(",")))
        total+=count("?".join([report] * 5), tuple(i for _ in range(5) for i in redundancy))

print(total)