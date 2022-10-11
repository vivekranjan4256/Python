#a person's card is picked out randomly and he will pay the bill
import random
str_inp=input("Enter names of people")
op=str_inp.split(" ")
n=len(op)
index=random.randint(0,n)
print(f"{op[index]} is going to pay the bill.")
# alternate way
random_person=random.choice(op)
print(f"{random_person} is going to pay the bill")
