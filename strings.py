mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
x=mainStr.split()
a=[]
i=0
while i<len(x):
    if x[i]!=subStr:
        a.append(x[i])
    i+=1
print(" ".join(a))


        
        