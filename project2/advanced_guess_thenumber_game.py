# Advanced Guess the Number Game
# This program allows the player to choose a difficulty level,
# guess the number within limited attempts, and replay the game.

import random

print("Welcome to the Guess the Number Game!")

while True:

    # Difficulty selection
    print("\nChoose Difficulty Level:")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 500)")

    level = int(input("Enter your choice (1/2/3): "))

    # Setting range based on difficulty
    if level == 1:
        max_number = 50
        max_attempts = 10
    elif level == 2:
        max_number = 100
        max_attempts = 7
    elif level == 3:
        max_number = 500
        max_attempts = 5
    else:
        print("Invalid choice! Default difficulty selected.")
        max_number = 100
        max_attempts = 7

    # Generate random number
    number = random.randint(1, max_number)

    print(f"\nI have chosen a number between 1 and {max_number}. Try to guess it!")

    attempts = 0
    guessed = False

    # Game loop
    while attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print("Lower number please!")

        elif guess < number:
            print("Higher number please!")

        else:
            print(f" Correct! You guessed the number {number} in {attempts} attempts.")
            guessed = True
            break

        print(f"Attempts left: {max_attempts - attempts}")

    # If player fails
    if not guessed:
        print(f" You lost! The correct number was {number}")

    # Replay option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! ")
        break