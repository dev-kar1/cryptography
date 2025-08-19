import numpy as np

'''Gram-Schmidt Orthogonalisation Block''' 

def GramSchmidtCoefficient(b1,b2):
    return np.dot(b1,b2)/np.dot(b2,b2)
  
def Projection(b1,b2):
    return GramSchmidtCoefficient(b1,b2) * b2
  
def GramSchmidt(B):
    n = B.shape[0]
    m = B.shape[1]
    GSO = np.zeros((n,m))
    for i in range (1,n):
        vector = B[i].copy()
        for j in range (i):
            vector = vector - Projection(vector, GSO[j])
        GSO[i] = vector
    return GSO
"GSO is fine and good to be used in LLL"

'''LLL Implementation'''

#the dependencies of lll go here, namely lovasz condition, sizereduce, etc
def Lovasz(B, GSO, k,  delta = 0.75):
    mu = GramSchmidtCoefficient(B[k],GSO[k-1])
    lhs = delta * np.dot(GSO[k-1],GSO[k-1])
    rhs = np.dot(mu * GSO[k-1] + GSO[k] , mu * GSO[k-1] + GSO[k])
    return lhs <= rhs
    
    
    
def SizeReduce(B):
    n = B.shape[0]
    for i in range (1,n):
        for j in range (i-1,-1,-1):
            mu = np.round(GramSchmidtCoefficient(B[i],B[j]))
            if mu != 0:
                B[i] = B[i] - mu * B[j]
    return B


#the LLL computation goes here
def LLL(B, delta = 0.75):
    n = B.shape[0]
    B = B.copy()
    k = 1
    SizeReduce(B) #we will make the function in the dependencies section
    GSO = GramSchmidt(B)
    for i in range (len(B)): #n=len(B) is rank of lattice, no of rows in lattice
        if not Lovasz(B, GSO, k, delta):
            B[i , i-1] = B[i-1 , i] #swapping works like a,b = b,a in python
            LLL(B)
        else:
            return B


