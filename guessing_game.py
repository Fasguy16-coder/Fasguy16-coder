python
import random

def guessing_game():
    number = random.randint(1, 10)
    attempts = 3

    print("Welcome to the Guessing Game! You have 3 attempts to guess the correct number between 1 and 10.")

    for _ in range(attempts):
        guess = int(input("Enter your guess: "))
        
        if guess == number:
            print("Congratulations! You guessed the correct number.")
            return
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    
    print(f"Sorry, you didn't guess the correct number. The correct number was {number}.")

guessing_game()
