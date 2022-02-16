# list="1234abcd"[::-1]
# print(list)

#write a program to reverse a string 
#string="1234abcd"
# list="1234abcd"
# i=-1
# while i>=(-(len(list))):
#     print(list[i],end="")
#     i-=1

#write a function to multiply all the numbers in a list.
#list:(8,2,3,-1,7)
#output(-336)
# list=[8,2,3,-1,7]
# len=len(list)
# i=0
# product=1
# while i<len:
#     a=
#     product=product*list
#     i+=1
# print(product)

list=[]
len=int(input("enter the length of the list"))
i=0
product=1
while i<len:
    a=int(input("enter the number"))
    list.append(a)
    product=product*a
    i+=1
print("list",list)
print([product])



    





