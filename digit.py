list=[12,45,324,36]
i=0
while i<len(list):
    b=str(list[i])
    j=0
    sum=0
    while j<len(b):
        sum=sum+int(b[j])
        j+=1
    print(sum,end=",")
    i+=1
        