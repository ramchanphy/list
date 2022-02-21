name=["neha","deepti","rani","pooja","chandni","preeti"]
room=[1,2,3]
i=0
s=0
x=2
while i<len(room):
    print("room:",room[i])
    j=s
    a=1
    while j<x:
        print(a,".",name[j])
        j+=1
        a+=1
    x+=2
    i+=1
    s+=2