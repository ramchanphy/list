a=["aba","def","hij","xyzx","aba"]
i=0
while i<len(a):
    j=0
    count=0
    while j<len(a[i]):
        if a[i][j]==a[i][j]:
            count+=1
        j+=1
    i+=1
print(count)
