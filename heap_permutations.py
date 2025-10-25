"""
Implements both iterative and recursive versions of Heap's algorithm for generating permutations of a given sequence
See https://en.wikipedia.org/wiki/Heap%27s_algorithm
"""

def permutations_rec(A, k=None, result=None):
    if k is None:
        k = len(A)
    if result is None:
        result = []
    if k == 1:
        return result.append(A.copy())
    
    permutations_rec(A, k-1, result)
    
    for i in range(k-1):
        if k % 2 == 0:
            A[i], A[k-1] = A[k-1], A[i]
        else:
            A[k-1], A[0] = A[0], A[k-1]
        permutations_rec(A, k-1, result)
    return result

def permutations_ite(A, n=None, result=None):
    if n is None:
        n = len(A)
    if result is None:
        result = []

    c = [0 for _ in range(n)]
    
    result.append(A.copy())

    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                A[i], A[0] = A[0], A[i]
            else:
                A[c[i]], A[i] = A[i], A[c[i]]
            result.append(A.copy())
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1
    return result
    

p = permutations_rec([1, 2, 3, 4])
print(len(p))
print(p)

p2 = permutations_ite([1, 2, 3, 4])
print(len(p))
print(p)

