numbers=[5,40,23,5,56,12,15,10,70]
i=0
second_max=numbers[0]
largest=numbers[0]
while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    if numbers[i]>second_max and numbers[i]!=largest:
        second_max=numbers[i]
    i+=1
print(largest)
print(second_max)