#create a program using maths and f-Strings that tells us how many days,weels,months we have left if we live until 90
#years old
#It will take your current age as the input and output a message
#with out time left in this format:
age=int(input("Enter your age: "))
days=(90-age)*365
weeks=(90-age)*52
months=(90-age)*12
print(f"You have {days} days , {weeks} weeks , and {months} months left.")