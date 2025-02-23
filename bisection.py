import sympy as sp
import numpy as np

def get_function(equation):
    """Safely parse the equation into a function."""
    x = sp.symbols('x')
    expr = sp.sympify(equation)  # Convert string to sympy expression
    return sp.lambdify(x, expr)  # Convert sympy expression to callable function

def find_interval(f, start=-10, end=10, step=0.5):
    """Finds an interval [a, b] where f(a) and f(b) have opposite signs."""
    x_values = np.arange(start, end, step)
    for i in range(len(x_values) - 1):
        a, b = x_values[i], x_values[i+1]
        if f(a) * f(b) < 0:  # Check for sign change
            return a, b
    raise ValueError("No valid interval found where f(a) and f(b) have opposite signs.")

def bisection_method(f, a, b, tolerance=1e-4, max_iter=10):
    """Bisection method with a maximum of 10 iterations."""
    for i in range(max_iter):
        c = (a + b) / 2  # Compute midpoint
        fc = f(c)

        print(f"Iteration {i+1}: c = {c:.6f}, f(c) = {fc:.6f}")

        if abs(fc) < tolerance:
            return c  # Root found

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c  # Return last computed value (even if not converged)

# Get user input for equation
equation = input("Enter equation (e.g., x**3 - 5*x + 3): ")
tol = float(input("Enter tolerance: "))

# Process and calculate result
try:
    f = get_function(equation)  # Securely parse equation
    a, b = find_interval(f)  # Automatically find valid boundaries
    print(f"Found interval: a = {a}, b = {b}")

    root = bisection_method(f, a, b, tol)
    print(f"\nApproximate Root after 10 iterations: {root:.6f}")
    print(f"f(root): {f(root):.6f}")

except ValueError as ve:
    print(f"Value Error: {ve}")
except Exception as e:
    print(f"Error: {e}")