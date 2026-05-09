# Guess the Number Game
# This program generates a random number between 1 and 100.
# The user has to guess the number and the program will guide
# whether the guess should be higher or lower.

import random   # Importing random module to generate random numbers

# Generate a random number between 1 and 100
n = random.randint(1, 100)

# Initial value for user guess
a = -1

# Variable to count number of attempts
guesses = 1

# Loop will run until the user guesses the correct number
while (a != n):

    # Taking input from user
    a = int(input("Guess the number: "))

    # If the guessed number is greater than the random number
    if (a > n):
        print("Lower number please")  # Hint for user
        guesses += 1  # Increase guess counter

    # If the guessed number is smaller than the random number
    elif (a < n):
        print("Higher number please")  # Hint for user
        guesses += 1  # Increase guess counter

# When the correct number is guessed
print(f"You have guessed the number {n} correctly in {guesses} attempts")