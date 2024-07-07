from sympy import symbols, limit, sin, oo  # Make sure to import sin
# Define the variable
x = symbols('x')

# Define the function
f = x*sin(1/x)

# Calculate the limit as x approaches 0
lim = limit(f, x, oo)

print(f"The limit of f(x) = {f} as x approaches 0 is: {lim}")
