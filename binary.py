binary_number=[1,0,0,1,1,0,1,1]
i=len(binary_number)-1
decimal=0
c=1
while i>=0:
    decimal=decimal+int(binary_number[i]/c)
    c=c/2
    i-=1
print(decimal)

