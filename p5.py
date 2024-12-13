# Importing the time module
import time

# Welcoming the user
name = input("What is your name? ")

print("Hello, " + name + "! Time to play hangman!")

# Wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Here we set the secret. You can select any word to play with.
word = "secret"

# Creates a variable with an empty value
guesses = ''

# Determine the number of turns
turns = 10

# Create a while loop
while turns > 0:
    # Make a counter that starts with zero
    failed = 0

    # For every character in secret word
    for char in word:
        # See if the character is in the player's guess
        if char in guesses:
            # Print the character
            print(char, end=" ")
        else:
            # If not found, print a dash
            print("_", end=" ")
            # And increase the failed counter with one
            failed += 1

    # If failed is equal to zero, print "You won"
    if failed == 0:
        print("\nYou won!")
        break

    # Ask the user to guess a character
    guess = input("\nGuess a character: ")
    # Set the player's guess to guesses
    guesses += guess

    # If the guess is not found in the secret word
    if guess not in word:
        # Turns counter decreases with 1 (now 9)
        turns -= 1
        # Print wrong
        print("Wrong")
        # How many turns are left
        print("You have", + turns, 'more guesses')

    # If the turns are equal to zero
    if turns == 0:
        print("You Lose")

