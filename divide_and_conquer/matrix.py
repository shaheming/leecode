import numpy as np


def multiply(m1, m2):
    row = m1.shape[0]
    col = m1.shape[1]
    if row == 1 and col == 1:
        return np.array([m1[0][0] * m2[0][0]])
    div = row / 2
    A11 = m1[:div, :div]
    A12 = m1[:div, div:]
    A21 = m1[div:, :div]
    A22 = m1[div:, div:]
    B11 = m1[:div, :div]
    B12 = m1[:div, div:]
    B21 = m1[div:, :div]
    B22 = m1[div:, div:]
    # A11 * B11
    print(A11, B11, A12, B21)
    C11 = multiply(A11, B11) + multiply(A12, B21)
    # A12 * B21
    C12 = multiply(A11, B12) + multiply(A12, B22)
    # A11 * B12
    C21 = multiply(A21, B11) + multiply(A22, B21)

    C22 = multiply(A21, B12) + multiply(A22, B22)
    print(C11,C12)
    row1 = np.hstack((C11, C12))
    row2 = np.hstack((C21, C22))
    return np.vstack((row1, row2))


m1 = np.array([[1, 2], 
               [3, 4]])

print(multiply(m1,m1))
print(np.matmul(m1, m1))
