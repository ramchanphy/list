list=[3,2,4,6,0,10,13,9]
a=[]
i=0
while i<len(list):
    j=i+1
    while j<len(list):
        c=[list[i],list[j]]
        a.append(c)
        break
        j+=1
    i+=2
print(a)




        

    