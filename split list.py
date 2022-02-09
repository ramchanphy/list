list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
a=[]
step=3
i=0
while i<step:
    a.append(list[i::step])
    i+=1
print(a)