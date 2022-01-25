a=[1,2,3,4,5,6,7,8,-11,-12,-13,-14,-15]
i=0
b=[]
c=[]
# sum=0
while i<len(a):
    if a[i]<0:
        b.append(a[i])
        # sum=sum+str(b)
    else:
        c.append(a[i])
    # j=0
    # k=c[i]
    # while j<len(c):
    #     if len(c[j])>len(k):
    #         k=c[j]
    #     j+=1
            
    i+=1
print(b)
# print(sum)
print(c)
# print(k)
# print(sum)
    
        
        