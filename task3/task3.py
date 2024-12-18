import math
import matplotlib.pyplot as plt


def secant_method(f, x0, x1, tol=1e-3, max_iter=100):
    """secant method for finding the root of an equation."""
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1 - fx0) < 1e-10:  # prevent division by zero
            raise ValueError("division by zero in secant method")
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("secant method did not converge")


def iteration_method(g, x0, tol=1e-3, max_iter=100):
    """simple iteration method for finding the root of an equation."""
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("iteration method did not converge")


def newton_raphson(f, df, x0, tol=1e-3, max_iter=100):
    """newton-raphson method for finding the root of an equation."""
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if abs(dfx) < 1e-10:  # Check for zero derivative
            raise ValueError("derivative is zero in Newton-Raphson method")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("newton-raphson method did not converge")


# defining functions, their derivatives, and iteration functions

def f1(x): return x ** 3 - x - 1


def df1(x): return 3 * x ** 2 - 1


def g1(x): return (x + 1) ** (1 / 3)


def f2(x): return x - math.cos(x)


def df2(x): return 1 + math.sin(x)


def g2(x): return math.cos(x)


def f3(x): return math.exp(-x) - x


def df3(x): return -math.exp(-x) - 1


def g3(x): return math.exp(-x)


def f4(x): return x ** 3 + x ** 2 + x + 7


def df4(x): return 3 * x ** 2 + 2 * x + 1


def g4(x): return -((x ** 2 + x + 7) ** (1 / 3)) if x ** 2 + x + 7 >= 0 else None


def f5(x): return x ** 2 + 4 * math.sin(x)


def df5(x): return 2 * x + 4 * math.cos(x)


def g5(x): return math.sqrt(-4 * math.sin(x)) if -4 * math.sin(x) >= 0 else None


def f6(x): return math.cos(x) - x * math.exp(x)


def df6(x): return -math.sin(x) - math.exp(x) - x * math.exp(x)


def g6(x): return math.cos(x) / math.exp(x)


# solving equations with different methods
solutions = []
functions = [
    (f1, df1, g1, [1, 1.5], 1.2),
    (f2, df2, g2, [0.5, 0.6], 0.5),
    (f3, df3, g3, [0, 0.5], 0.5),
    (f4, df4, g4, [-2, -1], -1.5),
    (f5, df5, g5, [-2, -1], -1.5),
    (f6, df6, g6, [0, 0.5], 0.5)
]

for i, (f, df, g, secant_range, x0) in enumerate(functions, start=1):
    print(f"\nsolving equation {i}:")
    try:
        root_secant = secant_method(f, secant_range[0], secant_range[1])
        print(f"secant method: x = {root_secant:.3f}")
    except ValueError as e:
        root_secant = "fail"
        print(f"secant method: {e}")

    try:
        root_iter = iteration_method(g, x0)
        print(f"iteration method: x = {root_iter:.3f}")
    except (ValueError, TypeError) as e:
        root_iter = "fail"
        print(f"iteration method: {e}")

    try:
        root_newton = newton_raphson(f, df, x0)
        print(f"newton-raphson method: x = {root_newton:.3f}")
    except ValueError as e:
        root_newton = "fail"
        print(f"newton-raphson method: {e}")

    solutions.append((root_secant, root_iter, root_newton))

# Final results table
print("\nresults of all methods:")
for i, (root_secant, root_iter, root_newton) in enumerate(solutions, start=1):
    print(f"equation {i}: secant = {root_secant}, iteration = {root_iter}, newton = {root_newton}")

# Visualization of graphs
for i, (f, _, _, _, _) in enumerate(functions, start=1):
    x_values = [j / 100 for j in range(-300, 300)]
    y_values = [f(x) for x in x_values]

    plt.figure()
    plt.plot(x_values, y_values, label=f'f{i}(x)')
    plt.axhline(0, color='black', linestyle='--')
    plt.title(f'graph of equation {i}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()