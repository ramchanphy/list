numbers=[5,40,23,56,50,12,15,10,70]
i=0
min=0
second_min=0
while i<len(numbers):
    if numbers[i]<min:
        min=numbers[i]
    if numbers[i]>second_min and numbers[i]<min:
        second_min=numbers[i]

    i+=1
print(min)
print(second_min)

