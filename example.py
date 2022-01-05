student_marks=[23,45,89,90,56,80]
length=len(student_marks)
index=0
total=0
while index<len(student_marks):
    total=student_marks[index]+total
    index=index+1
print("total marks:"+str(total))
