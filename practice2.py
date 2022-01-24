a="ramchanphy"
i=0
b=[]
while i<len(a):
    c=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    if a[i] not in b:
        b+=a[i]
        print(a[i],c)
    i+=1
        
        