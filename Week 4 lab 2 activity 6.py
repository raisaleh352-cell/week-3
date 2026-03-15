# Author Sana Alyaseri
# Class: software Development
# Example 6: functions where one function calls another to take the result and do further processing.

def add(a, b):
 return a + b

def multiply(x, y):
   return x * y

def add_and_multiply(a, b, c):
   sum_result = add(a, b) # Calling the add function
   product_result = multiply(sum_result, c) # Calling the multiply function
   return product_result
result = add_and_multiply(7, 8, 9)
print(result)

# Output: 135