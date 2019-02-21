import random

def Print_MAT(MAT):
    """print matrix in layers"""
    for x in MAT:
        print(x)

def exctract_clmn(b,j):
    return [row[j] for row in b]
    
def colvec_to_mat(vec_a):
    """Convert column vector to square matrix by zero padding"""
    col_matrix = [[0 for x in range(len(vec_a))] for y in range(len(vec_a))]
    
    for i in range(len(vec_a)):
            col_matrix[i][0] = vec_a[i]
    
    return col_matrix
    
def rowvec_to_mat(vec_b):
    """Convert row vector to square matrix by zero padding"""
    rol_matrix = [[0 for x in range(len(vec_b))] for y in range(len(vec_b))]
    
    for j in range(len(vec_b)):
            rol_matrix[0][j]= vec_b[j]
    
    return rol_matrix
    
def rank3TensorAdd(A,val,x,i,k):
    A[x][i][k]+=val
    
    
def rank3TensorMult(a,b):
    """Perform 3-D by 3-D array multiplication"""

    h_plane = [[0 for x in range(len(a))] for y in range(len(a))]
    
    rank3_C=[[[0 for x in range(n)] for y in range(n)]for z in range(n)]
        
    mat_a = mat_b = [[0 for x in range(len(a))] for y in range(len(a))]
    
    tmp=rslt_ =0
        
    for i in range(len(a)): 
        h_plane = a[i]# select horizontal plane in a
       
        for j in range(len(b)):
            v_plane = exctract_clmn(b,j) # select vertical plane in b

            
            for k in range(len(h_plane)): #go through rows in horizontal plane
                
                for x in range(len(v_plane)): #go through each column in horizontal plane
                   
                    Vplane_clm = exctract_clmn(v_plane,x) 
                    
                    # must convert vector to n*n matrices
                    mat_a =rowvec_to_mat(h_plane[k])
                    
                    mat_b =colvec_to_mat(Vplane_clm)
                    

                    tmp=rank2TensorMult(mat_a,mat_b) 
                    rslt_ = tmp[0][0] # get single value
                    
                    rank3TensorAdd(rank3_C,rslt_,x,i,k)
                   

    return rank3_C

def rank2TensorAdd(a,b,c,i,j):

    for k in range(len(a[0])):
        c[i][j] += a[i][k]*b[k][j]


def rank2TensorMult(a,b):
    """Perform 2-D by 2-D array multiplication"""
    c = [[0 for x in range(len(a))] for y in range(len(b))] 

    for i in range(len(a)): # iterate through rows
        for j in range(len(b[0])): # iterate through columns

            rank2TensorAdd(a,b,c,i,j)

    return c


def check_dimensions(a,b):
    """Check if dimensiosn are compatible for matrix multiplication"""
    try:
        assert len(a)==len(b[0])
        return True
    except :
        print('cannot perform multiplication,incompatible dimensions')

#main program 
if __name__ == "__main__":
    
    n=3 # =10,=20
    rank2_A=[[random.randint(1,21) for x in range(n)] for y in range(n)]
    rank2_B=[[random.randint(1,21) for x in range(n)] for y in range(n)]

    rank3_A=[[[random.randint(1,21) for x in range(n)] for y in range(n)]for z in range(n)]
    rank3_B=[[[random.randint(1,21) for x in range(n)] for y in range(n)]for z in range(n)]

    print('-----------------------------RANK2-TENSOR-----------------------------')
    if check_dimensions(rank2_A,rank2_B):
        Print_MAT(rank2TensorMult(rank2_A,rank2_B))
   
    print('-----------------------------RANK3-TENSOR-----------------------------')
    
    if check_dimensions(rank3_A,rank3_B):
        Print_MAT(rank3TensorMult(rank3_A,rank3_B))
            
