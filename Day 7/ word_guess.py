import random
word_list=["ardvark","baboon","camel"]
random_word=random.choice(word_list)
length=len(random_word)
display=[]
# print(f"Random choosen word is {random_word}")
for letter in random_word:
    display.append("_")
end=False
lives=6
while not end:
    guess_letter=input("Guess a letter: ").lower()
    if guess_letter in display:
        print(f"You have already guessed {guess_letter}")
    for i in range (0,length):
        if guess_letter==random_word[i]:
            display[i]=guess_letter
    if guess_letter not in random_word:
        print(f"You guesssed {guess_letter}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            print("You Loose")
            end=True
    print(f"{lives} guesses left")
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You Win")
        end=True


