#check if a number is prime or not
def check_prime(num):
    result=True
    for i in range (2,num):
        if num%i==0:
            result=False
            break
    if result==True:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

number=int(input("Enter a number to be checked: "))
check_prime(number)