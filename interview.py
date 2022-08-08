l1=[1,2,3,0,0,0]
l2=[2,5,6]
m=int(input("enter no. for m:-"))
n=int(input("enter no. for n:-"))
l=[]
i=0
while i<m:
    l.append(l1[i])
    i+=1
j=0
while j<n:
    l.append(l2[j])
    j+=1
k=0
while k<len(l):
    x=k+1
    while x<len(l):
        if l[k]>l[x]:
            temp=l[k]
            l[k]=l[x]
            l[x]=temp
        x+=1
    k+=1
print(l)
