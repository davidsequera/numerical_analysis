# Author: David Sequera

import numpy as np


def substract_row(A, b, i, j, factor):
    A[j] -= factor * A[i]
    b[j] -= factor * b[i]
    return A, b

def gauss(A, b):
    n, m = A.shape
    # Conditions
    if n != m:
        raise ValueError("Matrix A must be square")
    if n != len(b):
        raise ValueError("Matrix A and vector b must have the same size")
    if np.linalg.det(A) == 0:
        raise ValueError("Matrix A is linearly dependent")
    # Forward elimination
    for j in range(m):
        #  Condition for singular matrix
        if A[j, j] == 0:
                raise ValueError("Matrix A is singular")
        for i in range(j+1, n):
            factor = A[i, j] / A[j, j]
            A, b = substract_row(A, b, j, i, factor)
    # Backward substitution
    print (A)
    x = np.zeros(n)
    # Last element
    x[n-1] = b[n-1] / A[n-1, n-1]
    # Rest of the elements
    for i in range(n-2, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i, j] * x[j]
        x[i] /= A[i, i]
    return x





example = np.array([[2, 1, -1], [3, 2, 1], [1, 1, 1]], dtype=np.float64)
b = np.array([8, 12, 6], dtype=np.float64)
print (example)
print (b)
x = gauss(example, b)
print(x)
print(np.linalg.solve(example, b))

