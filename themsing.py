a=[1,3,2]
b=""
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        k=a[j]-a[i]
        b+=str(k)+","
        j+=1
    i+=1
k=b[0:3]
print(k)
