import numpy as np

def build_householder_reflection(v, dim):
    v = v.reshape(dim,1)
    return np.eye(dim) - 2 * v @ v.T

def householder(M):
    """
    Implements this algorithm:
    https://en.wikipedia.org/wiki/QR_decomposition#Using_Householder_reflections
    for computing a QR-decomposition of a rectangular (mxn)-matrix with m >= n.
    """
    (m, n) = M.shape
    Q = np.eye(m)
    R = M.copy()
    for i in range(n):
        dim = m - i
        column = R[i:,i]
        alpha = np.linalg.norm(column)
        e_i_reduced = np.zeros(dim)
        e_i_reduced[0] = 1
        u = column - alpha * e_i_reduced
        v = u / np.linalg.norm(u)
        Q_i_reduced = build_householder_reflection(v, dim)
        Q_i = np.block([[np.eye(i), np.zeros((i, m-i))], 
                        [np.zeros((n-i, i)), Q_i_reduced]])
        Q = Q @ Q_i.T
        R = Q_i @ R
    return (Q, R)

def QR(M):
    (m, n) = M.shape
    assert m >= n
    return householder(M)

A = np.array([
    [12, -51, 4],
    [6, 167, -68],
    [-4, 24, -41]
])

print(QR(A))
