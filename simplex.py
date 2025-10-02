import numpy as np

# Global float precision
eps = 0.0001

def simplex(A, b, c, x_0):
    """
    Returns, if it exists, a solution to the following LP problem:

    minimize <c, x>
    s.t Ax = b
        x >= 0
    with x_0 is a [basic feasible solution](https://en.wikipedia.org/wiki/Basic_feasible_solution)

    A is a (m x n) numpy array
    b is a (m x 1) numpy array
    c is a (n x 1) numpy array
    x_0 is a (n x 1) numpy array

    Assumes that m <= n and rank A = m.
    """
    m, n = A.shape

    assert np.linalg.matrix_rank(A) == m

    basis = x_0 >= eps
    basis.shape = (n,)
    while True:
        A_B = A[:, basis]
        A_B_inv = np.linalg.inv(A_B)
        x_B = A_B_inv @ b
        reduced_cost = c - A.transpose() @ A_B_inv.transpose() @ c[basis]
        if np.all(reduced_cost[basis == False] >= 0):  
            sol = np.zeros(n)
            count = 0
            for i, v in enumerate(basis):
                if v:
                    sol[i] = x_B[count][0]
                    count += 1
            return sol
        j = np.argmax(np.logical_and(reduced_cost.reshape(n) <= -eps, basis == False))
        d_j = A_B_inv @ A[:,j]

        if np.all(d_j.reshape(m) <= 0):
            raise ValueError("Unbounded problem, no solution")
        q = x_B.reshape(m) / d_j.reshape(m)

        positive_idx = np.where(q >= eps)[0]
        idx = positive_idx[q[positive_idx].argmin()]
        k = np.where(basis)[0][idx]
        
        basis[k] = False
        basis[j] = True
        
    
def basic_feasible_point(A, b, c):
    """
    Returns, if it exists, a basic feasible point of the following LP problem:
    
    minimize <c, x>
    s.t Ax = b
        x >= 0

    It works by solving the associated LP problem given by
    minimize sum_i z_i
    s.t Ax + Dz = b
        x >= 0, z >= 0
    
    where D is a diagonal matrix with D_ii = 1 if b_i >= 0, -1 otherwise.
    
    The point (0, Db) is always a basic feasible point of this algorithm,
    and this new problem is always feasible.
    Applying the simplex method to it, we get a solution (x, z):
    - If z = 0, x is a basic feasible solution to the initial problem
    - If z != 0, the initial problem is not solvable. 
    """
    m, n = A.shape
    
    c_aux = np.concatenate((np.zeros(n), np.ones(m)))
    D = np.diag([(-1)**int(x) for x in b.reshape(m) <= 0]) # D_ii = 1 if b_ii >= 0, -1 otherwise
    A_aux = np.concatenate((A, D), axis = 1)
    x_0 = np.concatenate((np.zeros(n), D@b.reshape(m)))
    
    sol = simplex(A_aux, b, c_aux, x_0)
    x, z = sol[:n], sol[n:]

    if np.linalg.norm(z) <= eps:
        return x.reshape((n,1))
    
    raise ValueError("Unbounded problem, no solution")



if __name__ == "__main__":
    """
    EXAMPLE:

    Solving
    
    min -x1 - 3x2
    s.t.    2x1 + 3x2 ≤ 6
            -x1 + x2 ≤ 1
            x1, x2 ≥ 0
    
    or in standard form, after addition of slack variables
    
    min -x1 - 3x2
    s.t.    2x1 + 3x2 + x3 = 6
            -x1 + x2 + x4 = 1
            x1, x2, x3, x4 ≥ 0

    A basic feasible solution is given by x_0 = (0, 0, 1, 1)
    """

    A = np.array([[2, 3, 1, 0], [-1, 1, 0, 1]])
    c = np.array([-1, -3, 0, 0])
    b = np.array([6, 1])
    c.shape = (4 ,1)
    b.shape = (2, 1)

    x_0 = np.array([0, 0, 1, 1])
    x_0.shape = (4, 1)

    bfp = basic_feasible_point(A, b, c)
    print("A basic feasible point is given by:", bfp)
        
    sol = simplex(A, b, c, bfp)
    print(f"A solution was found: {sol[:2]}")
    print(f"The value of the minimum is {c.transpose() @ sol}")
