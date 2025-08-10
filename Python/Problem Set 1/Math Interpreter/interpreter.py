# interpreter.py - By Charan Katyal# interpreter.py

# Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Split the input into x, y, and z
x, y, z = expression.split(" ")

# Convert x and z to integers
x = int(x)
z = int(z)

# Perform the appropriate arithmetic operation
if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    result = None  # Just in case there's an invalid operator

# Output the result formatted to 1 decimal place
if result is not None:
    print(f"{result:.1f}")
else:
    print("Invalid operator.")
