#calculate the area of the c shape pacman
import math 
def area_of_c_shape_pacman(radius, angle):
    # Calculate the area of the full circle
    full_circle_area = math.pi * radius ** 2
    #radius = 8
    
    # Calculate the area of the sector (the "mouth" of the pacman)
    sector_area = (angle / 360) * full_circle_area
    
    # The area of the c shape pacman is the area of the full circle minus the area of the sector
    c_shape_area = full_circle_area - sector_area
    
    return c_shape_area  
print(area_of_c_shape_pacman(8, 45))