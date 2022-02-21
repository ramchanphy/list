def minimum(list):
    min1=list[0]
    i=0
    while i<len(list):
        if list[i]<min1:
            min1=list[i]
        i+=1                                   
    return(min1)
print("the minimumis:",minimum([4,6,3,9,6,7,2,5]))