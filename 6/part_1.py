import math

def find_ways(time, distance):
    
    first = math.floor((time + math.sqrt(time**2-4*distance))/2)
    second = math.floor(((time - math.sqrt(time**2-4*distance))/2))
    if second * (time - second) == distance: # Edge case
        return first - second - 1
    return first -  second
 
times, distances = [], []
with open("input.txt") as t:
    times_raw = next(t)
    times = [
        int(i) for i in times_raw[len("Time:      "):].split(" ")
        if i
    ]
    distances_raw = next(t)
    distances = [
        int(i) for i in distances_raw[len("Distance:  "):].split(" ")
        if i
    ]
mult = 1
for time, distance in zip(times, distances):
    mult *= find_ways(time, distance)

print(mult)