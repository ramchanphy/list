list=[12,67,23,33]
i=0
a=[]

while i<len(list):
    j=0
    while j<len(list[i]):
        a.append(j)
        j+=1
    i+=1
print(a)
