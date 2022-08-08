l="abcabcbb"
b=""
c=0
i=0
while i<len(l):
    if l[i] not in b:
        b.append(l[i])
        c+=1
    i+=1
print(c)