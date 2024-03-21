def secant_method(f, x0, x1,T=1e-6):
    y2 = 1
    i = 0
    while (abs(y2) > T):
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        #  Formula to find x when y is equal to 0 in the secant
        x2 = x0 - (x1-x0)*f(x0)/ (f(x1) - f(x0)) 
        # Swapping the values
        x0,x1 = x1,x2
        i += 1
        y2 = f(x2)
        if i > 100:
            print('Not Convergent!')
            break
    # print("Iterations: ", i)
    return x2 


#  Example
f = lambda x: 2*x**4 - 3*x**3 -2*x**2 + 3*x + 1
x0 = 3
x1 = 4
print('\n Function is 0 when x is: %0.8f' % secant_method(f, x0, x1))