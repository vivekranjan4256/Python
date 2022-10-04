# and , or , not
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
age=int(input("What is your age? "))
if height>=120:
    print("You can ride the rollercoaster!")
    if age<=12:
        print("Please pay $5")
    elif age<=18:
        print("Please pay $7")
    elif age>=45 and age<=55:
        print("Have a free ride")
    else:
        print("Please pay $12")
else:
    print("You cannot ride the rollercoaster.")