def bisection(f, a, b, T=1e-6):
    #  Function to find the root of f in the interval [a,b]
    if f(a) * f(b) > 0:
        print('No root in this interval', f(a), f(b) )
        return None
    i = 0
    while (b - a) > T:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        i += 1
    # print("Iterations: ", i)
    return (a + b) / 2


#  Example
f = lambda x: 2*x**4 - 3*x**3 -2*x**2 + 3*x + 1
a = -0.6
b = 1.5
print(bisection(f, a, b))