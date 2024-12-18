def newton_method(f, df, x0, tol_abs=1e-6, tol_rel=1e-6, max_iter=100, error_type="absolute"):
    """implements newton's method with absolute and relative error termination criteria"""
    iter_count = 0
    while iter_count < max_iter:
        x1 = x0 - f(x0) / df(x0)  # newton's formula
        Ea = abs(x1 - x0)  # absolute error
        Er = Ea / abs(x1) if x1 != 0 else float('inf')  # relative error

        print(f"iteration {iter_count + 1}: x = {x1:.8f}, Ea = {Ea:.8e}, Er = {Er:.8e}")

        # termination criteria
        if error_type == "absolute" and Ea < tol_abs:
            print("terminating based on absolute error")
            return x1, iter_count + 1
        elif error_type == "relative" and Er < tol_rel:
            print("terminating based on relative error")
            return x1, iter_count + 1

        x0 = x1
        iter_count += 1

    print("maximum iterations reached")
    return x1, iter_count


# define the function and its derivative
def f(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6.1  # example: root is near x ~ 1.0


def df(x):
    return 3 * x ** 2 - 12 * x + 11  # derivative of the function


# main execution with examples
if __name__ == "__main__":
    # initial guess
    x0 = 5

    print("=== newton's method with absolute error ===")
    root_abs, iter_abs = newton_method(f, df, x0, tol_abs=1e-6, error_type="absolute")
    print(f"root (absolute): {root_abs:.8f}, iterations: {iter_abs}\n")

    print("=== newton's method with relative error ===")
    root_rel, iter_rel = newton_method(f, df, x0, tol_rel=1e-6, error_type="relative")
    print(f"root (relative): {root_rel:.8f}, iterations: {iter_rel}\n")
