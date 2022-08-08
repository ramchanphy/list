
A=[2,3,4]   
i=0
x=[]
while i<len(A):
    j=0
    while j<len(A):
        if (A[i])!=(A[j]):
            a=str(A[i])+str(A[j])
            x.append(a)
        j+=1
    i += 1
print(x)