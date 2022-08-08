num=[2,7,11,15]
target=9
a=[]
i=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]+num[j]==target:
            a.append(i)
            a.append(j)
        j+=1
    break
    i+=1
print(a)