import numpy as np

'''Gram-Schmidt Orthogonalisation''' 

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


'''LLL Implementation'''
#the lll computation goes here
def LLL(B):
    SizeReduce(B) #we will make the function in the dependencies section
    for i in range (len(B)): #n=len(B) is rank of lattice, no of rows in lattice
        if(lovasz(bi,bj)=False):
            bi,bi+1 = b1+1,bi #swapping works like a,b = b,a in python
            LLL(B)
        else:
            return B
#the dependencies of lll go here, namely lovasz condition, sizereduce, etc
def Lovasz(b1,b2):
    delta = 0.75 #can change between 0.25 to 1
    if (delta * (np.dot(b1,b1)) > np.dot((GramSchmidtCoefficient(b2,b1)* b1+b2),(GramSchmidtCoefficient(b2,b1)* b1+b2)):
        return True
    else :
    return False
    
    
    
def SizeReduce(B):
    GramSchmidt(B)
    for j in range (2,n):
        for i in range (j-1,1):
            m = GramSchmidtCoefficient(b1,b2)
            bj = bj - round(m)*bi
    return B
    
