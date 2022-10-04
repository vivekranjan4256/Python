direction=input("left or right: ")
if direction=="left":
    con1=input("swim or wait: ")
    if con1=="wait":
        door=input("Red, Blue or Yellow door: ")
        if door=="Yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")