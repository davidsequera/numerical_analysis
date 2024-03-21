def derivative(f, h=1e-6):
    # difference quotient method  (symmetric)
    return lambda x: (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson(f, x0, T=1e-6, df=None):
    # allows to pass the derivative as a parameter or aproximate it
    if df is None:
        df = derivative(f, T)
    xi = x0
    xi_1 = xi + 10* T

    i = 0
    while ( abs(xi - xi_1) > T):
        yi = f(xi)
        xi_1 = xi
        xi = xi - yi/df(xi)
        i += 1
    print("Iterations: ", i)
    return xi


#  Example
f = lambda x: 2*x**4 - 3*x**3 -2*x**2 + 3*x + 1
x0 = 0
print(newton_raphson(f, x0))
