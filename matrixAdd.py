def add(A,B):
    C=[]
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j]+B[i][j])
    return C

A=B=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
C=add(A,B)
print(C)