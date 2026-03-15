# Author Sana Alyaseri
# Class: software Development
# Example 4: Accessing a Global Variable
count = 0
def increment():
 global count # Declare 'count' as global
count += 1
print(f"Count inside function: {count}")

# Call the function
increment()
increment ()

# Access the global variable
print(f"Count outside function: {count}")