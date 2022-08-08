list=[6,4,2,6,3,2,2,3,5,6,3]
i=0
while i<len(list):
    a=list.count(6)
    b=list.count(4)
    c=list.count(2)
    d=list.count(3)
    e=list.count(5)
    i+=1
print("[",6,":",a,",",4,":",b,",",2,":",c,",",3,":",d,",",5,":",e,"]")