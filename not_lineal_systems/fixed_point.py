def derivative(f, h=1e-6):
    # difference quotient method  (symmetric)
    return lambda x: (f(x + h) - f(x - h)) / (2 * h)


def fixed_point(f, x0, max_iter, T = 1e-6, g=None, df=None):
    #  Fixed point method
    if df is None:
        df = derivative(f, T)

    if g is None:
        g = lambda x: x - f(x)
    x = x0
    for i in range(max_iter):
        x_old = x
        # if abs(df(x)) >= 1:
        #     raise ValueError("The derivative of the function at the initial point is greater than 1")
        print("Iteration: ", i, f" x:{x} g(x): {abs(g(x))}")
        x = g(x)
        if abs(x - x_old) < T:
            return x
    return x

# Example
f = lambda x: -x**3+2*x+1

x0 = 1.0
max_iter = 1000
T = 1e-6
print(fixed_point(f, x0, max_iter, T))
print(fixed_point(f, x0, max_iter, T, g=lambda x: (x**3-1)/2))