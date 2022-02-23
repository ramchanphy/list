list=[[1,2],[3,4],[5,6],[7,8]]
a=[]
i=0
while i<len(list):
    if type(list[i])==type([]):
        j=0
        while j<len(list[i]):
            if type(list[i][j])==type([]):
                k=0
                while k<len(list[i][j]):
                    a.append(list[i][j][k])
                    k+=1
            else:
                a.append(list[i][j])
            j+=1
    else:
        a.append(list[i])
    i+=1
print(a)
             