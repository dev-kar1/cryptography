from math import gcd
from functools import reduce

def extended_gcd(a, b):
    """Return (g, x, y) such that ax + by = g = gcd(a, b)."""
    if b == 0:
        return (abs(a), 1 if a > 0 else -1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def multi_extended_gcd(nums):
    """
    Given nums = [a1, a2, ..., ak],
    return (g, coeffs) such that sum coeffs[i]*nums[i] = g = gcd(nums).
    """
    g = nums[0]
    coeffs = [1]
    
    for i in range(1, len(nums)):
        g_new, x, y = extended_gcd(g, nums[i])
        coeffs = [c * x for c in coeffs] + [y]
        g = g_new
    
    return g, coeffs

def lattice_basis_reduction(A):
    """
    Input:
        A: n x m integer matrix (list of lists), rank(A) = n, n <= m
    Output:
        B: n x n integer matrix such that B Z^n = A Z^m
    """
    n = len(A)
    m = len(A[0])

    # Work with columns
    cols = [[A[i][j] for i in range(n)] for j in range(m)]

    for j in range(n):
        # Step 2: gcd of entries from row j to n in column j
        entries = cols[j][j:]
        g, coeffs = multi_extended_gcd(entries)

        # Step 3–4: construct new column a_j
        new_col = [0] * n
        for idx, c in enumerate(coeffs):
            row = j + idx
            new_col[row] += c * cols[j][row]

        cols[j] = new_col

        # Step 5–7: eliminate below-diagonal entries
        for k in range(j + 1, m):
            if cols[k][j] != 0:
                factor = cols[k][j] // g
                cols[k] = [
                    cols[k][i] - factor * cols[j][i]
                    for i in range(n)
                ]

    # Step 9: return first n columns
    B = [[cols[j][i] for j in range(n)] for i in range(n)]
    return B
