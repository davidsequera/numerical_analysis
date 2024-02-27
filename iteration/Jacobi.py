import numpy as np

def Jacobi(A,b, T = 10**-6):
    n,m = A.shape
    if n != m:
        raise ValueError("Matrix A must be square")
    if n != len(b):
        raise ValueError("Matrix A and vector b must have the same size")
    
    X = np.zeros(n, dtype=np.float64) # initial guess
    X_1 = X # initial guess
    dk = 1 
    # Diagonal vector
    D = np.diag(A)
    # Remainder matrix = A - D_Matrix
    R = A - np.diagflat(D)
    i = 0
    while(T < dk):
        X = (b - np.dot(R,X))/D
        dk = np.linalg.norm(X - X_1)
        X_1 = X
        i += 1
    print("Iterations: ", i)
    return X

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]], dtype=np.float64)
b = np.array([6., 25., -11., 15.], dtype=np.float64)
print (A)
print (b, "\n", "*" * 50)
x = Jacobi(A, b)
print(x)
print(np.linalg.solve(A, b))