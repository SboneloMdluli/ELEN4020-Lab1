import random

def rank2TensorAdd(a,b,c,i,j):

    for k in range(len(a[0])): 
        c[i][j] += a[i][k]*b[k][j]
    

def rank2TensorMult(a,b):
    
    c = [[0 for x in range(len(a))] for y in range(len(b))] # list comprehension 
    
    for i in range(len(a)): # iterate through rows 
        for j in range(len(b[0])): # iterate through columns
        
            rank2TensorAdd(a,b,c,i,j)
            
    return c


def check_dimensions(a,b):
    try:
        assert len(a)==len(b[0])
        return True
    except :
        print('cannot perform multiplication,incompatible dimensions')

#main program    
n=10
rank2_A=[[random.randint(1,21) for x in range(n)] for y in range(n)]
rank2_B=[[random.randint(1,21) for x in range(n)] for y in range(n)]

if check_dimensions(rank2_A,rank2_B):
    for x in rank2TensorMult(rank2_A,rank2_B):
         print(*x)
