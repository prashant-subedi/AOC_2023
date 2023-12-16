def hash(string):
    current = 0
    for char in string:
        current += ord(char)
        current*=17
        current%=256
    return current

with open("input.txt") as t:
    input_sequence = t.read().split(",")
    total = 0
    for string in input_sequence:
        total+=hash(string)
    print(total)