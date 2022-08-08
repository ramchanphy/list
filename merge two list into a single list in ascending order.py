l1=[1,2,4]
l2=[1,3,4]
l3=l1+l2
for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if l3[i]>l3[j]:
            l3[i],l3[j]=l3[j],l3[i]
print(l3)
i=0
while i<len(l3):
    j=0
    while j<len(l3):
        if l3[i]<l3[j]:
            l3[i],l3[j]=l3[j],l3[i]
        j+=1
    i+=1
print(l3)

