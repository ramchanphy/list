elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
sum2=0
even=0
odd=0
while i<len(elements):
    sum=sum+elements[i]
    
    if elements[i]%2==0:
        even=even+1
        sum1=elements[i]+sum1
    else:
        odd+=1
        sum2=elements[i]+sum2
    i+=1
avg=sum//len(elements)
avg1=sum1//even
avg2=sum2//odd
print("count of all the elements=",i)
print("count of the even elements =",even)
print("count of the odd elements =",odd)
print("sum of all the elements =",sum)
print("sum of the even =",sum1)
print("sum of the odd =",sum2)
print("average of all the numbers =",avg)
print("average of even numbers are =",avg1)
print("average of odd numbers are =",avg2)
