list=[1,3,2]
i=2
a=[]
while i<len(list):
    k=list[i+1]-list[i]
    a.append(k)
    i+=1
print(list[i-1]-list[i])