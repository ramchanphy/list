list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
length=len(list1)
a=[]
i=0
while i <=length:
    if i not in list2:
        a.append(i)
    i+=1
print(a)




