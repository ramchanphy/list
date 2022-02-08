a=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
i=0
b=[]
c=[]
sum=0
while i<len(a):
    if a[i]>0:
        c.append(a[i])
        j=c[0]
        while j<len(c):
            if c[i]<j:
                j=c[i]
            j+=1
    else:
        sum=sum+a[i]
    i+=1
b.append(j)
b.append(sum)
print(b)

    
        
        