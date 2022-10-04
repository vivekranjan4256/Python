total_bill=float(input("What was the total bill? $"))
percentage=float(input("What percentage tip would you like to give? 10,12, or 15? "))
people=int(input("How many people to split the bill? "))
total=total_bill+(percentage/100)*total_bill
each_person=round(total/people,2)
print(f"Each person should pay: ${each_person}")