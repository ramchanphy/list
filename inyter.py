# list="Pooja","Goupta"
# str=""
# i=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         if list[i][j]==list[i][0]:
#             c=list[i][0]
#             str=str+c+"."
#         j+=1
#     i+=1
# print(str[0:3])

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list=["h","i","j"]
i=0
while i<len(list1):
    if sub_list[i] not in list1:
        list1[2][1][2].append(sub_list[i])
        if i==2:
            break
    i+=1
print(list1)