import random

def make_verticalPlane(b,j):
    return [row[j] for row in b]
    

def rank3d(a,b):

    rslt_vector = [[0 for x in range(len(a))] for y in range(len(b))]
    h_plane = [[0 for x in range(len(a))] for y in range(len(a))]
    
    rank3_C=[[[random.randint(1,21) for x in range(n)] for y in range(n)]for z in range(n)]

    for i in range(len(a)): 
        h_plane = a[i]# select horizontal plane in a
        print(h_plane,'hp')
        for j in range(len(b)):
            v_plane = make_verticalPlane(b,j) # select vertical plane in b
            print(v_plane,'vp')
            
            for k in range(len(h_plane)): #go through rows in horizontal plane
                for x in range(len(v_plane)): #go through each column in horizontal plane
                    print(h_plane[k],v_plane[x],'damn')
                    #rslt_vector[x]=rank2TensorMult(h_plane[k],v_plane[x])
                    
            rank3_C[i][j].append(rslt_vector)

    return rank3_C

def rank2TensorAdd(a,b,c,i,j):

    for k in range(len(a[0])):
        c[i][j] += a[i][k]*b[k][j]


def rank2TensorMult(a,b):

    c = [[0 for x in range(len(a))] for y in range(len(b))] 

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
if __name__ == "__main__":
    n=2
    #rank2_A=[[random.randint(1,21) for x in range(n)] for y in range(n)]
    #rank2_B=[[random.randint(1,21) for x in range(n)] for y in range(n)]

    rank3_A=[[[random.randint(1,5) for x in range(n)] for y in range(n)]for z in range(n)]
    rank3_B=[[[random.randint(1,5) for x in range(n)] for y in range(n)]for z in range(n)]


    #print(rank3_B[0])
    if check_dimensions(rank3_A,rank3_B):
        for x in rank3_A:
             print(x)
    print('--------------------------------')         
    if check_dimensions(rank3_A,rank3_B):
        for x in rank3_B:
             print(x)
             
    print('--------------------------------')           
    if check_dimensions(rank3_A,rank3_B):
        for x in rank3_A[0]:
             print(x)
    print('--------------------------------')        
    if check_dimensions(rank3_A,rank3_B):
        for x in make_verticalPlane(rank3_B,0):
             print(x)
    print('--------------------------------')        
    if check_dimensions(rank3_A,rank3_B):
        for x in rank3d(rank3_A,rank3_B):
             print(x)   
