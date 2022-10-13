import random
word_list=["ardvark","baboon","camel"]
random_word=random.choice(word_list)
guess_letter=input("Guess a letter: ").lower()
for letter in random_word:
    if letter==guess_letter:
        print("Right")
    else:
        print("Wrong")
print(f"Random choosen word is {random_word}")