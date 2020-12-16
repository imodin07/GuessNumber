import random

# Random initializes the random number generator.

def Guess(x):
    randomNumber = random.randint(1, 20)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}:- "))
        if guess < randomNumber:
            print("Sorry number is too low. Try Again")
        elif guess > randomNumber:
            print("Sorry number is too high. Try Again")

    print(f"Yes!! You guessed the number {randomNumber} correctly.")

Guess(20)

