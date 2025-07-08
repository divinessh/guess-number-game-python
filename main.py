#To produce random numbers
import random

#Function to execute program
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("****NUMBER GUESSING GAME USING PYTHON****")
    print("Try guessing a number between 1 and 100!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("TOO LOW! Try again.")
            elif guess > number_to_guess:
                print("TOO HIGH! Try again.")
            else:
                print(f"CORRECT! The number was {number_to_guess}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a VALID number.")

#Execute game
guess_the_number()
