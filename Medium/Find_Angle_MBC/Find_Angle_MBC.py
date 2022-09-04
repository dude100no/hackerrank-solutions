import math

AB = int(input())
BC = int(input())

MC = math.sqrt((AB ** 2) + (BC ** 2))

angle = math.degrees(math.atan(AB / BC))

print(angle, round(angle))