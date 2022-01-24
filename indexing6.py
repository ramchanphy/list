a=[3,[7,[5,[4,33,],2,1],0],22,26,10]
i=0
l=[]
while i<len(a):
    if type(a[i])==type(l):
        j=0
        # b=[]
        while j<len(a[i]):
            if type(a[i][j])==type(l):
                k=0
                while k<len(a[i][j]):
                    a.append(a[i][j][k])
                    k+=1
            else:
                l.append(a[i][j])
            j+=1
    else:
        l.append(a[i])
                
    i+=1
print(l)
