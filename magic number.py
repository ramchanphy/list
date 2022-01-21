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
# sum=0
# i=0
# while i<len(magic_square):
#     j=0
#     total=0
#     while j<len(magic_square[i]):
#         total=(magic_square[i][j])+total
#         j+=1
#     i+=1
#     print(total)
# i=0
# a=0
# b=0
# c=0
# while i<len(magic_square):
#     a=a+magic_square[i][0]
#     b=b+magic_square[i][1]
#     c=c+magic_square[i][2]
#     i+=1
# print(a,b,c)
# if a==b==c:
#     print("magic square")
# else:
#     print("not a magic square")



    
    