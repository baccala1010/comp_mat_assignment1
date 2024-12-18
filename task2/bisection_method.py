import math

def f(x):
    return math.exp(x) - x**2

def bisection_method(f, a, b, stages=7):
    if f(a) * f(b) >= 0:
        raise ValueError("function must have opposite signs at the end points")

    for stage in range(1, stages + 1):
        #   calculating the midpoint
        c = (a + b) / 2
        fc = f(c)

        #   output the current stage
        print(f"stage {stage}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6f}")

        #   define which half of interval the root is in
        if fc == 0: # the exact root is found
            return c
        elif f(a) * fc < 0: # the root is in the left half
            b = c
        else: # the root is in the right half
            a = c

    return (a + b) / 2 # approximate root after the last stage

#   taking inputs
a, b = -2, 0

#   calling the function
approx_root = bisection_method(f, a, b, stages=7)
print(f"approximate root is {approx_root:.6f}")