from collections import defaultdict

def hash(string):
    current = 0
    for char in string:
        current += ord(char)
        current*=17
        current%=256
    return current

with open("input.txt") as t:
    boxes = defaultdict(dict)

    input_sequence = t.read().split(",")
    total = 0
    for string in input_sequence:
        last_char = string[-1]
        if last_char == "-":
            label = string[:-1]
        else:
            label = string[:-2]
            focal_length = int(string[-1])

        hash_value=hash(label)
        box = boxes[hash_value]

        if last_char == "-":
            if label in box:
                del box[label]
        else:
            box[label] = focal_length

total = 0
for box_no, box in boxes.items():
    box_total = 0
    for lens_no, focal_length in enumerate(box.values()):
        box_total+=(box_no+1)*(lens_no+1) *(focal_length)
    total+=box_total
print(total)