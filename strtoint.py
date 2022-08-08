list=['2',4,5,'6',7,'8']
i=0
a=[]
while i<len(list):
    if list[i]==str(list[i]):
        a.append(int(list[i]))
    else:
        a.append(list[i])
    i+=1
print(a)