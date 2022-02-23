list=[1,2,3,4,5,6,7,8]
# a=int(list)
i=1
b=[]
while i<len(list):
    k=list[i]-list[i-1]
    b.append(k)
    i+=1
print(b)
