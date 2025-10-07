import random
n=random.randint(1,100)
a = -1
guesses = 1
while (a != n):
    a=int(input("Guess the number: "))
    
    if (a>n):
        print("Lower number please")
        guesses +=1
    else:
        print("Higher number please")
        guesses +=1
        
print(f"You guessed the number {n} in ({guesses}) guesses attempt")