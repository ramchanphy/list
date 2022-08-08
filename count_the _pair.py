list=[10,20,10,20,10,10,30,50,10,20]
i=0
s=0
# count=0
while i<len(list):
    j=i
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count+=1
        j+=1
    x=count//2
    print(count)
    s+=x
    i+=1
print(s)