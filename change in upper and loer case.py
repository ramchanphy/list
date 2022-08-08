a="HELLO! Priyanka!"
b=""
i=0
while i<len(a):
    if a[i]>="A" and a[i]<="Z":
        c=a[i].lower()
        b+=c
    elif a[i]=="!" or a[i]==" ":
        b+=a[i]
    else:
        d=a[i].upper()
        b+=d
    i+=1
print(b)
