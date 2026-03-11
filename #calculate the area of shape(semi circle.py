#calculate the area of shape(semi circle and triangle) and print the result
import math
# value
e = 5
f = 8
g = 10
# semi circle area
semi_circle_area = (math.pi * (e/2)**2) / 2
# triangle area
triangle_area = (1/2) * f * g
# total area
total_area = semi_circle_area + triangle_area
print(f"The total area of the shape is: {total_area}")