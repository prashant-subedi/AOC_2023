import re
digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
reversed_digits = {
    name: i + 1 for i, name  in enumerate(digits)
}
i =0 
regex = re.compile("|".join(f"(?:{i})" for i in digits) + r"|\d")
reversed_regex = re.compile("|".join(f"(?:{i[::-1]})" for i in digits) + r"|\d")

print(regex)

print(reversed_regex)

with open("input.txt") as t:
    sum=0
    for line in t:
        i+=1
        first_matched = regex.search(line).group()
        last_matched =  reversed_regex.search(line[::-1]).group()

        first = int(reversed_digits.get(first_matched, first_matched))
        last = int(reversed_digits.get(last_matched[::-1], last_matched))

        
        sum += first * 10+last
        print(line[:-1], first * 10+last)
print(sum)