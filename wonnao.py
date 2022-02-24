list=[2,4,6,8]
i=1
a=[]
while i<len(list):
    k=list[i]-list[i-1]
    a.append(k)
    i+=1
print(a)
    