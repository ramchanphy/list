money= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
crore=0
lakh=0
dilwale=0
while i<len(money):
    if money[i]>=10000000:
        crore+=1
    elif money[i]>=100000 and money[i]<10000000:
        lakh+=1
    else:
        dilwale+=1
    i+=1
print("crorepati =",crore)
print("lakhpati =",lakh)
print("dilwale =",dilwale)
        