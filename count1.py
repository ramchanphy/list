a=["aba","ded","hij","xyzx","aba"]
i=0
c=0
b=[]
while i<len(a):
    if len(a[i])>0 and a[i][0]==a[i][-1]:
        b.append(a[i])
        c+=1
    i+=1
print(c)
print(b)
