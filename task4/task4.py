def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    results = [(x0, x1)]
    for _ in range(max_iter):
        f_x0, f_x1 = f(x0), f(x1)
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        results.append((x1, x2))
        if abs(x2 - x1) < tol:
            return results
        x0, x1 = x1, x2
    return results

def iteration_method(g, x0, tol=1e-6, max_iter=100):
    results = [x0]
    for _ in range(max_iter):
        x1 = g(x0)
        results.append(x1)
        if abs(x1 - x0) < tol:
            return results
        x0 = x1
    return results

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    results = [x0]
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        results.append(x1)
        if abs(x1 - x0) < tol:
            return results
        x0 = x1
    return results

def muller_method(f, x0, x1, x2, tol=1e-6, max_iter=100):
    results = [x0, x1, x2]
    for _ in range(max_iter):
        h1, h2 = x1 - x0, x2 - x1
        delta1, delta2 = (f(x1) - f(x0)) / h1, (f(x2) - x1) / h2
        d = (delta2 - delta1) / (h2 + h1)
        b = delta2 + h2 * d
        D = (b**2 - 4 * f(x2) * d)**0.5
        E = b - D if abs(b - D) > abs(b + D) else b + D
        x3 = x2 - 2 * f(x2) / E
        results.append(x3)
        if abs(x3 - x2) < tol:
            return results
        x0, x1, x2 = x1, x2, x3
    return results

# Define functions
def f(x): return x**3 - 6*x**2 + 11*x - 6.1
def df(x): return 3*x**2 - 12*x + 11
def g(x): return (6.1 - x**3 + 6*x**2) / 11

# Initial guesses
x0_secant, x1_secant = 5, 5.6
x0_iter, x1_iter = 5, 3.8502
x0_newton, x1_newton = 5, 3.8392
x0_muller, x1_muller, x2_muller = 5, 4.1088, 4.0047

# Solutions
secant_results = secant_method(f, x0_secant, x1_secant)
iter_results = iteration_method(g, x0_iter)
newton_results = newton_method(f, df, x0_newton)
muller_results = muller_method(f, x0_muller, x1_muller, x2_muller)

# Print results in table format
print(f"{'root':<10}{'1st method secant':<20}{'2nd method iteration':<20}{'3rd method newton-raphson':<20}{'4th method muller':<20}")
for i in range(max(len(secant_results), len(iter_results), len(newton_results), len(muller_results))):
    x_secant = secant_results[i] if i < len(secant_results) else ('', '')
    x_iter = iter_results[i] if i < len(iter_results) else ''
    x_newton = newton_results[i] if i < len(newton_results) else ''
    x_muller = muller_results[i] if i < len(muller_results) else ''
    print(f"x{i:<9}{x_secant[1]:<20}{x_iter:<20}{x_newton:<20}{x_muller:<20}")