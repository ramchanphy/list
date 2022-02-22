list=[[0],[1,2,3],[6,7,8,9,5],[5,10]]
i=0
max=[0]
a=[]
while i<len(list):
    if max<list[i]:
        max=list[i]
    i+=1
print(max)