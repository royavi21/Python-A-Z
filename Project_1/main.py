'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youStr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if you == computer:
    print("It's a tie!")
else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 0 and you == 1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 0 and you == -1:
        print("You win!")
    else:
        print("Something went wrong!")

'''
output:
Enter your choice: w
You chose Water
Computer chose Gun
You win!
'''