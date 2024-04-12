# Description: Steffensen's Method
# Author: David Sequera 

# Aitken's Delta-squared Method
aitken = lambda a, b, c:  a - (b-a)*(b-a) / (a-2.0*b+c)

def steffensen(f, x0, max_iter, T = 1e-6, g=None):
    if g is None:
        g = lambda x: x - f(x)
    a,i = x0, 0
    while abs(f(a)) > T and max_iter > i:
        b = g(a)
        c = g(b)
        a = aitken(a, b, c)
        i += 1
        print("Iteration: ", i, f" x:{a} g(x): {abs(g(a))}")
    if i == max_iter:
        raise ValueError("The method did not converge")
    return a

# Example
f = lambda x: -x**3+2*x+1

x0 = 1.5
max_iter = 1000
T = 1e-9
print(steffensen(f, x0, max_iter, T))
print(steffensen(f, x0, max_iter, T, g=lambda x: (x**3-1)/2))