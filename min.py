
a=[]
i=0
while i<10:
    user=int(input("enter the number"))
    a.append(user)
    i+=1
    j=0
    max=a[0]
    while j<len(a):
        if max<a[j]:
            max=a[j]
        j+=1
        k=0
        min=a[k]
        while k<len(a):
            if min>a[k]:
                min=a[k]
            k+=1
print("max=",max,"min=",min)
            
    