list=[2,4,6,8,10,11,8,9]
a=[]
i=0
while i<len(list):
    k=[list[i],list[i+1]]
    a.append(k)
    i+=2
print(a)