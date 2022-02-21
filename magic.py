magic_square=[
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    sum1=0
    f=len(magic_square)-1
    while j<len(magic_square):
        sum=sum+magic_square[j][j]
        sum1=sum1+magic_square[j][f]
        j+=1
        f-=1
    i+=1
print(sum)
print(sum1)