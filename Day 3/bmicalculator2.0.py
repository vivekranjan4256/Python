height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kgs"))
bmi=weight/(height**2)
print(round(bmi,2))
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("overweight")
elif bmi<35:
    print("obese")
else:
    print("clinically obese")