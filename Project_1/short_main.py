import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youStr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

'''if you == computer:
    print("It's a tie!")
else:
    if computer == -1 and you == 1: (computer - you) = -2
        print("You win!")
    elif computer == 1 and you == -1: (computer - you) = 2
        print("You lose!")
    elif computer == 0 and you == 1: (computer - you) = -1
        print("You lose!")
    elif computer == 1 and you == 0: (computer - you) = 1
        print("You win!")
    elif computer == -1 and you == 0: (computer - you) = -1
        print("You lose!")
    elif computer == 0 and you == -1: (computer - you) = 1
        print("You win!")
    else:
        print("Something went wrong!")

   The below logic is written on the basis of the value of computer you        
'''
if computer == you:
    print("It's a tie!")
elif computer - you == 1 or computer - you == -2:
    print("You win!")
else:
    print("You lose!")
