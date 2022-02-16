magic_square=[
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    row=0
    column=0
    diagonal=0
    while j<len(magic_square):
        row=row+magic_square[i][j]
        column=column+magic_square[j][i]
        diagonal=diagonal+magic_square[j][j]
        j+=1
    i+=1
print(row,"=sum of row")
print(column,"=sum of column")
print(diagonal,"=sum of diaginal")
if row==column==diagonal:
    print("magic_square")
else:
    print("not magic_square")
sum=0



    
    