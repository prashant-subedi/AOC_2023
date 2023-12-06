with open("input.txt") as t:
    sum=0
    for line in t:
        number = 0
        for char in line:
            if char.isdigit():
                number += 10*int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                number += int(char)
                break
        sum+=number
print(sum)