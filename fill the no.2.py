list=[1,2,4,5,7,9,11]
i=0
max=0
while i<len(list):
    if list[i]>1 and list[i]<len(list):
        list=max
    i+=1
    print(max)