n=121
temp=n
r=0
while n>0:
    dig=n%10
    r=r*10+dig
    n=n//10
if (temp==r):
    print("palindrome")
else:
    print("not palindrome")
print(r)
