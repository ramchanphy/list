list=['p','q']
a=[]
n=5
i=1
while i<=5:
    j=0
    while j<len(list):
        k=str(i)
        b=list[j]+k
        a.append(b)
        j+=1
    i+=1
print(a)



