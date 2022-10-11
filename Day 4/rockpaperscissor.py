import random
arr=["Rock","Paper","Scissor"]
choice=int(input("What do you choose? Tupe 0 for Rock, 1 for Paper, 2 for Scissors."))
compinput=random.randint(0,2)
print(f"You chose {arr[choice]}")
print(f"Computer chose {arr[compinput]}")
if choice==0 and compinput==2:
    print("You Win")
elif choice==0 and compinput==1:
    print("You Loose")
elif choice==0 and compinput==0:
    print("Draw")
elif choice==1 and compinput==0:
    print("You Loose")
elif choice==1 and compinput==1:
    print("Draw")
elif choice==1 and compinput==2:
    print("You Loose")
elif choice==2 and compinput==0:
    print("You Loose")
elif choice==2 and compinput==1:
    print("You Win")
elif choice==2 and compinput==2:
    print("Draw")
else:
    print("Invalid choice.")