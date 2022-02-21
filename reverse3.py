num=int(input("enter the number"))
n=str(num)
i=1
s=""
while i<=len(n):
    a=n[-i]
    s=s+a
    i+=1
print(int(s))