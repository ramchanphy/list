list=["1","2","3","4","5","6","7","8"]
x=[1,2,3,4,5,6,7,8]
a=""
i=0
while i<len(x):
    j=i+1
    while j<len(x):
        k=x[j]-x[i]
        a+=str(k)+","
        j+=1
    i+=1
print(a)

