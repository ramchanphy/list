magic_square=[
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    l=len(magic_square)-1
    while j<len(magic_square[i]):
        a+=magic_square[i][j]
        b+=magic_square[i][j]
        c+=magic_square[i][j]
        d+=magic_square[j][j]
        e+=magic_square[j][j]
        f+=magic_square[j][j]
        g+=magic_square[i][j]
        h+=magic_square[j][l]
        l-=1
        j+=1
    i+=1
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print()
if a==b==c:
    print("magic_square")
else:
    print("not magic squre")

        
        