a=["a",17,12,"a",17,18,"b",17,14,12,19,17,"b",12,13,11]
b=[]
for i in a:
    if i not in b and str(i).isdigit():
        b.append(i)
print(b)







