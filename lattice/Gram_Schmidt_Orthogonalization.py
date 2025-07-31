'''Gram Schmidt Orthogonalization'''
import numpy as np

def GramSchmidtCoefficient(b1,b2):
    return np.dot(b1,b2)/np.dot(b2,b2)
  
def Projection(b1,b2):
    return GramSchmidtCoefficient(b1,b2) * b2
  
def GramSchmidt(B):
    n = B.shape[0]
    m = B.shape[1]
    GSO = np.zeros((n,m))
    for i in range (n):
        vector = B[i].copy()
        for j in range (i):
            vector = vector - Projection(vector, GSO[j])
        GSO[i] = vector
    return GSO
