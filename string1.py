mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacement=0
str=mainStr.split()
i=0
while i<len(str):
    if str[i]==subStr:
        del str[i]
    else:
        print(str[i],end=" ")
    i+=1
