s="A man, a plan, a canal:Panama"
a=""
b=""
i=0
while i<len(s):
    if s[i]!="," and s[i]!=" " and s[i]!=":":
        a+=s[i]
    i+=1
b+=a.lower()
j=-1
c=""
while j>=(-(len(b))):
    c+=(b[j])
    j-=1
print(c)
if b==c:
    print(True)
else:
    print(False)
