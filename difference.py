
list1=[9,2,3,4,5,6,13]
list2=[1,2,3,5,4,6,7]
length=len(list1)
i=0
a=[]
while i<length:
    if list1[i] not in (list2):
        a.append(list1[i])
    i+=1
print(a)