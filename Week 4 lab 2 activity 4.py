# Author Sana Alyaseri
# Class: software Development
# Example 5: Using Global Variables to Share Data Between Functions

total_sum = 0

def add_to_sum(num):
    global total_sum
    total_sum

def display_sum():
 print(f"Total Sum: {total_sum}")

# Call the functions
add_to_sum(5)
add_to_sum(10)
add_to_sum(20)
display_sum()