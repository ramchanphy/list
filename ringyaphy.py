list=[[2,10],[5,3],[8,6]]
i=1
a=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        sub=list[i]-list[i][j]
        j+=1
    a.append([sub])
    i+=1
print(a)
