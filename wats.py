list=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
max=0
a=[]
sum=0
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        sum=sum+list[j]
        j+=1
    if sum>max:
        max=sum
        a.append(max)
    i+=1
print(a)