import math

def get_triangle_area(d, e):
    # calculate the height using pythagorean theorem
    # Step 1: Calculate the vertical height using Pythagoras
    height = math.sqrt(e**2 - d**2)
    # Step 2: Calculate the area
    area = 0.5 * d * height
    return area
#example value given
d = 10
e = 16

print("The area of the given shape is", (get_triangle_area(d, e)))
