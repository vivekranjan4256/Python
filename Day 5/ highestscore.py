student_scores=input("Enter student score: ").split()
for i in range (0,len(student_scores)):
    student_scores[i]=int(student_scores[i])
result=-1
for score in student_scores:
    if score>result:
        result=score
print(f"The highest score in the class is: {result}")
