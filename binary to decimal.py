a=[]
size=int(input("enter the size"))
i=0
while i<size:
    list=int(input("enter the binary no."))
    a.append(list)
    print("the list is:",a)
    i+=1
i=-1
power=0
sum=0
while i>=(-(len(a))):
    n=a[i]*2**power
    sum=sum+n
    i-=1
print("decimal value is:",sum)