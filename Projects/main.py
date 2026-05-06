# Snake,water,gun game
import random
computer = random.choice([1,-1,0])
youStr = input("Enter your chose: ")
youDict = {"w":1,"s":-1,"g":0}
reverseDict = {1:"Water",-1:"Snake",0:"Gun"}

you = youDict[youStr]
print(f"You chose : {reverseDict[you]} \ncomputer chose : {reverseDict[computer]}")
if computer == you:
    print("It's a draw")

else:
    if computer == 1 and you == -1:
        print("You won!")
    elif computer == 1 and you == 0:
        print("You lose!")
    elif computer == -1 and you == 1:
        print("You lose!")
    elif computer == -1 and you == 0:
        print("You won!")
    elif computer == 0 and you == -1:
        print("You lose!")
    elif computer == 0 and you == 1:
        print("You won!")
    else:
        print("Somthing wrong!")
