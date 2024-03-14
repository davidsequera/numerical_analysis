import numpy as np

def SOR(A,b, T = 1e-6):
    n,m = A.shape
    if n != m:
        raise ValueError("Matrix A must be square")
    if n != len(b):
        raise ValueError("Matrix A and vector b must have the same size")
    
    # W omega
    W = optimal_omega(A)
    print("W: ", W)

    X = np.zeros(n) # initial guess
    X_1 = np.copy(X) # initial guess
    dk = 1 
    i = 0
    while(T < dk):
        for i in range(n):
            o = 0
            for j in range(n):
                if j != i:
                    o += A[i,j] * X[j]
            X[i] = W*( (b[i] - o) / A[i,i] ) + (1-W)*X_1[i]
        dk = np.linalg.norm(X - X_1)
        X_1 = np.copy(X)
        i += 1
    print("Iterations: ", i)
    return X

# Tj = I - (D^-1)A
def t_j(A):
    n,n = A.shape
    Tj, v = np.copy(A), np.zeros(n)
    for i in range(n):
        Tj[i,i], v[i] =  0,-A[i,i]
        Tj[i] /= v[i]
    return Tj


# vectorized version
tt_j = lambda A: np.identity(A.shape[0]) - np.linalg.inv(np.diag(np.diag(A))) @ A

optimal_omega = lambda A: 2 / (1 + np.sqrt(1 - (np.max(np.abs(np.linalg.eig(t_j(A)).eigenvalues)))**2))

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]], dtype=np.float64)


b = np.array([6., 25., -11., 15.], dtype=np.float64)


print (A)
print (b, "\n", "*" * 50)
x = SOR(A, b)
print(x)
print(np.linalg.solve(A, b))
