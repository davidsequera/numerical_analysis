import pandas as pd
import numpy as np

def NewtonDividedDifference(M):
    n,m = M.shape
    if m != 2:
        raise ValueError("Enter a 2 column matrix")
    
    X,Y = M[:,0],M[:,1]

    def difference(X1,X2,Y1,Y2):
        return (Y2-Y1)/(X2-X1)
     
    # inferior diagonal that saves the differences 
    diff_matrix = np.zeros((n,n))

    # Base cases (diagonal of the matrix)
    for i in range(0,n):
        diff_matrix[i][i] = Y[i]

    # print(diff_matrix,'\n', "-"*50)
    for j in range(0,n):
        for i in range(j,-1, -1):
            if j == i:
                continue
            diff_matrix[i][j] = difference(X[i],X[j],diff_matrix[i][j-1],diff_matrix[i+1][j])
            # print(diff_matrix,'\n', "-"*50)
    def P(x):
        result = 0
        for i in range(0,n):
            term = diff_matrix[0][i]
            for j in range(0,i):
                term *= (x-X[j])
            result += term
        return result

    return P