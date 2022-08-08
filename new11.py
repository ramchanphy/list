def fun(p1,p2):
    if p1=="scisor" and p2=="paper":
        return("p1 won")
    elif p1=="scisor" and p2=="rock":
        return("p2 won")
    else:
        return("draw")
print(fun(p1=input("enter"),p2=input("enter the ")))
# print(p2=input("enter"))