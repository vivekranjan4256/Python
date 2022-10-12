student_heights=input("Enter student heights: ").split()
for i in range (0,len(student_heights)):
    student_heights[i]=int(student_heights[i])
print(student_heights)
length=0
for i in student_heights:
    length+=1
# print(length)
sum=0
for height in student_heights:
    sum=sum+height
average_height=sum/length
print(round(average_height))