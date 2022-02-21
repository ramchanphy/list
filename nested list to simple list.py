a=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    b.append(a[i][j][k])
                    k+=1
            else:
                b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
print(b)   

# print(a[0])
# print(a[1])
# print(a[2][0])
# print(a[2][1][0])
# print(a[2][1][1])
# print(a[2][2][0])
# print(a[2][2][1])
# print(a[2][3])
# print(a[3])
# print(a[4])
# print(a[5])             