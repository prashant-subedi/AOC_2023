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
    time = int(times_raw[len("Time:      "):].replace(" ", ""))
    distance_raw = next(t)
    distance = int(distance_raw[len("Distance:  "):].replace(" ", ""))
    print(find_ways(time, distance))

