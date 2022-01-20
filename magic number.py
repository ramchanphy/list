magic_square=[
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
sum=0
i=0
while i<len(magic_square):
    j=0
    total=0
    while j<len(magic_square[i]):
        total=(magic_square[i][j])+total
        j+=1
    i+=1
    print(total)

    
    