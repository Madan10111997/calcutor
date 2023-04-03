def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Get user input
num1 = int(input("Enter first number:10 "))
num2 = int(input("Enter second number:20 "))

# Perform calculations
result_add = add(num1, num2)
result_subtract = subtract(num1, num2)
result_multiply = multiply(num1, num2)

# Print results
print(f"{num1} + {num2} = {result_add}")
print(f"{num1} - {num2} = {result_subtract}")
print(f"{num1} * {num2} = {result_multiply}")
