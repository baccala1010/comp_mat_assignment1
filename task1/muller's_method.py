import math

#   defining a function
def f(x):
    return x**3 - 2 * x**2 + x - 1

def muller_method(f, x0, x1, x2, tol=1e-6, max_iter=100):
    for i in range(max_iter):

        #   calculating the values of f(x0), f(x1) and f(x2)
        f0, f1, f2 = f(x0), f(x1), f(x2)

        #   calculating differences
        h0 = x1 - x0
        h1 = x2 - x1

        delta0 = (f1 - f0) / h0
        delta1 = (f2 - f1) / h1

        #   calculating coefficient a
        a = (delta1 - delta0) / (h1 + h0)

        #   calculating coefficient b
        b = a * h1 + delta1

        #   calculating coefficient c
        c = f2

        #   calculating the discriminant
        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            raise ValueError('Discriminant is negative, can be complex')

        #   choosing a root with larger absolute value, denominator should not be zero
        root_part = math.sqrt(discriminant)
        if abs(b + root_part) > abs(b - root_part):
            denominator = b + root_part
        else:
            denominator = b - root_part

        #   calculating the next root
        dx = -2 * c / denominator
        x_new = x2 + dx

        #   checking if the root is within the tolerance
        if abs(dx) < tol:
            print(f"root found at iteration {i + 1}")
            return x_new

        #   updating the values of x0, x1 and x2
        x0, x1, x2 = x1, x2, x_new

    raise RuntimeError("Max iterations overreached")

#   taking inputs
x0 = float(input('first guess: '))
x1 = float(input('second guess: '))
x2 = float(input('third guess: '))

#   run the method
try:
    root = muller_method(f, x0, x1, x2)
    print(f"Root found: {root}")
except Exception as e:
    print(f"Error: {e}")