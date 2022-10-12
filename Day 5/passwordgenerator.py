import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'
                ,'W','X','Y','Z']
symbols=['!','#','$','%','&','(',')','*','+']
numbers=['0','1','2','3','4','5','6','7','8','9']


print("Welcome to the PyPassword Generator!")
letters_input=int(input("How many letters would you like in your password?\n"))
symbols_input=int(input("How many symbols would you like?\n"))
numbers_input=int(input("How many numbers would you like?\n"))

#Easy
password=""
for i in range (1,letters_input+1):
    password+=random.choice(letters)
for i in range (1,symbols_input+1):
    password+=random.choice(symbols)
for i in range (1,numbers_input+1):
    password+=random.choice(numbers)
print(password)

#Hard
password_list=[]
for i in range (1,letters_input+1):
    password_list.append(random.choice(letters))
for i in range (1,symbols_input+1):
    password_list.append(random.choice(symbols))
for i in range (1,numbers_input+1):
    password+=random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
result=""
for character in password_list:
    result+=character
print(f"Your password is {result}")
