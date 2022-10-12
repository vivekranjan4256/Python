# if number is divisible by 3 print Fizz
# if number is divisible by 5 print Buzz
# if number is divisible by both 3 and 5 print FizzBuzz
for i in range(1,101):
    if i%15==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)