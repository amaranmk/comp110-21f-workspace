"""An example of conditional (if-else) statements."""

__author__ = "730484862"

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else:
    print("Sorry, you guess incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print("Game over.")
 