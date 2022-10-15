import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level=="hard":
    no_of_attempts=5
elif difficulty_level=="easy":
    no_of_attempts=10
no_to_guess=random.randint(1,100)
print(no_to_guess)
game_finished=False
for i in range (no_of_attempts):
    print(f"You have {no_of_attempts-i} attempts remaining to guess the number.")
    user_num=int(input("Make a guess: "))
    if user_num==no_to_guess:
        print(f"You Win. The number was {no_to_guess}")
        game_finished=True
        break
    elif user_num>no_to_guess:
        print("Too high.")
    elif user_num<no_to_guess:
        print("Too low.")
if game_finished==False:
    print(f"You've run out of guesses, you lose. The number was {no_to_guess}")