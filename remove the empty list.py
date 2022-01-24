list=['My'," ",'name'," ","is"," ",'Tanu']
substr=" "
a=[]
i=0
while i<len(list):
    if list[i]!=substr:
        a.append(list[i])
    i+=1
print(a)