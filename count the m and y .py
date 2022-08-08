# x="my name is phyphy"
# s=x.split()
# a="m"
# b="y"
# count=0
# count1=0
# i=0
# while i<len(s):
#     if a in s[i]:
#         count+=1
#     if b in s[i]:
#         count1+=1
#     i+=1
# print(["m",count,"y",count1])
a=input("enter the character:")
i=0
b=[]
c=[]
while i <len(a):
    j=0
    count=0
    while j<len(a):
        if a[i] not in b:
            if a[i]==a[j]:
                count+=1
                b.append(a[i])
            else:
                count=1
                b.append(a[i])
        j+=1
    c.append(count)
    i+=1
print(c)
    