list=[1,2,3,4,5,6]
b=[]
i=0
j=1
while i <len(list):
    if list[i] not in b:
        b.append(list[-j])
        b.append(list[i])
    j+=1
    i+=1
print(b)