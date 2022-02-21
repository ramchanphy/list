list=["snake","ant","mouse","horse","eagle","elephant","whale"]
i=0
max=0
count=0
# b=[]
while i<len(list):
    j=0
    while j<len(list[i][j]):
        # if j<len(list[i][j]):
        count=count+1
        j+=1
        
        if max<count:
            max=list[i]
    i+=1
print(max)
        